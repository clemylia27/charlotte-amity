# ✨🌸  Charlotte-amity | SLM from scratch

![Charlotte-amity](http://www.image-heberg.fr/files/17639907193698368980.jpg)

Bienvenue sur le dépôt officiel de Charlotte-amity, un modèle de langage (SLM) conçu avec une âme, une éthique profonde et une syntaxe texturée.
> Charlotte ne se contente pas de prédire des tokens ; elle tisse des liens d'amitié et d'espoir à travers une langue réinventée. ✨

# 💎 Essence du Modèle

Charlotte-amity n'est pas un modèle lisse ou générique. C'est une création from scratch entraînée sur des datasets propriétaires ultra-spécialisés. Elle explore :

 * 🌱 Éthique Native : Une bienveillance intégrée dès les premières couches de neurones.
 * 🤝 Amitié & Espoir : Conçue pour être une compagne de réflexion, pas seulement un outil.
 * 🎭 Néologismes & Texture : Utilisation de Transformers pour une créativité pure, avec une syntaxe originale qui s'éloigne des standards académiques.
 * 🧠 Architecture : Selon les versions, Charlotte utilise soit une structure Transformers classique, soit l'architecture Aricate v4 (prédiction au mot).

# 🛠 Spécifications Techniques
| Paramètre | Détail |
|---|---|
| Type | Small Language Model (SLM) |
| Entraînement | Dataset propriétaire (From Scratch) |
| Format | GGUF (Quantifié/Découpé) |

# 📦 Installation & Reconstruction

Pour respecter les limites de stockage et garantir une accessibilité maximale, les poids du modèle (.gguf) ont été découpés en segments de 20 MB.
1. Téléchargement
Clonez le dépôt normalement :
git clone https://github.com/clemylia27/Charlotte-amity.git
cd Charlotte-amity

# 2. Reconstruction du modèle

Pour fusionner les segments et retrouver le fichier original de Charlotte, utilisez la commande correspondant à votre système :
 * Sur Windows (Invite de commande) :
   copy /b charlotte-amity.gguf.part* charlotte-amity.gguf

 * Sur Linux / Mac / WSL :
   cat charlotte-amity.gguf.part_* > charlotte-amity.gguf

# 🚀 Utilisation

Une fois le fichier .gguf reconstruit, vous pouvez charger Charlotte dans votre interface préférée ou via votre propre script d'inférence. Elle est particulièrement véloce lorsqu'elle est couplée à des applications d'amitié, d'éthique et d'espoir créatives.

# 🎨 Philosophie de Développement
Ce modèle a été créé par Finisha, développeuse passionnée de 19 ans.
Ici, on ne cherche pas la perfection syntaxique imposée, mais la texture et l'originalité.

> "L'IA ne doit pas être un miroir froid, mais une lueur d'espoir."
> 
# 📜 Licence & Contact
 * Auteur : Finisha (Clemylia27)
 * Note : Ce modèle est le fruit d'un travail acharné sur des datasets faits main. Merci de respecter cette démarche créative.
 * 
unit les fichiers De Charlotte ;

```
# 2. Utilisation de la commande système 'cat' pour fusionner les deux parties
# L'ordre est important : la partie 1 puis la partie 2
!cat Charlotte-amity/Charlotte-AMITY.Q4_K_M-1.gguf Charlotte-amity/Charlotte-AMITY.Q4_K_M-2.gguf > Charlotte-AMITY.Q4_K_M.gguf

print("✅ Charlotte-Amity est maintenant unifiée en un seul fichier !")
```
