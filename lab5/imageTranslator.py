from PIL import Image

im = Image.new('L', (29, 18), color = 'white')

arr = []

with open ("imagenum.txt", "r") as A:
    arr = [line.split() for line in A]

for i in range(29):
    for x in range(18):
        z = int(arr[i][x])
        im.putpixel((i,x), z)

im.show()

