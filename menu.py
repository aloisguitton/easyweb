import os
from tkinter import *
from edition import *
from functools import partial

class menu(object):

    def __init__(self, directory):

        print("ici")
        existe = False
        self.menu=""

        for x in os.listdir(directory):
            if x == "menu.ew":
                existe = True

        if existe == False:
            fichier=directory+"/menu.ew"
            print(fichier)
            fichier_menu = open(fichier, "w")
            html_val = """<div id=\"menu_bar_ew\" style=\"width:100%;background:grey;height:5%;position:fixed;top:0%;left:0%\"></div>
<ul id=\"navigation\">
</ul>"""
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

def ajouter_lien_menu(fenetre, fichier, chemin, menu_html):
    if fichier == "menu.ew":
        i = 0;
        div = Toplevel(fenetre)

        frametxt= Frame(div)
        frametxt.pack()
        L1 = Label(frametxt, text="Texte : ").pack( side = LEFT)
        textelab = Entry(frametxt, bd =5)
        textelab.pack(side = RIGHT)

        framewlien= Frame(div)
        framewlien.pack()
        L1 = Label(framewlien, text="Lien : ").pack( side = LEFT)
        combo = ttk.Combobox(framewlien)
        for x in os.listdir(chemin):
            if x.endswith(".html"):
                combo.insert(i, x)
                i+1

        combo.pack()

        Button(div, text="Ajouter", command=partial(ajout_lien, textelab, combo, div, menu_html, chemin)).pack()

        div.mainloop()
    else:
        messagebox.showwarning("Error", "Vous devez selectionner le menu")
