import textwrap
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw


def create_quote_image(quote):
    image = Image.open("static/template.jpg")
    font = ImageFont.truetype(
        "static/Times New Roman.ttf", 48, encoding="unic")

    image_width, image_height = (image.width - 300, image.height - 25)

    draw = ImageDraw.Draw(image)
    lines = textwrap.wrap(quote, width=20)

    font_width, font_height = font.getsize(quote)
    text_y = (image_height - font_height * len(lines)) / 2

    for line in lines:
        font_width, font_height = font.getsize(line)
        text_x = (image_width - font_width) / 2

        draw.text((text_x, text_y), line, (0, 0, 0), font)
        text_y += font_height

    file = BytesIO()

    image.save(file, format="PNG")
    file.seek(0)

    return file
