import csv
import textwrap
from tqdm import tqdm
from PIL import Image, ImageFont, ImageDraw

# Settings
font = ImageFont.truetype("ArbutusSlab.ttf", 50)
print("[STATUS] Initializing...")

with open('quotes.txt') as f:
    quotes = f.readlines()


def draw(quote):
    img = Image.open("Image.png")
    text = "Quote of the Day:\n" + textwrap.fill(quote, 43)
    image_editable = ImageDraw.Draw(img)
    image_editable.text((150, 1050), text, (255, 255, 255), font=font, spacing=30)
    img.save(f"images/{quote[0:20]}.png")
    return None

for q in tqdm(quotes):
    draw(q)

print("[STATUS] All Done!")
