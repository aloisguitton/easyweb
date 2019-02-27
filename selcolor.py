from tkinter.colorchooser import *

class selcolor(object):
    def __init__(self):
        self.color = None

    def getColor(self):
        self.color = askcolor(color="#6A9662", title = "Choisir une couleur")[1]

    def ret_color(self):
        return (self.color)
