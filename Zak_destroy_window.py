from tkinter import *
import time


class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.geometry("800x800")
        self.my_button=Button(self,text="ter",command=self.do_it,padx=20,pady=20)
        self.my_button.pack()
        self.x=500
        self.y=500
        self.after(100,self.do_it)
    def do_it(self):
        self.geometry(f"{self.x}x{self.y}")
        self.x-=1
        self.y-=1

        print(self.x,self.y)
        self.after(250,self.do_it)




if __name__ == '__main__':
    app=App()
    app.mainloop()