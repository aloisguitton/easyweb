import os
from tkinter import *
from functools import partial
from tkinter.filedialog import *

def nom_fichier(fenetre):
    div = Toplevel(fenetre)
    frame = Frame(div)
    frame.pack()
    L1 = Label(frame, text="Nom de la page")
    L1.pack( side = LEFT)
    nom = Entry(frame, bd =5)
    nom.pack(side = RIGHT)
    Button(div, text="Créer", command=partial(generer_fichier, nom, div)).pack()

def generer_fichier(nom, div):
    nom = nom.get()
    nom_page = nom
    if nom != "":
        nom = nom + ".html"
        html = """<!DOCTYPE html>
                <html>
                <head>
                    <meta charset="utf-8" />
                    <title>{0}</title>
                </head>

                <body>
                </body>
                </html>
                """.format(nom_page)
        codehtml = open(nom, "w")
        codehtml.write(html)
        codehtml.close()
        div.destroy()
    else:
        messagebox.showwarning("Error", "You need to insert an name")
    