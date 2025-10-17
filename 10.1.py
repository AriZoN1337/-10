from PIL import Image

image = Image.open("card.jpg")


cropped = image.crop((50, 50, 400, 300))

cropped.save("card_cropped.jpg")
cropped.show()
