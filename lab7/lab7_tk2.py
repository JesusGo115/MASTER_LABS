from PIL import Image

def task2():
    
    im1 = Image.open("cat.png")

    im2 = Image.open('ball.png')

    im3 = Image.open('google.JPEG')

    newIM = Image.new("RGB", (640,480), "white")

    target_x = 70
    for source_x in range(im1.width):
        target_y = 70
        for source_y in range(im1.height):
            color = im1.getpixel((source_x, source_y)) # get pixels from the source
            newIM.putpixel((target_x, target_y), color) # put pixels onto target
            target_y += 1
        target_x +=1

    target_x = 400
    for source_x in range(im2.width):
        target_y = 70
        for source_y in range(im2.height):
            color = im2.getpixel((source_x, source_y)) # get pixels from the source
            newIM.putpixel((target_x, target_y), color) # put pixels onto target
            target_y += 1
        target_x +=1

    target_x = 250
    for source_x in range(im3.width):
        target_y = 350
        for source_y in range(im3.height):
            color = im3.getpixel((source_x, source_y)) # get pixels from the source
            newIM.putpixel((target_x, target_y), color) # put pixels onto target
            target_y += 1
        target_x +=1


    newIM.save("task2_images.png")

task2()
