from PIL import Image

image = Image.open("./images/input.png")

resized_image = image.resized((300, 300))

print("toto")