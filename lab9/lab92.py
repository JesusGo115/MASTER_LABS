import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
"""
Filename: lab9_task3.py
Name: Jesus Gomez
Partner: Jonathan Quintero 
Date: 2/26/19
Course: CST205 Multimedia Design and Programming
Description: Program displays a window with an image 
"""
#This code changes the title of the window and displays an image on the window

#Extending the QWidget class
class Example(QWidget):
    def __init__(self):
        super().__init__()
        #Window title
        self.setWindowTitle('Jesus "Chuy" Gomez and Jonathan Josue Quintero Ramos')
        self.label = QLabel(self)
        #Pixmap module use to access to picture
        pixmap = QPixmap('bitCoin.jpeg')
        pixmap = pixmap.scaledToWidth(1000)
        self.label.setPixmap(pixmap)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        #Set the dimensions of the window
        self.setGeometry(100,100,600,400)
        self.show()

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())

