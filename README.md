# Image Processing Pipeline

## Description
Ce projet implémente une pipeline Python pour traiter un dossier d'images, redimensionner chaque image en format carré, appliquer un padding si nécessaire, et sauvegarder les images traitées dans un dossier de sortie unique.

## Structure du Projet
La structure des dossiers est la suivante :
```
.
├── datasets/          # Dossier contenant les images traitées (généré automatiquement)
├── input_images/      # Dossier contenant les images source à traiter
└── main.py            # Point d'entrée pour exécuter la pipeline
└── src/
    ├── image_processor.py    # Code de la classe ImageProcessor
```

## Prérequis
Assurez-vous d'avoir installé toutes les dépendances requises en exécutant la commande suivante :
```bash
pip install -r requirements.txt
```

## Utilisation
1. **Ajouter vos images** : Placez les images à traiter dans le dossier `input_images/`.
2. **Exécuter la pipeline** : Depuis le dossier racine du projet, lancez le script `main.py` :
   ```bash
   python main.py
   ```
3. **Résultats** : Les images traitées seront sauvegardées dans un sous-dossier unique dans `datasets/`, nommé par un horodatage de la forme `YYYYMMDDHHMMSS`.

## Détails de la Pipeline
- **Redimensionnement** : Les images sont redimensionnées tout en gardant leur ratio d'aspect d'origine.
- **Padding** : Un padding uniforme de couleur `(114, 114, 144)` est ajouté si l'image n'est pas déjà carrée, pour la transformer en un carré parfait.
- **Nom unique pour chaque exécution** : Chaque traitement crée un dossier unique dans `datasets/`, pour éviter d'écraser les résultats d'exécutions précédentes.

## Configuration et Tests
- **Configuration PyCharm** : Configurez `main.py` comme script principal dans PyCharm pour lancer la pipeline rapidement.
- **Tests et Vérifications** : Le code est formaté et vérifié avec un linter pour garantir la qualité et la lisibilité du code.

## Auteur
Ce projet a été réalisé par **Younes Bokhari** dans le cadre d'un exercice pédagogique.
