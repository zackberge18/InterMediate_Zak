from tkinter import *
from PIL import Image,ImageTk
import time
import sqlite3
import progress_bar




class App(Tk):

    def __init__(self):
        super(App, self).__init__()
        self.title("Shred life Eco")
        self.geometry("475x600")



        ####MAin frame
        self.main_frame=Frame(self)
        self.main_frame.pack(fill="both",expand=True)


        # 4 button for the first time

        self.travel_btn = Button(self.main_frame,text="TraveL ",command=self.travel_func,padx=50,pady=60,font="arial 20 bold")
        self.info_btn = Button(self.main_frame,text="Info    ", command=self.travel_func,padx=50,pady=60,font="arial 20 bold")
        self.people_btn = Button(self.main_frame,text="People", command=self.people_func,padx=50,pady=60,font="arial 20 bold")
        self.events_btn = Button(self.main_frame,text="Events", command=self.travel_func,padx=50,pady=60,font="arial 20 bold")

        ####4 main button pack
        self.travel_btn.grid(row=0, column=0, pady=(50, 0), padx=(30, 0))
        self.info_btn.grid(row=0, column=1, pady=(50, 0))
        self.people_btn.grid(row=1, column=0, padx=(30, 0))
        self.events_btn.grid(row=1, column=1)




    def travel_func(self):
        self.main_frame.destroy()
        self.travel_frame = Frame(self)
        self.travel_frame.pack(fill="both", expand=True)

        #room Button
        self.green_room = Button(self.travel_frame, text="Green Room", padx=30, pady=10,font="arial 10 bold",command=lambda : self.green_room_func(1))
        self.yellow_room = Button(self.travel_frame, text="Yellow Room", padx=30, pady=10,font="arial 10 bold",command=lambda : self.green_room_func(2))
        self.girl_room = Button(self.travel_frame, text="Girl Room", padx=30, pady=10,font="arial 10 bold",command=lambda :  self.green_room_func(3))
        self.blue_room = Button(self.travel_frame, text="Blue room", padx=30, pady=10,font="arial 10 bold",command=lambda :  self.green_room_func(4))
        self.a,self.b,self.c,self.d=0,0,0,0

        ### LAbel Button
        self.green_room_label = Label(self.travel_frame, text=f"{self.a}/5",font="30")
        self.yellow_room_label = Label(self.travel_frame, text=f"{self.b}/3",font="30")
        self.girl_room_label = Label(self.travel_frame, text=f"{self.c}/1",font="30")
        self.blue_room_label = Label(self.travel_frame, text=f"{self.d}/3",font="30")
        self.green_room_label.grid(row=0, column=0)
        self.yellow_room_label.grid(row=2, column=0)
        self.girl_room_label.grid(row=0, column=1)
        self.blue_room_label.grid(row=2, column=1)

        # room button pack
        self.green_room.grid(row=1, column=0, pady=100, padx=(30, 0))
        self.yellow_room.grid(row=3, column=0, pady=100)
        self.girl_room.grid(row=1, column=1, padx=(30, 0))
        self.blue_room.grid(row=3, column=1)


    def  green_room_func(self,x):

            if x == 1:
                self.a = self.a + 1
                self.green_room_label.config(text=f"{self.a}/5")
#
                self.travel_frame.destroy()
                ####MAin frame
                self.main_frame = Frame(self)
                self.main_frame.pack(fill="both", expand=True)
#
                #LAbel for entry
                me=Label(self.main_frame, text="information", font=20)
                me.grid(row=0,column=0,columnspan=2,pady=(100,0),ipadx=50)
                self.name_label=Label(self.main_frame,text="name",font=20)
                self.last_label=Label(self.main_frame, text="last",font=20)
                self.name_label.grid(row=1,column=0,padx=40,pady=(20,0))
                self.last_label.grid(row=2, column=0,padx=40)
#
                self.name_entry=Entry(self.main_frame,width=30)
                self.last_entry=Entry(self.main_frame,width=30)
                self.name_entry.grid(row=1, column=1,pady=(20,0))
                self.last_entry.grid(row=2, column=1)
#
                self.buy_btn=Button(self.main_frame,text="buy",command=self.buy_btn_func,padx=10,pady=10)
                self.buy_btn.grid(row=3,column=0,columnspan=2)
#

            elif x == 2:
                self.b= self.b + 1

                self.yellow_room_label.config(text=f"{self.b}/3")
            elif x == 3:
                self.c = self.c+ 1
                self.girl_room_label.config(text=f"{self.c}/1")
            elif x == 4:
                self.d = self.d + 1
                self.blue_room_label.config(text=f"{self.c}/3")

    def buy_btn_func(self):
        self.buy_label = Label(self.main_frame, text=f"{str(self.name_entry.get())} succesfully booked", font="arial 10 bold")
        self.buy_label.grid(row=4, column=0, padx=40, pady=(20, 0),columnspan=2,ipadx=100)

        ###DAtabase
        ######Creata data base or connect to one
        conn = sqlite3.connect("capital_anime/customer.db")
        # create aCursor
        c = conn.cursor()
        ###create  a table

        c.execute("INSERT INTO customer VALUES (:f_name,:l_name)",
                  {
                      "f_name": self.name_entry.get(),
                      "l_name": self.last_entry.get()
                  }
                  )

        ####Commit changes
        conn.commit()

        conn.close()

    def people_func(self):
        self.main_frame.destroy()
        self.people_frame = Frame(self)
        self.people_frame.pack(fill="both", expand=True)

        ###DAtabase
        ######Creata data base or connect to one
        conn = sqlite3.connect("capital_anime/customer.db")
        # create aCursor
        c = conn.cursor()
        ###create  a table

        c.execute("SELECT *,oid FROM customer")
        records=c.fetchall()
        print(records)
        print_record=""
        self.the_label=Label(self.people_frame, text="People who are staying currently 1",bd=10, borderwidth=10,relief=SUNKEN, font=30,width=200)
        self.the_label.pack()
        a=0

        self.name_peopleframe=Frame(self.people_frame)
        self.name_peopleframe.pack(side=LEFT)

        Label(self.name_peopleframe,text=str("DOn julio"+ "\n"),font="arial 15 bold").pack()
        self.name_peopleframe_progress_bar = Frame(self.people_frame,bg="blue")
        self.name_peopleframe_progress_bar.pack(side=RIGHT)

        progress_bar.progress_bar(self.name_peopleframe_progress_bar)
        self.the_label.config(text=f"People who are staying currently {a}")



        ####Commit changes
        conn.commit()

        conn.close()


if __name__ == '__main__':
    app=App()
    app.mainloop()