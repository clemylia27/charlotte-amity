from cog import BasePredictor, Input
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class Predictor(BasePredictor):
    def setup(self):
        """Chargement du modèle au démarrage"""
        self.model_name = "Finisha-F-scratch/Charlotte-amity"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            torch_dtype=torch.float16,
            device_map="auto"
        )

    def predict(self,
                prompt: str = Input(description="Ton texte pour Charlotte"),
                max_length: int = Input(description="Longueur de la texture", default=100)
               ) -> str:
        """Génération de la réponse"""
        inputs = self.tokenizer(prompt, return_tensors="pt").to("cuda")
        outputs = self.model.generate(**inputs, max_new_tokens=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
