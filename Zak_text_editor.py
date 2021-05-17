from tkinter import *
from tkinter import filedialog

class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.geometry("1200x660")

        #####Create Main Frame

        self.my_frame=Frame(self)
        self.my_frame.pack(pady=5)

        #####CREATE OUR SCROLLBAR
        self.text_scroll = Scrollbar(self.my_frame)
        self.text_scroll.pack(side=RIGHT, fill=Y)


        #######Create TExt box

        self.my_text=Text(self.my_frame,width=50,height=20,font="arial 20 bold",selectbackground="brown",selectforeground="orange",yscrollcommand=self.text_scroll.set)
        self.my_text.pack(side=LEFT)

        #####cofigure our scroll bar
        self.text_scroll.config(command=self.my_text.yview)
        self.my_menu=Menu(self)
        self.config(menu=self.my_menu)

        ##ad_file menu
        file_menu=Menu(self.my_menu,tearoff=False)
        self.my_menu.add_cascade(label="File",menu=file_menu)
        file_menu.add_command(label="new")
        file_menu.add_command(label="open")
        file_menu.add_command(label="save")
        file_menu.add_separator()
        file_menu.add_command(label="exit",command=self.quit)
        #edit menu
        edit_menu = Menu(self.my_menu, tearoff=False)
        self.my_menu.add_cascade(label="Edit", menu=file_menu)
        edit_menu.add_command(label="copy")
        edit_menu.add_command(label="paste")
        edit_menu.add_command(label="cut")
        edit_menu.add_separator()
        edit_menu.add_command(label="exit")

        #add status bar
        status_bar=Label(self,text="Ready       ",anchor=E)
        status_bar.pack(fill=X,side=BOTTOM,ipady=5)


if __name__ == '__main__':
    app=App()
    app.mainloop()