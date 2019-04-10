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

newSite = urlopen(image)

image2 = np.asarray(bytearray(newSite.read()), dtype="uint8")
image2 = cv2.imdecode(image2, cv2.IMREAD_COLOR)

print(image2)

# TASK 3

def downloadImage(url):
    name = 'google'
    full = str(name) + '.png'
    urllib.request.urlretrieve(url, full)

downloadImage(image)

#convert image to grayscale
goog = cv2.applyColorMap(image2, cv2.COLORMAP_BONE)

goog_remap = cv2.applyColorMap(image2, cv2.COLORMAP_HOT)

# use highgui to display image
cv2.imshow("Hot Google", goog_remap)

# keeps the image displayed
cv2.waitKey()

goog_remap = cv2.applyColorMap(image2, cv2.COLORMAP_RAINBOW)

cv2.imshow("Google on Drugs", goog_remap)

cv2.waitKey()

