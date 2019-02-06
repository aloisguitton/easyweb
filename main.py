from tkinter import *
from tkinter.filedialog import *
from tkinter import tix
from edition import *
from fichier import *
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

        self.fichier_ouvert=""
        self.html = fichier()
        
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
        self.filemenu.add_command(label="Nouvelle page")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Sauvegarder", command=self.sauvegarder)
        self.menu.add_cascade(label="Fichier", menu=self.filemenu)

        self.addmenu = Menu(self.menu, tearoff=0)
        self.addmenu.add_command(label="Ajouter un conteneur", command=partial(ajout_div, fenetre, (self.draw), (self.fichier_ouvert), (self.html)))
        self.menu.add_cascade(label="Ajouter", menu=self.addmenu)
        fenetre.config(menu=self.menu)  
  
    def sauvegarder(self):
        nouveau_code = self.html.ret_html()
        codehtml = open(self.fichier_ouvert, "w")
        codehtml.write(nouveau_code)
        codehtml.close()

    def tree(self):
        self.arbor = Frame(self.paned, bg="white", borderwidth=2, relief=GROOVE)
        self.arbor.pack(side=LEFT, padx=5, pady=5)

        label = Label(self.arbor, text="Explorer", bg="yellow")
        label.pack()

        self.paned.add(self.arbor, width=fenetre.winfo_screenwidth()*0.2)

        self.frame_liste_fichier = LabelFrame(self.arbor, text="Listes des fichiers", relief=RIDGE)
        dirlist=tix.DirList(self.arbor, command=self.showdir)
        dirlist.pack(fill="x")

        for x in os.listdir("./"):
            if x.endswith(".html") or x.endswith(".txt"):
                but = Button(self.frame_liste_fichier, text=x, bg="yellow")
                but.configure(command=partial(parse, "./"+x, (self.draw), fenetre, self.html))
                self.fichier_ouvert="./"+x
                x = self.html.ret_html()
                but.pack()
        
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
        afficher(self.prop_pan, self.draw, fenetre)
        #except:
        #    print("error")
        
        self.lastx = event.x
        self.lasty = event.y

    #permet de capturer les mouvement de la souris 
    def mouseMove(self, event):
        #permet d'obtenir les coordonnées du draw
        coor = self.draw.coords(CURRENT)
        self.draw.move(CURRENT, event.x - self.lastx, event.y - self.lasty)
        self.lastx = event.x
        self.lasty = event.y

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
        self.prop_pan = Frame(self.paned, bg="red")

    def showdir(self, directory):

        for widget in self.frame_liste_fichier.winfo_children():
            widget.destroy()

        for x in os.listdir(directory):
            if x.endswith(".html") or x.endswith(".txt"):
                but = Button(self.frame_liste_fichier, text=x, bg="yellow")
                but.configure(command=partial(parse, directory+"/"+x, (self.draw), fenetre, self.html))
                self.fichier_ouvert=directory+"/"+x
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

fenetre = tix.Tk()
app= Main(fenetre)
fenetre.mainloop()
