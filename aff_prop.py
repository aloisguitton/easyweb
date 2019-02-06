from tkinter import *

def afficher(prop_frame, obj, fenetre):
    for all in prop_frame.winfo_children():
            all.destroy()
    Label(prop_frame, text=obj.gettags(CURRENT)[0]).pack()

    coor = obj.coords(CURRENT)
    
    framemt = Frame(prop_frame)
    framemt.pack()
    v = StringVar()
    Label(framemt, text="Margin top: ").pack(side=LEFT)
    e = Entry(framemt, textvariable=v).pack(side=LEFT)
    v.set(float(coor[1])/fenetre.winfo_screenheight()*100)
    Label(framemt, text="%").pack(side=LEFT)

    framewid = Frame(prop_frame)
    framewid.pack()
    v = StringVar()
    Label(framewid, text="Width: ").pack(side=LEFT)
    e = Entry(framewid, textvariable=v).pack(side=LEFT)
    v.set((float(coor[2])-float(coor[0]))/fenetre.winfo_screenwidth()*(100/60)*100)
    Label(framewid, text="%").pack(side=LEFT)

    framehei = Frame(prop_frame)
    framehei.pack()
    v = StringVar()
    Label(framehei, text="Height: ").pack(side=LEFT)
    e = Entry(framehei, textvariable=v).pack(side=LEFT)
    v.set((float(coor[3])-float(coor[1]))/fenetre.winfo_screenheight()*100)
    Label(framehei, text="%").pack(side=LEFT)