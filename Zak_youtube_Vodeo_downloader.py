from tkinter import *
import pytube
from pytube import YouTube




class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title("Ridwan Xelil U Ferizat Kaya")
        self.geometry("500x300")
        self.resizable(0,0)
        self.my_label=Label(self,text="Youtube Video Daxa Kurmanci", font="arial 20 bold")
        self.my_label.pack()
        self.my_entry=Entry(self,width=50,font="Helvetica 12 bold")
        self.my_entry.pack()
        self.my_button=Button(self,text="Ji youtube DAxa",command=self.down_me)
        self.my_button.pack()

    def down_me(self):
        self.url = YouTube(str(self.my_entry.get()))
        self.video = self.url.streams.first()
        self.video.download()
        self.succes_label=Label(self,text="Kertwene Video daxist",font="arial 10 bold")
        self.succes_label.pack()





if __name__ == '__main__':

    app=App()
    app.mainloop()