"""Point d'entrée principal pour exécuter la pipeline de traitement d'images."""

from src.image_processor import ImageProcessor


def main():
    """Exécute la pipeline de traitement d'images."""
    # Initialisation de l'instance avec le chemin du dossier des images source
    processor = ImageProcessor("input_images")
    # Traitement des images avec une taille de sortie souhaitée de 640 pixels
    processor.process_folder(output_size=640)


if __name__ == "__main__":
    main()
