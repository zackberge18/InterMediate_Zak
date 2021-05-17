from tkinter import *
from tkinter import ttk
class App(Tk):

    def __init__(self):
        super(App, self).__init__()
        self.geometry("500x500")
        my_progress=ttk.Progressbar(self,orient=HORIZONTAL,length=300,mode="determinate")
        my_progress.pack(padx=10)
        my_progress["value"]=+88
        Label(self, text="88").pack()
        #if name == "berry":
        #    my_progress["value"] += 20
        #if name=="carlos":
        #    my_progress["value"]+=87


if __name__ == '__main__':
    app=App()
    app.mainloop()
