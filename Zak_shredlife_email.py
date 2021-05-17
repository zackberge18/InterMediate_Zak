from tkinter import *
import os
import smtplib
import imghdr
from email.message import EmailMessage
from PIL import Image, ImageTk


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
        my_image = ImageTk.PhotoImage(Image.open("char_naruto/z.png"))
        my_image2 = ImageTk.PhotoImage(Image.open("char_naruto/l.png"))
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

        self.clear_button = Button(btn_frame, image=my_image,
                                   command=lambda: self.email_me(1, self.my_text.get(1.0, END), self.my_text.get(1.0, 2.0)),
                                   relief=GROOVE)
        self.clear_button.pack(side=LEFT, padx=(5, 0), ipadx=20, pady=10)
        self.get_button = Button(btn_frame, image=my_image2,
                                 command=lambda: self.email_me(2, self.my_text.get(1.0, END), self.my_text.get(1.0, 2.0)),
                                 relief=GROOVE)

        self.get_button.pack(side=RIGHT, padx=10, ipadx=30, pady=10)

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

    def email_me(self,x, y, z):
        e_mail = "ukena18@gmail.com"
        pass_word = "2125253032"

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(e_mail, pass_word)

            subject = z

            msg = f"{z}\n\n{y}"
            if x == 1:
                smtp.sendmail(e_mail, "ukena18@gmail.com", msg)
            elif x == 2:
                smtp.sendmail(e_mail, "ukena18@gmail.com", msg)


if __name__ == '__main__':
    app = App()
    app.mainloop()
import os
import smtplib
import imghdr
from email.message import EmailMessage

from tkinter import *
def email_me(x,y,z):
    e_mail="ukena18@gmail.com"
    pass_word="2125253032"


    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(e_mail,pass_word)

        subject=z

        msg=f"{z}\n\n{y}"
        if x==1:
            smtp.sendmail(e_mail,"ukena18@gmail.com",msg)
        elif x==2:
            smtp.sendmail(e_mail, "ukena18@gmail.com", msg)
