import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSlot

"""
Filename: lab93.py
Name: Jesus Gomez
Partner: Jonathan Quintero
Date: 2/26/19
Course: CST205 Multimedia Design and Programming
Description: Makes two buttons and makes them able to be pressed 
"""

#This code creates and sets two button that both have their own results if you press one of them

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout()

        self.my_btn = QPushButton("Button 1", self)
        self.my_lbl = QLabel('Button not clicked')
        self.my_btn.clicked.connect(self.on_click)
        vbox.addWidget(self.my_btn)
        vbox.addWidget(self.my_lbl)

        self.my_btn1 = QPushButton("Button 2", self)
        self.my_lbl1 = QLabel("Button not clicked")
        self.my_btn1.clicked.connect(self.on_click1)
        vbox.addWidget(self.my_btn1)
        vbox.addWidget(self.my_lbl1)

        self.setLayout(vbox)

    @pyqtSlot()
    def on_click(self):
        self.my_lbl.setText('Button clicked')
        print('Clicked 1')
        print("\033[1;32;40m Bright Green  \n") #This displays the "Button clicked" and makes the text bright green
        
    def on_click1(self):
        self.my_lbl1.setText("Button 2 clicked")
        print("Clicked 2")
        print("\033[0;35;47m Magenta") #This displays the "Button 2 Clicked" and makes the text negated Magenta
app = QApplication(sys.argv)
main_win = MainWindow()
main_win.show()
sys.exit(app.exec_())
