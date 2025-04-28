from PIL import ImageFont, ImageDraw, Image

image = Image.open('test.png')
draw = ImageDraw.Draw(image)

# use a bitmap font
# font = ImageFont.load("arial.pil")
# font = ImageFont.load("megamax-jonathan-too-font/MegamaxJonathanToo-YqOq2.ttf")
# font = ImageFont.load("arial/arialceb.ttf")
# font = ImageFont.truetype(font="SFNS.ttf")
# draw.text((10, 10), "hello", font=font)

# use a truetype font
# font directory: /Library/Fonts/, /System/Library/Fonts/ and ~/Library/Fonts/ on macOS.
font = ImageFont.truetype(font="SFNS.ttf", size=200)

draw.text((100, 50), "hello chenzuoli.", font=font)

image.show()
