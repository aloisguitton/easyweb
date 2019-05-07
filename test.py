from tkinter import *

root = Tk()

def key(event):
    print ("pressed", repr(event.char))


e = Text(root)
e.bind("<Key>", key)
e.pack()
root.mainloop()
