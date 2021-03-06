# coding=utf-8
from tkinter import *
from tkinter.filedialog import *
from tkinter import tix
from edition import *
from fichier import *
from menu import *
from parse_html import *
from aff_prop import *
from os import walk
from functools import partial
from tkinter.colorchooser import *
import tkinter.ttk as ttk
import glob
import os

class Main(object):

    def __init__(self, master):

        fenetre.geometry("{0}x{1}+0+0".format(fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()))

        self.gifsdict={}

        self.directory="./"
        self.fichier_ouvert=""
        self.html = fichier()
        self.html_menu = menu(self.directory)

        pre_parse_menu(self.html_menu)

        self.paned = PanedWindow(fenetre, orient=HORIZONTAL)

        self.prin_pan = Frame(self.paned, bg="blue")
        self.draw = Canvas(self.prin_pan, width=fenetre.winfo_screenwidth()*0.6, height=fenetre.winfo_screenheight(),
                           background="white",
                           scrollregion=(0, 0, "150i", "150i"))

        self.paned.pack(side=TOP, expand=Y, fill=BOTH)

        self.tree()
        self.principale()
        self.propriete()
        self.menu()



        self.paned.add(self.prop_pan)
        self.showdir

    def menu(self):
        self.menu = Menu(fenetre)
        self.filemenu = Menu(self.menu, tearoff=0)
        self.filemenu.add_command(label="Sauvegarder", command=self.sauvegarder)
        self.menu.add_cascade(label="Fichier", menu=self.filemenu)

        self.menumenu = Menu(self.menu, tearoff=0)
        self.menumenu.add_command(label="Editer le menu", command=partial(self.sel_menu))
        self.menumenu.add_command(label="Ajouter un lien", command=partial(ajouter_lien_menu, fenetre, (self.fichier_ouvert), self.directory, self.html_menu, self.draw))
        self.menumenu.add_command(label="Ajouter/mettre à jour le menu à la page", command=partial(ajout_menu_page, (self.fichier_ouvert), (self.html_menu), (self.draw), fenetre, self.html))
        self.menu.add_cascade(label="Menu", menu=self.menumenu)

        self.addmenu = Menu(self.menu, tearoff=0)
        self.addmenu.add_command(label="Ajouter un conteneur", command=partial(ajout_div, fenetre, (self.draw), (self.fichier_ouvert), (self.html), (self.html_menu)))
        self.addmenu.add_command(label="Ajouter une image", command=partial(ajout_image, fenetre, self.draw, self.fichier_ouvert, self.html, self.directory, self.gifsdict))
        self.addmenu.add_command(label="Ajouter du texte", command=partial(ajout_texte, fenetre, self.draw, self.fichier_ouvert, self.html, self.directory, self.prin_pan))
        self.menu.add_cascade(label="Ajouter", menu=self.addmenu)

        fenetre.config(menu=self.menu)

    def sauvegarder(self):
        if self.fichier_ouvert != "":
            nouveau_code = ""
            nouveau_code_retour_vide = self.html.ret_html() + "</body>\n</html>"
            nouveau_code_retour_vide_tab = nouveau_code_retour_vide.split("\n")
            for line in nouveau_code_retour_vide_tab:
                if line != "":
                    nouveau_code = nouveau_code + line + "\n"
            codehtml = open(self.fichier_ouvert, "w")
            codehtml.write(nouveau_code)
            codehtml.close()
        codemenu = open("menu.ew", "w")
        codemenu.write(self.html_menu.ret_menu())
        codemenu.close()

    def sel_fich(self, fichier):
        self.fichier_ouvert=fichier
        parse(fichier, (self.draw), fenetre, self.html, self.gifsdict)
        self.addmenu.entryconfigure(0, command=partial(ajout_div, fenetre, (self.draw), (self.fichier_ouvert), (self.html), (self.html_menu)))
        self.addmenu.entryconfigure(1, command=partial(ajout_image, fenetre, self.draw, self.fichier_ouvert, self.html, self.directory, self.gifsdict))
        self.addmenu.entryconfigure(2, command=partial(ajout_texte, fenetre, self.draw, self.fichier_ouvert, self.html, self.directory, self.prin_pan))
        self.menumenu.entryconfigure(1, command=partial(ajouter_lien_menu, fenetre, (self.fichier_ouvert), self.directory, self.html_menu, self.draw))
        self.menumenu.entryconfigure(2, command=partial(ajout_menu_page, (self.fichier_ouvert), (self.html_menu), (self.draw), fenetre, self.html))

    def sel_menu(self):
        parse_menu(self.html_menu, (self.draw), fenetre)
        self.fichier_ouvert = "menu.ew"
        self.addmenu.entryconfigure(0, command=partial(ajout_div, fenetre, (self.draw), (self.fichier_ouvert), (self.html), (self.html_menu)))
        self.addmenu.entryconfigure(1, command=partial(ajout_image, fenetre, self.draw, self.fichier_ouvert, self.html, self.directory, self.gifsdict))
        self.addmenu.entryconfigure(2, command=partial(ajout_texte, fenetre, self.draw, self.fichier_ouvert, self.html, self.directory, self.prin_pan))
        self.menumenu.entryconfigure(1, command=partial(ajouter_lien_menu, fenetre, (self.fichier_ouvert), self.directory, self.html_menu, self.draw))
        self.menumenu.entryconfigure(2, command=partial(ajout_menu_page, (self.fichier_ouvert), (self.html_menu), (self.draw), fenetre, self.html))

    def sel_dossier(self):
        self.directory = filedialog.askdirectory()
        self.showdir()
        self.html_menu = menu(self.directory)

    def tree(self):
        self.arbor = Frame(self.paned, bg="white", borderwidth=2, relief=GROOVE)
        self.arbor.pack(side=LEFT, padx=5, pady=5)

        Button(self.arbor, text="Selectionner un dossier", command=partial(self.sel_dossier)).pack()


        self.paned.add(self.arbor, width=fenetre.winfo_screenwidth()*0.2)

        self.frame_liste_fichier = LabelFrame(self.arbor, text="Listes des fichiers", relief=RIDGE)

        for x in os.listdir("./"):
            if x.endswith(".html"):
                but = Button(self.frame_liste_fichier, text=x, bg="yellow")
                but.configure(command=partial(self.sel_fich, "./"+x))

                x = self.html.ret_html()
                but.pack()

        self.ajout = Button(self.arbor, text="Créer une nouvelle page", command=partial(self.nom_fichier)).pack(side=BOTTOM)

        self.frame_liste_fichier.pack()

    #permet de savoir sur quel element on est
    def mouseEnter(self, event):
        self.draw.itemconfig(CURRENT, fill="red")

    #reset de l'etat de l'element
    def mouseLeave(self, event):
        self.draw.itemconfig(CURRENT, fill="blue")

    #permet de savoit les clicks
    def mouseDown(self, event):


        #try sur clic dans fenetre pour savoir si clic sur un div par exemple
        #try:
        afficher(self.prop_pan, self.draw, fenetre, self.draw, self.html, self.html_menu, self.directory, self.fichier_ouvert, self.gifsdict)
        #except:
        #    print("error")

        self.lastx = event.x
        self.lasty = event.y

    #permet de capturer les mouvement de la souris
    def mouseMove(self, event):
        #permet de savoir sur qu'elle element on est
        tag = self.draw.gettags(CURRENT)[0]
        res = re.search("menu_lien", tag)
        res2 = re.search("menu_bar", tag)
        if res == None and res2 == None:
            #permet d'obtenir les coordonnées du draw
            coor = self.draw.coords(CURRENT)
            self.draw.move(CURRENT, event.x - self.lastx, event.y - self.lasty)
            self.lastx = event.x
            self.lasty = event.y
            afficher(self.prop_pan, self.draw, fenetre, self.draw, self.html, self.html_menu, self.directory, self.fichier_ouvert, self.gifsdict)

    def principale(self):
        #self.paned.add(Label(self.paned, text='Main', background='red', anchor=CENTER), width=fenetre.winfo_screenwidth()*0.6)

        self.paned.add(self.prin_pan, width=fenetre.winfo_screenwidth()*0.6)


        self.draw.scrollY = Scrollbar(self.prin_pan, orient=VERTICAL)

        self.draw['yscrollcommand'] = self.draw.scrollY.set
        self.draw.scrollY['command'] = self.draw.yview

        self.draw.tag_bind(test, "<Any-Enter>", self.mouseEnter)
        self.draw.tag_bind(test, "<Any-Leave>", self.mouseLeave)

        Widget.bind(self.draw, "<1>", self.mouseDown)
        Widget.bind(self.draw, "<B1-Motion>", self.mouseMove)

        self.draw.scrollY.pack(side=RIGHT, fill=Y)
        self.draw.pack(side=LEFT)

    def propriete(self):
        self.prop_pan = Frame(self.paned)

    def showdir(self):

        for widget in self.frame_liste_fichier.winfo_children():
            widget.destroy()

        for x in os.listdir(self.directory):
            if x.endswith(".html"):
                but = Button(self.frame_liste_fichier, text=x, bg="yellow")
                but.configure(command=partial(self.sel_fich, self.directory+"/"+x))
                but.pack()
        self.frame_liste_fichier.pack()

    def lire_fichier(self, fichier):
        for all in self.prop_pan.winfo_children():
            all.destroy()
        with open(fichier, 'r') as mon_fichier:
            txt = mon_fichier.read()
        Label(self.prop_pan, text=txt).pack(side=TOP, anchor=W)
        x = self.html.ret_html()
        self.fichier_ouvert=fichier
        self.addmenu.entryconfigure(1, command=partial(ajout_div, fenetre, (self.draw), (self.fichier_ouvert), (self.html)))

    def nom_fichier(self):
        div = Toplevel(fenetre)
        frame = Frame(div)
        frame.pack()
        L1 = Label(frame, text="Nom de la page")
        L1.pack( side = LEFT)
        nom = Entry(frame, bd =5)
        nom.pack(side = RIGHT)
        Button(div, text="Créer", command=partial(self.generer_fichier, nom, div)).pack()

    def generer_fichier(self, nom, div):
        nom = nom.get()
        if nom != "":
            nom_page = nom
            nom = self.directory + "/" + nom + ".html"
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
            self.showdir()
        else:
            messagebox.showwarning("Error", "You need to insert an name")

fenetre = Tk()
app= Main(fenetre)
fenetre.mainloop()
