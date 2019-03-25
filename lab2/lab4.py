from PIL import Image

im = Image.open("roblox_head.jpeg")

print(im.format, im.size, im.mode)

im.show()

