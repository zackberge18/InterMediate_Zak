import datetime

now_for_me = datetime.datetime.now()
uno_date = datetime.datetime(now_for_me.year, 5, 5)
dos_date = datetime.datetime(now_for_me.year, 5, 10)
mi = dos_date - uno_date
print(mi)
print(now_for_me - uno_date)

formula = ((100*(now_for_me - uno_date)) / (dos_date - uno_date))

print(formula)
from tkinter import *

class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.label=Label(self,text="my legacy")
        self.label.pack()
        self.bind("<B1-Motion>",self.a)
        self.bind("<w>", self.d)
        self.bind("<s>", self.s)
        self.bind("<d>", self.w)


    def a(self,event):

        a="a"
        self.label.config(text=f"{a}")

    def s(self, event):
            a = "s"
            self.label.config(text=f"{a}")

    def d(self,event):

        a="w"
        self.label.config(text=f"{a}")

    def w(self,event):

        a="d"
        self.label.config(text=f"{a}")


if __name__ == '__main__':
    app=App()
    app.mainloop()