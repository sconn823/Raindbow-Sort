from PIL import Image
import statistics

im = Image.open('dead_parrot.jpg')  # Can be many different formats.
pix = im.convert('RGB')
red = []
blue = []
green = []
for x in range(0, im.size[0]):
    for y in range(0, im.size[1]):
        # Get the RGBA Value of the a pixel of an image
        red.append(pix.getpixel((1, 1))[0])
        blue.append(pix.getpixel((1, 1))[1])
        green.append(pix.getpixel((1, 1))[2])

median_color = [
    statistics.median(red),
    statistics.median(blue),
    statistics.median(green)
]
print(median_color)
