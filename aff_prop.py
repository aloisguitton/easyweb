from tkinter import *
from functools import partial
from edition import *
import tkinter.ttk as ttk
from menu import *

def afficher(prop_frame, obj, fenetre, draw, html, menu, chemin, fichier, gifsdict):

    type = obj.type(CURRENT)

    for all in prop_frame.winfo_children():
            all.destroy()

    tag = obj.gettags(CURRENT)[0]

    Label(prop_frame, text=tag).pack()

    if type == "rectangle":
        item = re.findall("<div id=\"{0}\"(.*)".format(tag), html.ret_html())[0]
        couleur = re.findall("background:(.*);hei", item)[0]

        res = re.search("menu_bar_", tag)
        res2 = re.search("menu.ew", fichier)

        print(res2)

        if res and res2 == None:
            Label(prop_frame, text="Vous devez editer ce conteneur \n dans l'onglet \"editer le menu\"").pack()
        else:
            coor = obj.coords(CURRENT)

            framemt = Frame(prop_frame)
            framemt.pack()
            t = StringVar()
            Label(framemt, text="Margin top: ").pack(side=LEFT)
            Entry(framemt, textvariable=t).pack(side=LEFT)
            t.set(int(int(coor[1])/fenetre.winfo_screenheight()*100))
            Label(framemt, text="%").pack(side=LEFT)

            frameml = Frame(prop_frame)
            frameml.pack()
            l = StringVar()
            Label(frameml, text="Margin left: ").pack(side=LEFT)
            Entry(frameml, textvariable=l).pack(side=LEFT)
            l.set(int(int(coor[0])/fenetre.winfo_screenwidth()*(100/60)*100))
            Label(frameml, text="%").pack(side=LEFT)

            framewid = Frame(prop_frame)
            framewid.pack()
            w = StringVar()
            Label(framewid, text="Width: ").pack(side=LEFT)
            Entry(framewid, textvariable=w).pack(side=LEFT)
            w.set(int((int(coor[2])-int(coor[0]))/fenetre.winfo_screenwidth()*(100/60)*100))
            Label(framewid, text="%").pack(side=LEFT)

            framehei = Frame(prop_frame)
            framehei.pack()
            h = StringVar()
            Label(framehei, text="Height: ").pack(side=LEFT)
            Entry(framehei, textvariable=h).pack(side=LEFT)
            h.set(int((int(coor[3])-int(coor[1]))/fenetre.winfo_screenheight()*100))
            Label(framehei, text="%").pack(side=LEFT)

            color = selcolor()
            Button(prop_frame, text='Selectionner une couleur', command=partial(color.getColor)).pack()

            Button(prop_frame, text="Valider", command=partial(edit, w, h, t, l, tag, draw, color, fenetre, html, menu, couleur)).pack()
            si_menu = re.search("menu.ew", fichier)
            if si_menu:
                Button(prop_frame, text="Supprimer", command=partial(supprimer_div, tag, draw, menu, 0)).pack()
            else:
                Button(prop_frame, text="Supprimer", command=partial(supprimer_div, tag, draw, html, 1)).pack()
    elif type == "text":
        res = re.search("menu_lien_", tag)
        res2 = re.search("menu.ew", fichier)
        if res and res2 == None:
            Label(prop_frame, text="Vous devez editer ce lien \n dans l'onglet \"editer le menu\"").pack()
        elif res:
            framenom = Frame(prop_frame)
            framenom.pack()
            nom = StringVar()
            Label(framenom, text="Texte du lien").pack(side=LEFT)
            Entry(framenom, textvariable=nom).pack(side=LEFT)
            nom.set(tag[10:])
            ancien_tag = tag[10:]

            framelien = Frame(prop_frame)
            framelien.pack()
            Label(framelien, text="Lien").pack(side=LEFT)
            liste = []
            for x in os.listdir(chemin):
                if x.endswith(".html"):
                    liste.append(x)

            combo = ttk.Combobox(framelien, value=liste)
            combo.pack(side=LEFT)

            Button(prop_frame, text="Mettre à jour le lien", command=partial(mise_jour_lien, nom, combo, menu, ancien_tag, draw, fenetre)).pack()

    elif type == "image":

        coor = obj.coords(CURRENT)
        print(coor[0])
        img_html = re.findall('<img id=\"{}\"(.*)>'.format(tag), html.ret_html())[0]

        ma_top = re.findall('height:(.*)%;p', img_html)[0]
        ma_top = int(((-(int(ma_top)/100)*fenetre.winfo_screenheight())/2 + coor[1])/fenetre.winfo_screenheight()*100)

        ma_left = re.findall('width:(.*)%;h', img_html)[0]
        ma_left = int(-((int(ma_left)/100*fenetre.winfo_screenwidth()*0.6)/2-coor[0])/(fenetre.winfo_screenwidth()*0.6)*100)

        img = re.findall('src="(.*)"', img_html)[0]
        framemt = Frame(prop_frame)
        framemt.pack()
        t = StringVar()
        Label(framemt, text="Margin top: ").pack(side=LEFT)
        Entry(framemt, textvariable=t).pack(side=LEFT)
        t.set(ma_top)
        Label(framemt, text="%").pack(side=LEFT)

        frameml = Frame(prop_frame)
        frameml.pack()
        l = StringVar()
        Label(frameml, text="Margin left: ").pack(side=LEFT)
        Entry(frameml, textvariable=l).pack(side=LEFT)
        l.set(ma_left)
        Label(frameml, text="%").pack(side=LEFT)

        framewid = Frame(prop_frame)
        framewid.pack()
        w = StringVar()
        Label(framewid, text="Width: ").pack(side=LEFT)
        Entry(framewid, textvariable=w).pack(side=LEFT)
        w.set(re.findall('width:(.*)%;h', img_html)[0])
        Label(framewid, text="%").pack(side=LEFT)

        framehei = Frame(prop_frame)
        framehei.pack()
        h = StringVar()
        Label(framehei, text="Height: ").pack(side=LEFT)
        Entry(framehei, textvariable=h).pack(side=LEFT)
        h.set(re.findall('height:(.*)%;p', img_html)[0])
        Label(framehei, text="%").pack(side=LEFT)


        Button(prop_frame, text="Valider", command=partial(edit_image, w, h, t, l, tag, draw, fenetre, html, menu, img, gifsdict)).pack()

        Button(prop_frame, text="Supprimer", command=partial(supprimer_image, tag, draw, html)).pack()



    else:
        coor = obj.coords(CURRENT)
        print(type)
