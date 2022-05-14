from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def_init_(self):
        super(UI, self)._init_()

#load the ui file in the game
        uic.loadUi("game.ui", self)

#Define our ui Widgets
        self.button1 = self.findChild(QPushButton,"push_1")
        self.button1 = self.findChild(QPushButton,"push_2")
        self.button1 = self.findChild(QPushButton,"push_3")
        self.button1 = self.findChild(QPushButton,"push_4")
        self.button1 = self.findChild(QPushButton,"push_5")
        self.button1 = self.findChild(QPushButton,"push_6")
        self.button1 = self.findChild(QPushButton,"push_7")
        self.button1 = self.findChild(QPushButton,"push_8")
        self.button1 = self.findChild(QPushButton,"push_9")
        self.button1 = self.findChild(QPushButton,"push_10")
        self.button1 = self.findChild(QPushButton,"push_11")
        self.button1 = self.findChild(QPushButton,"push_12")
        self.button1 = self.findChild(QPushButton,"push_13")
        self.button1 = self.findChild(QPushButton,"push_14")
        self.button1 = self.findChild(QPushButton,"push_15")
        self.button1 = self.findChild(QPushButton,"push_16")
        self.button1 = self.findChild(QPushButton,"push_17")
        self.button1 = self.findChild(QPushButton,"push_18")
        self.button1 = self.findChild(QPushButton,"push_19")
        self.button1 = self.findChild(QPushButton,"push_20")
        self.button1 = self.findChild(QPushButton,"push_21")
        self.button1 = self.findChild(QPushButton,"push_22")
        self.button1 = self.findChild(QPushButton,"push_23")
        self.button1 = self.findChild(QPushButton,"push_24")
        self.button1 = self.findChild(QPushButton,"push_25")
        self.button1 = self.findChild(QPushButton,"push_26")
        self.button1 = self.findChild(QPushButton,"push_27")
        self.button1 = self.findChild(QPushButton,"restart")
        self.lable1 = self.findChild(QLabel, "lable1")
        
