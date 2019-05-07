from tkinter import *
from fichier import *
from image import *
from random import *
from selcolor import *
import PIL.Image
import PIL.ImageTk
from resizeimage import resizeimage
from os.path import basename
from shutil import copyfile
from tkinter.filedialog import *
from tkinter import ttk
from functools import partial
from tkinter import messagebox
import re

result=None

def ajout_div_fun(w, h, color, div, draw, html, fenetre, top, tag, left, fichier):
    color_value = color.ret_color()
    if top.get() == "":
        top = 0
    else:
        top = top.get()

    if left.get() == "":
        left = 0
    else:
        left = left.get()
    if color_value == None:
        color_value = "#FFFFFF"
    if tag.get() != "":
        if w.get().isdigit():
            if float(w.get()) != 0:
                if h.get().isdigit():
                    if float(h.get()) != 0:
                        ajout_div_princ(div, draw, html, (w.get()), (h.get()), color_value, fenetre, top, (tag.get()), left, fichier)
                    else:
                        messagebox.showwarning("Error","Height can't be egal to 0")
                else:
                    messagebox.showwarning("Error", "You need to insert a integer")
            else:
                messagebox.showwarning("Error","Weight can't be egal to 0")
        else:
            messagebox.showwarning("Error", "You need to insert a integer")
    else:
        messagebox.showwarning("Error", "You need to insert an id")

def edit(w, h, top, left, tag, draw, color, fenetre, html, menu, couleur):
    color_value = color.ret_color()
    if top.get() == "":
        top = 0
    else:
        top = top.get()
    if left.get() == "":
        left = 0
    else:
        left = left.get()
    if color_value == None:
        color_value = couleur
    if tag != "":
        if w.get().isdigit():
            if float(w.get()) != 0:
                if h.get().isdigit():
                    if float(h.get()) != 0:
                        draw.delete(tag)
                        if tag != "menu_bar_ew":
                            edit_ajout_div_princ(draw, html, (w.get()), (h.get()), color_value, fenetre, top, tag, left)
                        else:
                            edit_ajout_menu(draw, menu, (w.get()), (h.get()), color_value, fenetre, top, tag, left)
                    else:
                        messagebox.showwarning("Error","Height can't be egal to 0")
                else:
                    messagebox.showwarning("Error", "You need to insert a integer")
            else:
                messagebox.showwarning("Error","Weight can't be egal to 0")
        else:
            messagebox.showwarning("Error", "You need to insert a integer")
    else:
        messagebox.showwarning("Error", "You need to insert an id")

def edit_image(w, h, top, left, tag, draw, fenetre, html, menu, img, gifsdict):
    if top.get() == "":
        top = 0
    else:
        top = top.get()
    if left.get() == "":
        left = 0
    else:
        left = left.get()
    if tag != "":
        if w.get().isdigit():
            if float(w.get()) != 0:
                if h.get().isdigit():
                    if float(h.get()) != 0:
                        draw.delete(tag)
                        edit_ajout_image_princ(draw, html, w.get(), h.get(), fenetre, top, tag, left, img, gifsdict)
                    else:
                        messagebox.showwarning("Error","Height can't be egal to 0")
                else:
                    messagebox.showwarning("Error", "You need to insert a integer")
            else:
                messagebox.showwarning("Error","Weight can't be egal to 0")
        else:
            messagebox.showwarning("Error", "You need to insert a integer")
    else:
        messagebox.showwarning("Error", "You need to insert an id")

def ajout_div(fenetre, draw, fichier, html, menu):
    color = selcolor()
    if fichier != "":
        if fichier == "menu.ew":
            messagebox.showwarning("Error", "Vous ne pouvez pas ajouter un conteneur au menu")
        else:
            div = Toplevel(fenetre)
            framewid = Frame(div)
            framewid.pack()
            L1 = Label(framewid, text="Largeur(%)")
            L1.pack( side = LEFT)
            widthlab = Entry(framewid, bd =5)
            widthlab.pack(side = RIGHT)

            framemt = Frame(div)
            framemt.pack()
            L1 = Label(framemt, text="Hauteur(%)  ")
            L1.pack( side = LEFT)
            heightlab = Entry(framemt, bd =5)
            heightlab.pack(side = RIGHT)

            frametop = Frame(div)
            frametop.pack()
            L1 = Label(frametop, text="Marge Top(%)  ")
            L1.pack( side = LEFT)
            toplab = Entry(frametop, bd =5)
            toplab.pack(side = RIGHT)

            frameleft = Frame(div)
            frameleft.pack()
            L1 = Label(frameleft, text="Marge Gauche(%)  ")
            L1.pack( side = LEFT)
            leftlab = Entry(frameleft, bd =5)
            leftlab.pack(side = RIGHT)

            frametag = Frame(div)
            frametag.pack()
            L1 = Label(frametag, text="ID (Doit être unique)")
            L1.pack( side = LEFT)
            taglab = Entry(frametag, bd =5)
            taglab.pack(side = RIGHT)

            Button(div, text='Couleur du conteneur', command=partial(color.getColor)).pack()


            Button(div, text="Valider", bg="Green", command=partial(ajout_div_fun, widthlab, heightlab, color, div, draw, html, fenetre, toplab, taglab, leftlab, fichier)).pack(side=BOTTOM)
            div.mainloop()
    else:
        messagebox.showwarning("Error", "You need to open a file")

def edit_ajout_menu(draw, menu, w, h, color, fenetre, top, tag, left):
    draw.create_rectangle(fenetre.winfo_screenwidth()*0.6*(float(left)/100), fenetre.winfo_screenheight()*(float(top)/100), fenetre.winfo_screenwidth()*0.6*(float(left)/100) + fenetre.winfo_screenwidth()*0.6*(float(w)/100), fenetre.winfo_screenheight()*(float(top)/100)+fenetre.winfo_screenheight()*(float(h)/100), fill=color, tags=tag)
    html_val = menu.ret_menu()
    avant = re.findall('<div id="{0}" style="(.*)">'.format(tag), html_val)[0]
    apres = "width:{0}%;background:{1};height:{2}%;position:absolute;top:{3}%;left:{4}%".format(w, color, h, top, left)
    html_val = html_val.replace(avant, apres)
    menu.remplacer(html_val)

def edit_ajout_div_princ(draw, html, w, h, color, fenetre, top, tag, left):
    draw.create_rectangle(fenetre.winfo_screenwidth()*0.6*(float(left)/100), fenetre.winfo_screenheight()*(float(top)/100), fenetre.winfo_screenwidth()*0.6*(float(left)/100) + fenetre.winfo_screenwidth()*0.6*(float(w)/100), fenetre.winfo_screenheight()*(float(top)/100)+fenetre.winfo_screenheight()*(float(h)/100), fill=color, tags=tag)
    html_val = html.ret_html()
    avant = re.findall('<div id="{0}" style="(.*)">'.format(tag), html_val)[0]
    apres = "width:{0}%;background:{1};height:{2}%;position:absolute;top:{3}%;left:{4}%".format(w, color, h, top, left)
    html_val = html_val.replace(avant, apres)
    html.remplacer(html_val)

def edit_ajout_image_princ(draw, html, w, h, fenetre, top, tag, left, img, gifsdict):
    print(img)
    nom = basename(img)
    nom_sans_ext = os.path.splitext(nom)[0]
    ext = os.path.splitext(nom)[1]

    imgfile = img

    largeur = fenetre.winfo_screenwidth()*0.6*int(w)/100
    hauteur = fenetre.winfo_screenheight()*int(h)/100
    photo = PIL.Image.open(imgfile)
    resolution = (int(largeur),int(hauteur))
    img = PIL.ImageTk.PhotoImage(photo.resize(resolution))
    gifsdict[imgfile] = img
    draw.create_image(fenetre.winfo_screenwidth()*0.6*(float(left)/100) + largeur/2, fenetre.winfo_screenheight()*(float(top)/100) + hauteur/2, image=img, tags=tag)
    ecrire_image(tag, w, h, top, left, imgfile, html)

def ajout_div_princ(div, draw, html, w, h, color, fenetre, top, tag, left, fichier):
    if fichier == "_menu_bar_ew":
        tag += "_menu_bar_ew"
    div.destroy()
    draw.create_rectangle(fenetre.winfo_screenwidth()*0.6*(float(left)/100), fenetre.winfo_screenheight()*(float(top)/100), fenetre.winfo_screenwidth()*0.6*(float(left)/100) + fenetre.winfo_screenwidth()*0.6*(float(w)/100), fenetre.winfo_screenheight()*(float(top)/100)+fenetre.winfo_screenheight()*(float(h)/100), fill=color, tags=tag)
    if fichier == "menu.ew":
        html_val = "<div id=\"{0}\" style=\"width:{1}%;background:{2};height:{3}%;position:fixed;top:{4}%;left:{5}%\"></div>\n".format(tag, w, color, h, top, left)
    else:
        html_val = "<div id=\"{0}\" style=\"width:{1}%;background:{2};height:{3}%;position:absolute;top:{4}%;left:{5}%\"></div>\n".format(tag, w, color, h, top, left)
    html.ecrire(html_val)

def ecrire_image(tag, w, h, top, left, img, html):
    html_val = "<img id=\"{0}\" style=\"width:{1}%;height:{2}%;position:absolute;top:{3}%;left:{4}%\" src=\"{5}\">\n".format(tag, w, h, top, left, img)
    html.ecrire(html_val)

def ajout_menu_page(fichier, menu, draw, fenetre, html):
    if fichier != "":
        if fichier != "menu.ew":

            html_html = html.ret_html()
            nouv_html = ""

            for line in html_html:
                nouv_html += line

            body = re.findall('<body>(.*)', nouv_html, re.MULTILINE | re.DOTALL)[0]
            body_split = body.split("\n")

            menu_nb = 0
            nouv_html = ""

            for line in body_split:
                res = re.search("menu_bar_ew", line)
                li = re.search("li", line)
                ul = re.search("ul", line)
                if res or li or ul:
                    res2 = re.search("</a>", line)
                    if res2:
                        texte = re.findall('\">(.*)</a>', line)[0]
                        tag = "menu_lien_" + texte
                        draw.delete(tag)
                    menu_nb += 1
                    item = re.findall('id=\"(.*)\" style', line)
                    draw.delete(item)
                else:
                    nouv_html = nouv_html + line + "\n"

            menu_html = menu.ret_menu()
            nouv_html += menu_html


            div_liste = re.findall('<div(.*)">', menu_html)
            a_liste = re.findall('<a(.*)</a>', menu_html)
            a_liste.reverse()

            html_val = html_html.replace(body, nouv_html)

            html.remplacer(html_val)

            for div in div_liste:
                l =  re.findall('left:(.*)%', div)[0]
                w = re.findall('width:(.*)%;b', div)[0]
                h = re.findall('height:(.*)%;p', div)[0]
                color = re.findall('background:(.*);h', div)[0]
                top = re.findall('top:(.*)%;l', div)[0]
                tag = re.findall('id="(.*)" st', div)[0]
                draw.create_rectangle(fenetre.winfo_screenwidth()*0.6*(float(l)/100), fenetre.winfo_screenheight()*(float(top)/100), fenetre.winfo_screenwidth()*0.6*(float(l)/100) + fenetre.winfo_screenwidth()*0.6*(float(w)/100), fenetre.winfo_screenheight()*(float(top)/100)+fenetre.winfo_screenheight()*(float(h)/100), fill=color, tags=tag)

            i=0

            for a in a_liste:
                i=i+1
                texte = re.findall('\">(.*)', a)[0]
                tag = "menu_lien_" + texte
                draw.create_text(fenetre.winfo_screenwidth()*0.6 - 75*i, fenetre.winfo_screenheight()*0.025, text=texte, tags=tag)

        else:
            messagebox.showwarning("Error", "Vous ne pouvez pas ajouter un menu à un menu")
    else:
        messagebox.showwarning("Error", "Vous devez selectionner un fichier")

def ajout_lien(texte, lien, div, menu_html, chemin, draw, fenetre):

    # fichier = chemin + "/menu.ew"
    # with open(fichier, 'r') as mon_fichier:
                # fichier_menu = mon_fichier.read()
    fichier_menu = menu_html.ret_menu()

    avant=re.findall('<ul(.*)</ul>', fichier_menu, re.MULTILINE | re.DOTALL)[0]

    # couleur_var = couleur.ret_color()

    if avant == " id=\"navigation_menu_bar_ew\" style=\"z-index: 3;height: 5%;position: absolute;margin-top: 0;margin-bottom: 0;right: 0;\">":
        apres=""" id=\"navigation_menu_bar_ew\" style=\"z-index: 3;height: 5%;position: absolute;margin-top: 0;margin-bottom: 0;right: 0;\">
        <li id=\"li_menu_bar_ew\" style=\"display: inline-block;margin-top: 2%\">
            <a href="{0}" id=\"li_menu_bar_ew\" style=\"text-decoration: none;margin-right: 10px;margin-left: 10px;\">{1}</a>
        </li>""".format(lien.get(), texte.get())
    else:
        avant=re.findall('</l(.*)ul>', fichier_menu)[0]
        apres="""i>
        <li id=\"li_menu_bar_ew\" style=\"display: inline-block;margin-top: 2%\">
            <a href="{0}" id=\"li_menu_bar_ew\" style=\"text-decoration: none;margin-right: 10px;margin-left: 10px;\">{1}</a>
        </li></""".format(lien.get(), texte.get())

    html_val = fichier_menu.replace(avant, apres)

    ajout_lien_menu_div(draw, html_val, fenetre)

    menu_html.remplacer(html_val)

    div.destroy()

def mise_jour_lien(nom, lien, menu, ancien_tag, draw, fenetre):
    menu_txt = menu.ret_menu()
    reg = "<a (.*)" + ancien_tag + "</a>"
    avant = re.findall(reg, menu_txt)[0] + ancien_tag
    apres = "href=\"{0}\" id=\"li_menu_bar_ew\" style=\"text-decoration: none;margin-right: 10px;margin-left: 10px;\">{1}".format(lien.get(), nom.get())
    nouv_menu = menu_txt.replace(avant, apres)
    ancien_tag = "menu_lien_" + ancien_tag
    draw.delete(ancien_tag)
    ajout_lien_menu_div(draw, nouv_menu, fenetre)
    menu.remplacer(nouv_menu)

def ajout_lien_menu_div(draw, html, fenetre):

    texte_lien = re.findall('10px;">(.*)</a>', html)

    texte_lien.reverse()
    i=0

    for texte in texte_lien:
        i=i+1
        tag = "menu_lien_" + texte
        draw.delete(tag)
        # draw.create_text(fenetre.winfo_screenwidth()*0.6 - 75*i, fenetre.winfo_screenheight()*0.025, text=texte, activefill=couleur, tags=tag)
        draw.create_text(fenetre.winfo_screenwidth()*0.6 - 75*i, fenetre.winfo_screenheight()*0.025, text=texte, tags=tag)

def ajout_texte(fenetre, draw, fichier, html, directory, prin_pan):
    color = selcolor()
    if fichier != "":
        if fichier == "menu.ew":
            messagebox.showwarning("Error", "Vous ne pouvez pas ajouter un texte au menu")
        else:
            div = Toplevel(fenetre)
            framewid = Frame(div)
            framewid.pack()
            L1 = Label(framewid, text="Largeur(%)")
            L1.pack( side = LEFT)
            widthlab = Entry(framewid, bd =5)
            widthlab.pack(side = RIGHT)

            frametop = Frame(div)
            frametop.pack()
            L1 = Label(frametop, text="Marge Top(%)  ")
            L1.pack( side = LEFT)
            toplab = Entry(frametop, bd =5)
            toplab.pack(side = RIGHT)

            frameleft = Frame(div)
            frameleft.pack()
            L1 = Label(frameleft, text="Marge Gauche(%)  ")
            L1.pack( side = LEFT)
            leftlab = Entry(frameleft, bd =5)
            leftlab.pack(side = RIGHT)

            frametag = Frame(div)
            frametag.pack()
            L1 = Label(frametag, text="ID (Doit être unique)")
            L1.pack( side = LEFT)
            taglab = Entry(frametag, bd =5)
            taglab.pack(side = RIGHT)

            framemt = Frame(div)
            framemt.pack()
            L1 = Label(framemt, text="Texte :")
            L1.pack()
            textelab = Text(framemt, bd =5)
            textelab.pack()

            Button(div, text='Couleur du fond', command=partial(color.getColor)).pack()


            Button(div, text="Valider", command=partial(ajout_texte_fun, widthlab, textelab, color, div, draw, html, fenetre, toplab, taglab, leftlab, fichier)).pack(side=BOTTOM)
            div.mainloop()
    else:
        messagebox.showwarning("Error", "You need to open a file")

def ajout_texte_fun(w, texte, color, div, draw, html, fenetre, top, tag, left, fichier):
    color_value = color.ret_color()
    if top.get() == "":
        top = 0
    else:
        top = top.get()

    if left.get() == "":
        left = 0
    else:
        left = left.get()
    if color_value == None:
        color_value = "#FFFFFF"
    if tag.get() != "":
        tag = tag.get()
        if w.get().isdigit():
            if float(w.get()) != 0:
                w=w.get()
                texte=texte.get("1.0",END)
                div.destroy()

                largeur = fenetre.winfo_screenwidth()*0.6*int(w)/100

                draw.create_text(fenetre.winfo_screenwidth()*0.6*(float(left)/100), fenetre.winfo_screenheight()*(float(top)/100), anchor="nw", tags=tag, text=texte, width=largeur)

                html_val = "<a id=\"{}\" style=\"margin-top:{}%;position:absolute;left:{}%;max-width:{}%;overflow-wrap:break-word;\">{}</a>".format(tag, top, left, w, texte)
                html_val = html_val.replace("\n", "<br>")

                html.ecrire(html_val)
            else:
                messagebox.showwarning("Error","Weight can't be egal to 0")
        else:
            messagebox.showwarning("Error", "You need to insert a integer")
    else:
        messagebox.showwarning("Error", "You need to insert an id")

#si id = 0 alors menu si id=1 alors pas menu
def supprimer_div(tag, draw, html, id):
    if id == 0:
        html_val = html.ret_menu()
    else:
        html_val = html.ret_html()

    reg = "<div id=\"{0}\" (.*)div>".format(tag)
    avant = "<div id=\"{0}\" ".format(tag) + re.findall(reg, html_val)[0] + "div>"
    # avant = """<div id="aze" style="width:20%;background:#df0f1d;height:3%;position:absolute;top:7%;left:39%"></div>"""
    draw.delete(tag)
    html_val = html_val.replace(avant, "")
    html.remplacer(html_val)

def supprimer_image(tag, draw, html):
    html_val = html.ret_html()
    reg = "<img id=\"{}\" (.*)>".format(tag)
    avant = "<img id=\"{}\" ".format(tag) + re.findall(reg, html_val)[0] + ">"
    draw.delete(tag)
    html_val = html_val.replace(avant, "")
    html.remplacer(html_val)

def ajout_image(fenetre, draw, fichier, html, directory, gifsdict):
    if fichier != "":
        if fichier == "menu.ew":
            messagebox.showwarning("Error", "Vous ne pouvez pas ajouter un conteneur au menu")
        else:
            div = Toplevel(fenetre)

            framewid = Frame(div)
            framewid.pack()
            L1 = Label(framewid, text="Largeur(%)")
            L1.pack( side = LEFT)
            widthlab = Entry(framewid, bd =5)
            widthlab.pack(side = RIGHT)

            framehgt = Frame(div)
            framehgt.pack()
            L1 = Label(framehgt, text="Hauteur(%)")
            L1.pack( side = LEFT)
            heightlab = Entry(framehgt, bd =5)
            heightlab.pack(side = RIGHT)

            frametop = Frame(div)
            frametop.pack()
            L1 = Label(frametop, text="Marge Top(%)  ")
            L1.pack( side = LEFT)
            toplab = Entry(frametop, bd =5)
            toplab.pack(side = RIGHT)

            frameleft = Frame(div)
            frameleft.pack()
            L1 = Label(frameleft, text="Marge Gauche(%)  ")
            L1.pack( side = LEFT)
            leftlab = Entry(frameleft, bd =5)
            leftlab.pack(side = RIGHT)

            frametag = Frame(div)
            frametag.pack()
            L1 = Label(frametag, text="ID (Doit être unique)")
            L1.pack( side = LEFT)
            taglab = Entry(frametag, bd =5)
            taglab.pack(side = RIGHT)

            image_sel = image()

            Button(div, text="Selectionner une image", command=partial(importer, image_sel, directory)).pack()

            Button(div, text="Ajouter", command=partial(ajouter_image, fenetre, draw, image_sel, html, directory, div, widthlab, leftlab, toplab, taglab, gifsdict, heightlab)).pack()

            div.mainloop()
    else:
        messagebox.showwarning("Error", "Vous devez choisir un fichier")

def importer(image_sel, directory):
    fichier = askopenfilename()
    image_sel.set_image(fichier)

def ajouter_image(fenetre, draw, image_sel, html, directory, div, w, left, top, tag, gifsdict, h):
    tag = tag.get()
    if top.get() == "":
        top = 0
    else:
        top = top.get()
    if left.get() == "":
        left = 0
    else:
        left = left.get()
    if tag != "":
        if w.get().isdigit():
            if float(w.get()) != 0:
                if image_sel.ret_image != "":
                    w=w.get()
                    h=h.get()
                    div.destroy()

                    img = image_sel.ret_image()
                    nom = basename(image_sel.ret_image())
                    nom_sans_ext = os.path.splitext(nom)[0]
                    ext = os.path.splitext(nom)[1]
                    ran = randint(1,1000000)
                    nom = nom_sans_ext + str(ran) + ext
                    copyfile(image_sel.ret_image(), directory + nom)

                    imgfile = directory + nom

                    largeur = fenetre.winfo_screenwidth()*0.6*int(w)/100
                    hauteur = fenetre.winfo_screenheight()*int(h)/100
                    photo = PIL.Image.open(imgfile)
                    resolution = (int(largeur),int(hauteur))
                    img = PIL.ImageTk.PhotoImage(photo.resize(resolution))
                    gifsdict[imgfile] = img
                    draw.create_image(fenetre.winfo_screenwidth()*0.6*(float(left)/100) + largeur/2, fenetre.winfo_screenheight()*(float(top)/100) + hauteur/2, image=img, tags=tag)
                    print(tag)
                    ecrire_image(tag, w, h, top, left, imgfile, html)
                else:
                    messagebox.showwarning("Error", "Vous devez mettre une image")
            else:
                messagebox.showwarning("Error","Weight can't be egal to 0")
        else:
            messagebox.showwarning("Error", "You need to insert a integer")
    else:
        messagebox.showwarning("Error", "You need to insert an id")

def maj_texte(draw, zone_text, tag, event):
    draw.itemconfigure(tag, text=zone_text.get("1.0",END))

def edit_texte(zone_text, l, t, w, draw, html, tag, fenetre):
    if t.get() == "":
        t = 0
    else:
        t = str(t.get())
    if l.get() == "":
        l = 0
    else:
        l = str(l.get())
    if w.get().isdigit():
        if float(w.get()) != 0:
            w = str(w.get())
            draw.delete(tag)
            draw.create_text(fenetre.winfo_screenwidth()*0.6*(float(l)/100), fenetre.winfo_screenheight()*(float(t)/100), anchor="nw", tags=tag, text=zone_text.get("1.0",END), width=fenetre.winfo_screenwidth()*0.6*(float(w)/100))
            html_val = html.ret_html()
            avant = re.findall('<a id="{}" style="(.*)</a>'.format(tag), html_val)[0]
            apres = "margin-top:{}%;position:absolute;left:{}%;max-width:{}%;overflow-wrap:break-word;\">{}".format(t, l, w, zone_text.get("1.0",END).replace("\n", "<br>"))
            html_val = html_val.replace(avant, apres)
            html.remplacer(html_val)
        else:
            messagebox.showwarning("Error","Weight can't be egal to 0")
    else:
        messagebox.showwarning("Error", "You need to insert a integer")

#pas utilisé pour le moment
def ajout_bouton(fichier, fenetre, draw):
    if fichier != "":
        color = selcolor()
        div = Toplevel(fenetre)
        framewid = Frame(div)
        framewid.pack()
        L1 = Label(framewid, text="Largeur(%)")
        L1.pack( side = LEFT)
        widthlab = Entry(framewid, bd =5)
        widthlab.pack(side = RIGHT)

        framemt = Frame(div)
        framemt.pack()
        L1 = Label(framemt, text="Hauteur(%)  ")
        L1.pack( side = LEFT)
        heightlab = Entry(framemt, bd =5)
        heightlab.pack(side = RIGHT)

        frametop = Frame(div)
        frametop.pack()
        L1 = Label(frametop, text="Marge Top(%)  ")
        L1.pack( side = LEFT)
        toplab = Entry(frametop, bd =5)
        toplab.pack(side = RIGHT)

        frameleft = Frame(div)
        frameleft.pack()
        L1 = Label(frameleft, text="Marge Gauche(%)  ")
        L1.pack( side = LEFT)
        leftlab = Entry(frameleft, bd =5)
        leftlab.pack(side = RIGHT)

        frametag = Frame(div)
        frametag.pack()
        L1 = Label(frametag, text="ID (Doit être unique)")
        L1.pack( side = LEFT)
        taglab = Entry(frametag, bd =5)
        taglab.pack(side = RIGHT)

        frametexte = Frame(div)
        frametexte.pack()
        L1 = Label(frametexte, text="Texte du bouton")
        L1.pack( side = LEFT)
        textelab = Entry(frametexte, bd =5)
        textelab.pack(side = RIGHT)

        Button(div, text='Couleur du bouton', command=partial(color.getColor)).pack()

        combo = ttk.Combobox(div)
        combo.insert(1, "coucou")
        combo.pack()

        Button(div, text="Ajouter", command=partial(ajout_bout_div, draw, widthlab, heightlab, toplab, leftlab, taglab, textelab, color, combo, div, fenetre)).pack()
        div.mainloop()
    else:
        messagebox.showwarning("Error", "Vous devez selectionner un fichier")

#pas utilisé pour le moment
def ajout_bout_div(draw, w, h, top, left, tag, text, color, link, div, fenetre):
    color_value = color.ret_color()

    if top.get() == "":
        top = 0
    else:
        top = top.get()
    if left.get() == "":
        left = 0
    else:
        left = left.get()
    if color_value == None:
        color_value = "#FFFFFF"
    if tag != "":
        if w.get().isdigit():
            if float(w.get()) != 0:
                w = w.get()
                if h.get().isdigit():
                    if float(h.get()) != 0:
                        h = h.get()
                        div.destroy()
                        draw.create_rectangle(fenetre.winfo_screenwidth()*0.6*(float(left)/100), fenetre.winfo_screenheight()*(float(top)/100), fenetre.winfo_screenwidth()*0.6*(float(left)/100) + fenetre.winfo_screenwidth()*0.6*(float(w)/100), fenetre.winfo_screenheight()*(float(top)/100)+fenetre.winfo_screenheight()*(float(h)/100), fill=color_value, tags=tag)
                        draw.create_text(0, 10, text="bouton", activefill="#2EFEF7")
                    else:
                        messagebox.showwarning("Error","Height can't be egal to 0")
                else:
                    messagebox.showwarning("Error", "You need to insert a integer")
            else:
                messagebox.showwarning("Error","Weight can't be egal to 0")
        else:
            messagebox.showwarning("Error", "You need to insert a integer")
    else:
        messagebox.showwarning("Error", "You need to insert an id")
