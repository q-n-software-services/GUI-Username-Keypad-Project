# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import time


start_time = time.time()
pressed = False
count = 0
t=0
t1=0
p=0
p1=0
value = 0.0
prev_value = 0.0
class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 500, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for components
    def UiComponents(self):
        global value
        global prev_value

        vbox = QVBoxLayout()

        self.btn1 = QPushButton("click me", self)
        self.btn1.setText("Click Me")
        self.btn1.setGeometry(200, 200, 200, 200)
        vbox.addWidget(self.btn1)

        # self.btn1.clicked.connect(self.pressed)
        self.btn1.clicked.connect(self.released)

        self.label = QLabel("Here is the value", self)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def pressed(event):
        global pressed
        global p
        pressed = True
        p = time.time() - start_time
        # print("button pushed at", t)

    def released(event):
        global pressed
        global p
        pressed = False
        p1 = time.time() - start_time
        # print("button released at", t1)
        print("button held down for", p1 - p, "seconds")


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
