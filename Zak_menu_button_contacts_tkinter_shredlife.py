from tkinter import *
from PIL import Image,ImageTk

class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.title("Shred-life Eco")
        self.geometry("400x600")
        self.my_menu=Menu(self)
        self.config(menu=self.my_menu)

        #Photo for button
        self.info_img=ImageTk.PhotoImage(file="shred/info.jpg")
        self.people_img=ImageTk.PhotoImage(file="shred/people.jpg")
        self.event_img=ImageTk.PhotoImage(file="shred/event.jpg")
        self.book_img=ImageTk.PhotoImage(file="shred/travel.png")

        ##create menu items
        self.main_menu=Menu(self.my_menu)
        self.my_menu.add_cascade(label="Contact",menu=self.main_menu)
        self.main_menu.add_command(label="Zach",command=lambda : self.call_me(1))
        self.main_menu.add_command(label="Lori",command=lambda : self.call_me(2))
        self.book_btn = Button(self,text="book   ",padx=60,pady=60,command=self.book_func)
        self.info_btn = Button(self, text="Info    ",padx=60,pady=60)
        self.people_btn = Button(self, text="People",padx=60,pady=60)
        self.events_btn = Button(self, text="EVents",padx=60,pady=60)
        self.book_btn.grid(row=0,column=0,pady=(50,0),padx=(30,0))
        self.info_btn.grid(row=0, column=1,pady=(50,0))
        self.people_btn.grid(row=1, column=0,padx=(30,0))
        self.events_btn.grid(row=1, column=1)

    def call_me(self,x):
        self.book_btn.destroy()
        self.info_btn.destroy()
        self.people_btn.destroy()
        self.events_btn.destroy()
        self.we = Frame(self)
        self.we.pack(fill=BOTH, expand=1)
        if x==1:
            self.contact_label=Label(self.we,text="Zack* \n 9703454345",bd=3,bg="grey",fg="brown",font="arial 30 bold",borderwidth=3)
            self.contact_label.pack()
        else:
            self.contact_label = Label(self.we, text="#Lori \n 9703454345", bd=3, bg="grey", fg="brown",font="arial 30 bold",borderwidth=3)
            self.contact_label.pack()

    def book_func(self):
        list_of_day=[1,2,3,4]

        self.book_btn.destroy()
        self.info_btn.destroy()
        self.people_btn.destroy()
        self.events_btn.destroy()

        #Label(self.book_frame,text="BEst Travel To Dillon Area",font="arial 20 bold").pack()
        #self.days=StringVar()
        #self.days.set("Any")
        #self.drop=OptionMenu(self.book_frame,self.days,*list_of_day).pack(pady=30)
        #self.book_apply=Button(self.book_frame,text="apply",command=self.day,padx=30).pack()
#

    def day(self):
        Label(self.book_frame,text=f"Congrat, you succesfully booked for").pack()
        Label(self.book_frame,image=PhotoImage(Image.open("shred/shredlife.png"))).pack()

if __name__ == '__main__':
    app=App()
    app.mainloop()