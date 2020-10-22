from PIL import Image
import numpy as np

im = Image.open("fruit_fade.png")
pix = np.array(im)

# get the maximum value
maximum = np.max(pix)

# calculate the scaling factor
scale = 255.0/maximum

# create the new 2D array
new_pix = []
for row in pix:
    new_row = []
    for pixel in row:
        new_row.append(pixel * scale + 100)
    new_pix.append(new_row)

new_pix = np.array(new_pix).astype('uint8')

im2 = Image.fromarray(new_pix)
im2.show()

# I don't understand the properties of pixels enough to understand how to maximize contrast