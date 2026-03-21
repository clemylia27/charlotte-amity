from cog import BasePredictor, Input, ConcatenateIterator
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from threading import Thread
import torch

class Predictor(BasePredictor):
    def setup(self):
        """Chargement unique du modèle Charlotte-Amity"""
        self.model_id = "Finisha-f-scratch/Charlotte-Amity"
        
        print(f"Chargement de {self.model_id}...")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_id)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_id,
            torch_dtype=torch.float16,
            device_map="auto"
        )

    def predict(
        self,
        prompt: str = Input(description="Ton message pour Charlotte"),
        max_tokens: int = Input(description="Longueur max de la réponse", default=100, ge=1, le=128),
        temperature: float = Input(description="Créativité (0.1 à 1.5)", default=0.4),
        top_p: float = Input(description="Filtrage nucleus", default=0.3),
    ) -> ConcatenateIterator[str]:
        """Génère le texte en temps réel (Streaming)"""
        
        # Préparation des entrées
        inputs = self.tokenizer(prompt, return_tensors="pt").to("cuda")
        
        # Configuration du streamer pour l'envoi mot à mot
        streamer = TextIteratorStreamer(self.tokenizer, skip_prompt=True, skip_special_tokens=True)
        
        generation_kwargs = dict(
            **inputs,
            streamer=streamer,
            max_new_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            do_sample=True if temperature > 0 else False,
        )

        # Lancer la génération dans un thread pour ne pas bloquer le stream
        thread = Thread(target=self.model.generate, kwargs=generation_kwargs)
        thread.start()

        # Envoyer les morceaux de texte au fur et à mesure
        for new_text in streamer:
            yield new_text
          
