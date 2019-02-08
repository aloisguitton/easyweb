import re

def parse(fichier, draw, fenetre, html):
    with open(fichier, 'r') as mon_fichier:
                txt = mon_fichier.read()
    body = re.findall(r"<body>(.*)</body>", txt, re.MULTILINE | re.DOTALL)[0]
    debut = re.findall(r"(.*)<body>", txt, re.MULTILINE | re.DOTALL)[0]
    div_liste = re.findall('<div(.*)>', body)
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
    except:
        pass
    
def parse_menu(menu, draw, fenetre):

    with open("menu.ew", 'r') as mon_fichier:
                txt = mon_fichier.read()
    
    # body = re.findall(r"<body>(.*)</body>", txt, re.MULTILINE | re.DOTALL)[0]
    # debut = re.findall(r"(.*)<body>", txt, re.MULTILINE | re.DOTALL)[0]
    div_princ = re.findall('<div(.*)">', txt)
    menu.ecrire(txt)
    # html.reset()
    # html.ecrire(debut + "<body>" + body)

    # draw.delete("all")
  
    for div in div_princ:
        color = re.findall('background:(.*);h', div)[0]
        draw.create_rectangle("0", "0", fenetre.winfo_screenwidth()*0.6, "52", fill=color, tags="menu_bar_ew")
