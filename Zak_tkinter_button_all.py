
#button Image

"""from tkinter import *
from PIL import ImageTk,Image
class fe:
    def __init__(self,root):
      self.root=root
      photo=ImageTk.PhotoImage(Image.open("pink.jpg"))
      self.b = Button(self.root,image=photo,width="400",height="600")
      self.b.pack()


root = Tk()
front_end=fe(root)
root.mainloop()"""


#button Image

"""from tkinter import *
from PIL import ImageTk,Image
root=Tk()
b=Button(root,justify = RIGHT)
photo=ImageTk.PhotoImage(Image.open("pink.jpg"))
b.config(image=photo,width="400",height="400")
b.pack(side=LEFT)
root.mainloop()
"""
#button Image
"""from tkinter import *
#from tkinter.ttk import *
import PIL
from PIL import ImageTk,Image
first = Tk()
Label(first, text = 'Welcome To My Domain', font =(
'Verdana', 17)).pack(side = LEFT, pady = 11)
imge =ImageTk.PhotoImage(Image.open("pink.jpg"))
Button(first, text = 'Have a Nice Day !', image = imge).pack(side = LEFT)
mainloop()
"""

### imRead size of button
"""from tkinter import *
import PIL
from PIL import ImageTk,Image
import cv2

im = cv2.imread('pink.jpg')

h,w,d=im.shape

def set():
    var.set("Good-Bye Cruel World")


root = Tk()
root.geometry(f"{h}x{w}")
imge =ImageTk.PhotoImage(Image.open("pink.jpg"))
my_size=Image.open("pink.jpg")


frame = Frame(root,height=h,width=w)
frame.pack()

var = StringVar()
var.set("Hello World")


label1 = Label(frame, textvariable=var)
label1.pack()

label2 = Label(frame, image=imge)
label2.pack()

button = Button(frame, text="set", command=set)
button.pack()

root.mainloop()

"""
# (225, 400, 3)"""

from tkinter import *
"""

def retrieve():
    print(my_entry.get())
    print(my_entry2.get())


root = Tk()
root.geometry("200x150")

frame = Frame(root)
frame.pack()

my_entry = Entry(frame, width=46,bd=45)
my_entry.insert(2,"aaaaaa")
my_entry.insert(0, 'cccccc')
my_entry.pack(padx=5, pady=5)

my_entry2 = Entry(frame, width=15)
my_entry2.insert(0, 'password')
my_entry2.pack(padx=5, pady=5)

Button = Button(frame, text="Submit", command=retrieve)
Button.pack(padx=5, pady=5)

root.mainloop()
"""
"""from tkinter import *

root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()
def PPP():
    if RBttn==1:
        print("a")
    if RBttn2==1:
        print("b")


Var1 = StringVar()

RBttn = Radiobutton(frame, text="Option1", variable=Var1,command=PPP,
                    value=1)
print(RBttn)
RBttn.pack(padx=5, pady=5)


RBttn2 = Radiobutton(frame, text="Option2", variable=Var1,command=PPP,
                     value=2)
RBttn2.pack(padx=5, pady=5)


root.mainloop()"""

"""from tkinter import *


def retrieve():
    print(Var1.get())


root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()

Var1 = IntVar()

RBttn = Radiobutton(frame, text="Burger", variable=Var1,
                    value=1)
RBttn.pack(padx=5, pady=5)

RBttn2 = Radiobutton(frame, text="Pizza", variable=Var1,
                     value=2)
RBttn2.pack(padx=5, pady=5)

Button = Button(frame, text="Submit", command=retrieve)
Button.pack()

root.mainloop()
"""
"""from tkinter import *


def retrieve():
    print(Var1.get())


root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()

Var1 = IntVar()

RBttn = Radiobutton(frame, text="Burger", variable=Var1,
                    value=1, command=retrieve)
RBttn.pack(padx=5, pady=5)

RBttn2 = Radiobutton(frame, text="Pizza", variable=Var1,
                     value=2, command=retrieve)
RBttn2.pack(padx=5, pady=5)

root.mainloop()"""
#########Check button
"""from tkinter import *


def retrieve():
    if Var1.get()==True:
        print(Var1.get())
    if Var2.get()==True:
        print(Var2.get())


root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()

Var1 = IntVar()
Var2 = IntVar()

ChkBttn = Checkbutton(frame, text="Option1", variable=Var1)
ChkBttn.pack(padx=5, pady=5)

ChkBttn2 = Checkbutton(frame, text="Option2", variable=Var2)
ChkBttn2.pack(padx=5, pady=5)

Button = Button(frame, text="Submit", command=retrieve)
Button.pack(padx=5, pady=5)

root.mainloop()"""
"""
from tkinter import *
from tkinter import ttk


def retrieve():
    print(Combo.get())


root = Tk()
root.geometry("200x150")

frame = Frame(root)
frame.pack()

vlist = ["Option1", "Option2", "Option3",
         "Option4", "Option5"]

Combo = ttk.Combobox(frame, values=vlist)
Combo.set("Pick an Option")
Combo.pack(padx=5, pady=5)

Button = Button(frame, text="Submit", command=retrieve)
Button.pack(padx=5, pady=5)

root.mainloop()"""
####### scroll bar
"""from tkinter import *

root = Tk()

frame = Frame(root, width=300, height=300)
frame.pack(expand=True, fill=BOTH)

canvas = Canvas(frame, bg='white', width=300, height=300,
                scrollregion=(0, 0, 500, 500))

hbar = Scrollbar(frame, orient=HORIZONTAL)
hbar.pack(side=BOTTOM, fill=X)
hbar.config(command=canvas.xview)

vbar = Scrollbar(frame, orient=VERTICAL)
vbar.pack(side=RIGHT, fill=Y)
vbar.config(command=canvas.yview)

canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(side=LEFT, expand=True, fill=BOTH)

root.mainloop()"""

