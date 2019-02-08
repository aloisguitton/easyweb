from tkinter import *
from fichier import *
from tkinter.filedialog import *
from tkinter import tix
from selcolor import *
from functools import partial         
from tkinter import messagebox

result=None

def ajout_div_fun(w, h, color, div, draw, html, fenetre, top, tag, left):
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
                        ajout_div_princ(div, draw, html, (w.get()), (h.get()), color_value, fenetre, top, (tag.get()), left)
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

def edit(w, h, top, left, tag, draw, color, fenetre, html, menu):
    color_value = color.ret_color()
    print(tag)
    print(color_value)
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
                if h.get().isdigit():
                    if float(h.get()) != 0:
                        draw.delete(tag)
                        if tag != "menu_bar_ew":
                            edit_ajout_div_princ(draw, html, (w.get()), (h.get()), color_value, fenetre, top, tag, left)
                            html.ret_html()
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

def ajout_div(fenetre, draw, fichier, html):
    color = selcolor()
    if fichier != "":
        div = Toplevel(fenetre)
        framewid = Frame(div)
        framewid.pack()
        L1 = Label(framewid, text="Width(%)")
        L1.pack( side = LEFT)
        widthlab = Entry(framewid, bd =5)
        widthlab.pack(side = RIGHT)
        
        framemt = Frame(div)
        framemt.pack()
        L1 = Label(framemt, text="Height(%)  ")
        L1.pack( side = LEFT)
        heightlab = Entry(framemt, bd =5)
        heightlab.pack(side = RIGHT)

        frametop = Frame(div)
        frametop.pack()
        L1 = Label(frametop, text="Margin Top(%)  ")
        L1.pack( side = LEFT)
        toplab = Entry(frametop, bd =5)
        toplab.pack(side = RIGHT)

        frameleft = Frame(div)
        frameleft.pack()
        L1 = Label(frameleft, text="Margin Left(%)  ")
        L1.pack( side = LEFT)
        leftlab = Entry(frameleft, bd =5)
        leftlab.pack(side = RIGHT)

        frametag = Frame(div)
        frametag.pack()
        L1 = Label(frametag, text="ID (need to be unique)")
        L1.pack( side = LEFT)
        taglab = Entry(frametag, bd =5)
        taglab.pack(side = RIGHT)

        Button(div, text='Select Color', command=partial(color.getColor)).pack()

        Button(div, text="Valider", bg="Green", command=partial(ajout_div_fun, widthlab, heightlab, color, div, draw, html, fenetre, toplab, taglab, leftlab)).pack(side=BOTTOM)
        div.mainloop()
    else:
        messagebox.showwarning("Error", "You need to open a file")

def edit_ajout_menu(draw, menu, w, h, color, fenetre, top, tag, left):
    draw.create_rectangle("0", "0", fenetre.winfo_screenwidth()*0.6, fenetre.winfo_screenheight()*(float(h)/100), fill=color, tags="menu_bar_ew")
    html_val = menu.ret_menu()
    print(html_val)
    print(tag)
    avant = re.findall('<div id="{0}" style="(.*)">'.format(tag), html_val)[0]
    apres = "position:absolute;width:{0};background:{1};height:52px;".format(w, color)
    html_val = html_val.replace(avant, apres)
    menu.remplacer(html_val)
    
def edit_ajout_div_princ(draw, html, w, h, color, fenetre, top, tag, left):
    draw.create_rectangle(fenetre.winfo_screenwidth()*0.6*(float(left)/100), fenetre.winfo_screenheight()*(float(top)/100), fenetre.winfo_screenwidth()*0.6*(float(left)/100) + fenetre.winfo_screenwidth()*0.6*(float(w)/100), fenetre.winfo_screenheight()*(float(top)/100)+fenetre.winfo_screenheight()*(float(h)/100), fill=color, tags=tag)
    html_val = html.ret_html()
    avant = re.findall('<div id="{0}" style="(.*)">'.format(tag), html_val)[0]
    apres = "width:{0}%;background:{1};height:{2}%;position:absolute;top:{3}%;left:{4}%".format(w, color, h, top, left)
    html_val = html_val.replace(avant, apres)
    html.remplacer(html_val)

def ajout_div_princ(div, draw, html, w, h, color, fenetre, top, tag, left):
    div.destroy()
    draw.create_rectangle(fenetre.winfo_screenwidth()*0.6*(float(left)/100), fenetre.winfo_screenheight()*(float(top)/100), fenetre.winfo_screenwidth()*0.6*(float(left)/100) + fenetre.winfo_screenwidth()*0.6*(float(w)/100), fenetre.winfo_screenheight()*(float(top)/100)+fenetre.winfo_screenheight()*(float(h)/100), fill=color, tags=tag)
    html_val = "<div id=\"{0}\" style=\"width:{1}%;background:{2};height:{3}%;position:absolute;top:{4}%;left:{5}%\"></div>\n".format(tag, w, color, h, top, left)
    html.ecrire(html_val)
