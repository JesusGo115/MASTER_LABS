
from PIL import Image
im = Image.open('god.jpg')

def negative_image1(pixel):
    return tuple(map(lambda a : 255 - a, pixel))

negative_list = map( negative_image1, im.getdata() )

im.putdata(list(negative_list))

def negative_image2(pixel):
     return tuple(map(lambda a : 255 + a, pixel))
negative_list = map( negative_image2, im.getdata())

im.putdata(list(negative_list)) 

im.show()
