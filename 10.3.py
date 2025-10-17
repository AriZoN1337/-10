from PIL import Image, ImageDraw, ImageFont

name = input("Введите имя, кого хотите поздравить: ")

image = Image.open("birthday_congrats.jpg").convert("RGBA")

txt = Image.new("RGBA", image.size, (255, 255, 255, 0))
draw = ImageDraw.Draw(txt)

try:
    font = ImageFont.truetype("arialbd.ttf", 40)  # bold
except:
    font = ImageFont.load_default()

text = f"{name}, поздравляю!"
text_width, text_height = draw.textsize(text, font=font)

position = ((image.width - text_width) // 2, image.height - text_height - 20)

draw.text(position, text, font=font, fill=(255, 0, 0, 255))  # красный цвет

final = Image.alpha_composite(image, txt)
final.save("birthday_congrats.png")
final.show()
