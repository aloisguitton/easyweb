from tkinter import *
from functools import partial
from edition import *

def afficher(prop_frame, obj, fenetre, draw, html, menu):

    type = obj.type(CURRENT)

    for all in prop_frame.winfo_children():
            all.destroy()

    tag = obj.gettags(CURRENT)[0]


    Label(prop_frame, text=tag).pack()

    if type == "rectangle":
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
        Button(prop_frame, text='Select Color', command=partial(color.getColor)).pack()

        Button(prop_frame, text="valider", command=partial(edit, w, h, t, l, tag, draw, color, fenetre, html, menu)).pack()
