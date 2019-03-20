from tkinter.filedialog import *

class image(object):

    def __init__(self):
        self.image=""


    def set_image(self, fichier):
        self.image = fichier
        print(self.image)

    def ret_image(self):
        return self.image
