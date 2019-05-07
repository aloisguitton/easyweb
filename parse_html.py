import re
from edition import *

def parse(fichier, draw, fenetre, html, gifsdict):
    with open(fichier, 'r') as mon_fichier:
                txt = mon_fichier.read()
    body = re.findall(r"<body>(.*)</body>", txt, re.MULTILINE | re.DOTALL)[0]
    try:
        menu = re.findall(r"<ul(.*)</ul>", txt, re.MULTILINE | re.DOTALL)[0]
    except:
        menu = ""
    debut = re.findall(r"(.*)<body>", txt, re.MULTILINE | re.DOTALL)[0]

    div_liste = re.findall('<div(.*)>', body)
    img_liste = re.findall('<img(.*)>', body)
    a_liste = re.findall('<a id(.*)>', body)

    html.reset()
    html.ecrire(debut + "<body>" + body)

    draw.delete("all")


    try:
        for div in div_liste:
            l =  re.findall('left:(.*)%', div)[0]
            w = re.findall('width:(.*)%;b', div)[0]
            h = re.findall('height:(.*)%;p', div)[0]
            color = re.findall('background:(.*);h', div)[0]
            top = re.findall('top:(.*)%;l', div)[0]
            tag = re.findall('id="(.*)" st', div)[0]
            draw.create_rectangle(fenetre.winfo_screenwidth()*0.6*(float(l)/100), fenetre.winfo_screenheight()*(float(top)/100), fenetre.winfo_screenwidth()*0.6*(float(l)/100) + fenetre.winfo_screenwidth()*0.6*(float(w)/100), fenetre.winfo_screenheight()*(float(top)/100)+fenetre.winfo_screenheight()*(float(h)/100), fill=color, tags=tag)

        for img in img_liste:

            l =  re.findall('left:(.*)%', img)[0]
            w = re.findall('width:(.*)%;h', img)[0]
            h = re.findall('height:(.*)%;p', img)[0]
            top = re.findall('top:(.*)%;l', img)[0]
            tag = re.findall('id="(.*)" st', img)[0]
            imgre = re.findall('src="(.*)"', img)[0]

            imgfile = imgre

            largeur = fenetre.winfo_screenwidth()*0.6*int(w)/100
            hauteur = fenetre.winfo_screenheight()*int(h)/100

            photo = PIL.Image.open(imgfile)
            resolution = (int(largeur),int(hauteur))
            img = PIL.ImageTk.PhotoImage(photo.resize(resolution))
            gifsdict[imgfile] = img

            draw.create_image(fenetre.winfo_screenwidth()*0.6*(float(l)/100) + largeur/2, fenetre.winfo_screenheight()*(float(top)/100) + hauteur/2, image=img, tags=tag)

        for texte in a_liste:
            tag = re.findall('="(.*)" sty', texte)[0]
            t = re.findall('margin-top:(.*)%;p', texte)[0]
            l = re.findall('left:(.*)%;m', texte)[0]
            w = re.findall('max-width:(.*)%;o', texte)[0]
            txt_aff = re.findall('">(.*)</a', texte)[0]


            txt_aff = txt_aff.replace("<br>", "\n")

            draw.create_text(fenetre.winfo_screenwidth()*0.6*(float(l)/100), fenetre.winfo_screenheight()*(float(t)/100), anchor="nw", tags=tag, text=txt_aff, width=fenetre.winfo_screenwidth()*0.6*(float(w)/100))

        if menu != "":
            print("ici")
            ajout_lien_menu_div(draw, txt, fenetre)
    except:
        pass

def pre_parse_menu(menu):

    with open("menu.ew", 'r') as mon_fichier:
                txt = mon_fichier.read()

    div_princ = re.findall('<div(.*)">', txt)
    menu.ecrire(txt)

def parse_menu(menu, draw, fenetre):

    with open("menu.ew", 'r') as mon_fichier:
                txt = mon_fichier.read()

    div_liste = re.findall('<div(.*)">', txt)

    menu.reset()
    menu.ecrire(txt)

    draw.delete("all")


    for div in div_liste:
        l =  re.findall('left:(.*)%', div)[0]
        w = re.findall('width:(.*)%;b', div)[0]
        h = re.findall('height:(.*)%;p', div)[0]
        color = re.findall('background:(.*);h', div)[0]
        top = re.findall('top:(.*)%;l', div)[0]
        tag = re.findall('id="(.*)" st', div)[0]
        draw.create_rectangle(fenetre.winfo_screenwidth()*0.6*(float(l)/100), fenetre.winfo_screenheight()*(float(top)/100), fenetre.winfo_screenwidth()*0.6*(float(l)/100) + fenetre.winfo_screenwidth()*0.6*(float(w)/100), fenetre.winfo_screenheight()*(float(top)/100)+fenetre.winfo_screenheight()*(float(h)/100), fill=color, tags=tag)

    ajout_lien_menu_div(draw, txt, fenetre)
