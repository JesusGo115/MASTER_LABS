from PIL import Image

im = Image.open('god.jpg')

def sunset(picture):
    new_list = []
    for p in picture.getdata():
        temp = (p[0], int(p[1] * 0.5), int(p[2] * 0.3))
        new_list.append(temp)
    picture.putdata(new_list)
    im.show()
sunset(im)

