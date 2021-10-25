from PIL import Image, ImageDraw, ImageFont

WIDTH = 1024
HEIGTH = 1024
FILE_NAME_SUFFINX = "_raw.png"


def create(number: str, color=(255, 255, 255), background=(73, 109, 137)):
    img = Image.new('RGB', (WIDTH, HEIGTH), color=background)
    font = ImageFont.truetype('../fonts/OrelegaOne-Regular.ttf', 450 + size_plus(number))
    img = center_text(img, font, number, color=color)
    file_name = "../output/raw/" + number + FILE_NAME_SUFFINX
    img.save(file_name)
    return file_name


def add_number(number: str, color=(255, 255, 255)):
    img = Image.open("../output/words/" + number + ".png")
    font = ImageFont.truetype('../fonts/OrelegaOne-Regular.ttf', 400 + size_plus(number))
    img = center_text(img, font, number, color=color)
    file_name = "../output/final/" + number + ".png"
    img.save(file_name)
    return file_name


def center_text(img, font, text, color):
    draw = ImageDraw.Draw(img)
    text_width, text_height = draw.textsize(text, font)
    text_height += int(text_height*0.21) #https://stackoverflow.com/questions/55773962/pillow-how-to-put-the-text-in-the-center-of-the-image
    position = ((WIDTH-text_width)/2,(HEIGTH-text_height)/2)
    draw.text(position, text, color, font=font)
    return img


def size_plus(number):
    if int(number) < 10:
        return 300
    if int(number) < 100:
        return 200
    if int(number) < 1000:
        return 100
    return 0

if __name__ == "__main__":
    import random
    create("5", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    #add_number("1")