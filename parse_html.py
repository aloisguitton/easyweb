import re

def parse(fichier, draw, fenetre, html):
    with open(fichier, 'r') as mon_fichier:
                txt = mon_fichier.read()
    div_liste = re.findall('<div(.*)', txt)
    
    html.reset()
    html.ecrire("\n"+txt)

    draw.delete("all")

    for div in div_liste:
        w = re.findall('width:(.*)%;b', div)[0]
        h = re.findall('height:(.*)%;p', div)[0]
        color = re.findall('background:(.*);h', div)[0]
        top = re.findall('top:(.*)%', div)[0]
        tag = re.findall('id="(.*)" st', div)[0]
        draw.create_rectangle("0", fenetre.winfo_screenheight()*(float(top)/100), fenetre.winfo_screenwidth()*0.6*(float(w)/100), fenetre.winfo_screenheight()*(float(top)/100)+fenetre.winfo_screenheight()*(float(h)/100), fill=color, tags=tag)