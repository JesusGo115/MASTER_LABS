'''
Lab7
The code interates through the image and finds out what the reddest pixel
in the image and shows the coordinates of that red pixel.

author: Jesus "Chuy" Gomez
date: 17 February 2019
'''

from PIL import Image

im = Image.open('apple.jpg')

width, height = im.size

print(width)
print(height)

pixel_list = []

for x in range(int(width)):
    for y in range(int(height)):

        #print("Coordinates: ", (x, y))
        pixel_list = im.getpixel((x, y))
        #print(pixel_list[0])
        if int(pixel_list[0]) == 255:
            print("One of the image's largest red component is on the coordinate: ", (x, y))
