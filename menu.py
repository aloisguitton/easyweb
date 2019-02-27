import os
from tkinter import *
from edition import *
from selcolor import *
from functools import partial

class menu(object):

    def __init__(self, directory):

        existe = False
        self.menu=""

        for x in os.listdir(directory):
            if x == "menu.ew":
                existe = True

        if existe == False:
            fichier=directory+"/menu.ew"
            fichier_menu = open(fichier, "w")
            html_val = """<div id=\"menu_bar_ew\" style=\"width:100%;background:grey;height:5%;position:fixed;top:0%;left:0%\"></div>
            <ul id=\"navigation_menu_bar_ew\" style=\"z-index: 3;height: 5%;position: absolute;margin-top: 0;margin-bottom: 0;right: 0;\"></ul>"""
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

def ajouter_lien_menu(fenetre, fichier, chemin, menu_html, draw):
    if fichier == "menu.ew":
        # color = selcolor()

        div = Toplevel(fenetre)
        liste = []
        frametxt= Frame(div)
        frametxt.pack()
        L1 = Label(frametxt, text="Texte : ").pack( side = LEFT)
        textelab = Entry(frametxt, bd =5)
        textelab.pack(side = RIGHT)

        framewlien= Frame(div)
        framewlien.pack()
        L1 = Label(framewlien, text="Lien : ").pack( side = LEFT)


        for x in os.listdir(chemin):
            if x.endswith(".html"):
                liste.append(x)

        combo = ttk.Combobox(framewlien, value=liste)
        # Button(div, text='Couleur au survol', command=partial(color.getColor)).pack()

        combo.pack()

        Button(div, text="Ajouter", command=partial(ajout_lien, textelab, combo, div, menu_html, chemin, draw, fenetre)).pack()

        div.mainloop()
    else:
        messagebox.showwarning("Error", "Vous devez selectionner le menu")
