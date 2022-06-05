import cv2
from PIL import Image
from PIL.ImageDraw import ImageDraw
from PIL.ImageFont import ImageFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog, QTextBrowser
from PyQt5 import uic, QtGui
from PyQt5.QtGui import QPixmap
import sys
import os
import model
import matplotlib.pyplot as plt

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("image.ui", self)

        # Define our widgets
        self.button = self.findChild(QPushButton, "pushButton")
        self.button2 = self.findChild(QPushButton, "pushButton_2")
        self.label = self.findChild(QLabel, "label")
        self.label2 = self.findChild(QLabel, "label_2")
        self.textBrowser = self.findChild(QTextBrowser, "textBrowser")

        # Click The Dropdown Box
        self.button.clicked.connect(self.clicker)
        self.button2.clicked.connect(self.clicker2)

        # Show The App
        self.show()

    def clicker(self):
        document_path = os.path.expanduser('~\Pictures')
        fname = QFileDialog.getOpenFileName(self, "Open File", document_path,
                                            "All Files (*);;PNG Files (*.png);;Jpg Files (*.jpg)")
        # Open The Image
        if fname:
            self.pixmap = QPixmap(fname[0])
            self.flnm = fname[0]
            # Add Pic to label
            self.label.setPixmap(self.pixmap)
            self.label.setScaledContents(True)

    def clicker2(self):
        letter, image = model.get_letters(self.flnm)
        word = model.get_word(letter)
        document_path2 = os.path.expanduser('~\Pictures')
        filename = document_path2 + 'recognizedImage.jpg'
        self.pixmap = QPixmap(filename)
        self.label2.setPixmap(self.pixmap)
        self.label2.setScaledContents(True)
        self.textBrowser.setText(word)


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
