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
            html_val = "<div id=\"menu_bar_ew\" style=\"width:100%;background:grey;height:5%;position:fixed;top:0%;left:0%\"></div>\n"
            fichier_menu.write(html_val)
            fichier_menu.close()


    def ecrire(self, html):
        self.menu += html

    def reset(self):
        self.menu = ""

    def remplacer(self, html):
        self.menu = html

    def ret_menu(self):
        return self.menu
