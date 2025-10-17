from PIL import Image

cards = {
    "Новый год": "newyear.jpg",
    "День рождения": "birthday.jpg",
    "8 марта": "march8.jpg"
}

holiday = input("К какому празднику нужна открытка? ")
filename = cards.get(holiday)

if filename:
    image = Image.open(filename)
    image.show()
else:
    print("Нет открытки к такому празднику.")
