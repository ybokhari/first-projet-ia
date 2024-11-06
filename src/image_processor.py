"""Module de traitement d'images pour redimensionner et appliquer un padding aux images."""

import os
from datetime import datetime

from PIL import Image


class ImageProcessor:
    """Classe pour traiter les images : redimensionnement et padding pour obtenir un format carré."""

    def __init__(self, input_path: str):
        """
        Initialise le processeur d'images avec le chemin du dossier contenant les images.

        :param input_path: Chemin relatif du dossier contenant les images d'entrée.
        """
        self.input_path = input_path

    def process_folder(self, output_size: int):
        """
        Traite toutes les images du dossier spécifié puis sauvegarde les images.

        :param output_size: Taille du côté de l'image carrée résultante (en pixels).
        """
        output_folder = os.path.join(
            "datasets", datetime.now().strftime("%Y%m%d%H%M%S")
        )
        os.makedirs(output_folder, exist_ok=True)

        for filename in os.listdir(self.input_path):
            image_path = os.path.join(self.input_path, filename)
            if not os.path.isfile(image_path):
                continue

            img = self.process_image(image_path, output_size)
            output_path = os.path.join(output_folder, filename)
            img.save(output_path)

    def process_image(self, image_path: str, output_size: int) -> Image:
        """
        Ouvre et traite une image : redimensionne et applique un padding pour obtenir un format carré.

        :param image_path: Chemin de l'image à traiter.
        :param output_size: Taille du côté de l'image carrée résultante (en pixels).
        :return: Image traitée.
        """
        img = Image.open(image_path)
        img = self.resize_to_square(img, output_size)
        img = self.add_padding(img, output_size)
        return img

    @staticmethod
    def resize_to_square(img: Image, output_size: int) -> Image:
        """
        Redimensionne l'image pour qu'elle s'ajuste au format carré tout en gardant le ratio d'aspect.

        :param img: Image à redimensionner.
        :param output_size: Taille du côté de l'image carrée.
        :return: Image redimensionnée.
        """
        # Calcul du ratio et des nouvelles dimensions
        width, height = img.size
        if height > width:
            new_height = output_size
            new_width = int(output_size * width / height)
        else:
            new_width = output_size
            new_height = int(output_size * height / width)

        return img.resize((new_width, new_height))

    @staticmethod
    def add_padding(img: Image, output_size: int) -> Image:
        """
        Ajoute un padding pour obtenir un format carré si nécessaire.

        :param img: Image redimensionnée.
        :param output_size: Taille du côté de l'image carrée.
        :return: Image avec padding.
        """
        # Création d'un nouveau canevas carré de couleur uniforme
        new_img = Image.new("RGB", (output_size, output_size), (114, 114, 144))
        img_width, img_height = img.size

        # Calcul de la position pour centrer l'image
        top_left_x = (output_size - img_width) // 2
        top_left_y = (output_size - img_height) // 2

        new_img.paste(img, (top_left_x, top_left_y))
        return new_img
