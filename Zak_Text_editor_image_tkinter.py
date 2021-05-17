from tkinter import *
from PIL import Image, ImageTk
from tkinter import font


class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title("SHredlife")
        txt_frame = Frame(self)
        txt_frame.config(width=80, height=20)
        txt_frame.pack()

        global my_image
        global my_image2
        global my_image3
        my_image = ImageTk.PhotoImage(Image.open("char_naruto/naruto.png"))
        my_image2 = ImageTk.PhotoImage(Image.open("char_naruto/sasuke.png"))
        self.my_image3 = ImageTk.PhotoImage(Image.open("char_naruto/kakashi.png"))

        self.my_text = Text(txt_frame, width=60, height=20, font="arial 15", bd=3)

        self.my_text.pack(pady=10, side=LEFT)
        text_scroll = Scrollbar(txt_frame)
        text_scroll.pack(side=RIGHT, fill=Y)
        self.my_text.config(yscrollcommand=text_scroll.set)
        text_scroll.config(command=self.my_text.yview)

        btn_frame = Frame(self)
        btn_frame.config(width=60, height=20)
        btn_frame.pack(side=BOTTOM)

        self.clear_button = Button(btn_frame, image=my_image,command=self.clear,relief=GROOVE)
        self.clear_button.pack(side=LEFT, padx=(5, 0), ipadx=20, pady=10)
        self.get_button = Button(btn_frame, image=my_image2,
                                 command=self.clear,
                                 relief=GROOVE)

        self.get_button.pack(side=RIGHT, padx=10, ipadx=30, pady=10)
        self.select_button=Button(self,text="select",command=self.select)
        self.select_button.pack()
        self.bold_button=Button(self,text="BOLd",command=self.bolder)

        self.bold_button.pack()

    def clear(self):
        my_label = Label(self, text=self.my_text.get(1.0, END)).pack()
        self.clear_button.config(image=self.my_image3)
        my_label = Label(self, text=self.my_text.get(1.0, END)).pack()
        position = self.my_text.index(INSERT)

        self.my_text.image_create(position, image=my_image)
        print(position)

    def text_i(self):
        a = self.my_text.get(1.0, END)
        return a
    def select(self):
        selected=self.my_text.selection_get()
        Label(self,text=selected).pack()

    def bolder(self):
        bold_font=font.Font(self.my_text,self.my_text.cget("font"))
        bold_font.configure(weight="bold")
        self.my_text.tag_configure("bold",font=bold_font)
        self.my_text.tag_add("bold","sel.first","sel.last")
if __name__ == '__main__':
    app = App()
    app.mainloop()