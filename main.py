import sys
import os
from tkinter import Button
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Célia Cachos')
        self.setWindowIcon(QIcon('imagens/logo.png'))
        self.setFixedSize(QSize(1000,500))


        btn = QPushButton("Button") #create the btn
        btn.setFixedSize(QSize(100,100)) #changes btn size
        btn.setCheckable(True) #makes btn clickable
        btn.clicked.connect(self.the_button_was_clicked) #action when clicked
        btn.clicked.connect(self.the_button_was_toggled)
        self.setCentralWidget(btn) #Shows btn

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self, checked):
        print("Checked?", checked)

app = QApplication(sys.argv)

main_window = MainWindow() #Defines the main_window
main_window.show() #Show the main_window

app.exec() #Executes in loop the application


