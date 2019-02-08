import os 

class menu(object):

    def __init__(self):
        directory = "./"
        existe = False
        self.menu=""

        for x in os.listdir(directory):
            print(x)
            if x == "menu.ew":
                existe = True

        if existe == False:
            fichier_menu = open("menu.ew", "w")
            fichier_menu.close()

    def ecrire(self, html):
        self.menu += html

    def remplacer(self, html):
        self.html = html

    def ret_menu(self):
        return self.menu