from urllib.request import Request, urlopen
import random
import urllib.request
from bs4 import BeautifulSoup
from pprint import pprint
import numpy as np
import cv2

# TASK 2

aSite = 'https://www.google.com/'

returning = urlopen(aSite)

object1 = BeautifulSoup(returning, 'html.parser')

for link in object1.findAll("img"):
    temp = link.get('src')
    if temp[:1] == "/":
        image = aSite + temp
print(image)

newSite = urlopen('https://bigmemes.funnyjunk.com/pictures/This+is+so+sad_db2afd_7008045.jpg')

image2 = np.asarray(bytearray(newSite.read()), dtype="uint8")
image2 = cv2.imdecode(image2, cv2.IMREAD_COLOR)

print(image2)

# TASK 3

imURL = 'https://bigmemes.funnyjunk.com/pictures/This+is+so+sad_db2afd_7008045.jpg'

def downloadImage(url):
    name = 'sbeve'
    full = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full)

downloadImage(imURL)

#convert image to grayscale
sbeve = cv2.imread('sbeve.jpg', cv2.IMREAD_GRAYSCALE)

sbeve_remap = cv2.applyColorMap(sbeve, cv2.COLORMAP_HOT)

# use highgui to display image
cv2.imshow("Hot Meme", sbeve_remap)

# keeps the image displayed
cv2.waitKey()


sbeve_remap = cv2.applyColorMap(sbeve, cv2.COLORMAP_RAINBOW)

cv2.imshow("Sbeve on Drugs", sbeve_remap)

cv2.waitKey()

