from tkinter import *
from PIL import Image,ImageTk
import sqlite3
from tkinter import ttk

class App(Tk):
    def __init__(self):
        Tk.__init__(self)


        self.my_notebook=ttk.Notebook(self)
        self.my_notebook.pack(pady=15,fill=BOTH)


        ####DAtaabase
        conn=sqlite3.connect("shred_life.db")

        c=conn.cursor()

        #c.execute("""CREATE TABLE shred_life(
        #first_name text,
        #first_date_1 integer,
        #first_date_2 integer,
        #last_date_1 integer,
        #last_date_2 integer
        #
        #)""")
##
        #c.execute("DELETE FROM shred_life WHERE first_name=:first",{'first':'zacd'})

        c.execute("SELECT * FROM shred_life")
        a=c.fetchall()
        print(a)
        conn.commit()

        conn.close()

        ####create entry frame
        entry_frame=Frame(self.my_notebook)
        entry_frame.pack()

        ###inside entry frame create Labels
        my_name_entry_label=Label(entry_frame,text="NAme")
        my_name_entry_label.grid(row=0,column=0)
        my_date_entry_label = Label(entry_frame, text="date")
        my_date_entry_label.grid(row=1, column=0)

        #####INside entry frame create Entrys
        self.name_entry=Entry(entry_frame,width=40)
        self.name_entry.grid(row=0,column=1,columnspan=7,pady=5)

        self.date_entrya1 = Entry(entry_frame,width=5)
        self.date_entrya1.grid(row=1, column=1)
        Label(entry_frame,text="/").grid(row=1,column=2)
        self.date_entrya2 = Entry(entry_frame, width=5)
        self.date_entrya2.grid(row=1, column=3)
        Label(entry_frame, text=">>>>to>>>>").grid(row=1,column=4)
        self.date_entryab1 = Entry(entry_frame, width=5)
        self.date_entryab1.grid(row=1, column=5)
        Label(entry_frame, text="/").grid(row=1,column=6)
        self.date_entryab2= Entry(entry_frame, width=5)
        self.date_entryab2.grid(row=1, column=7)

        self.send_db_button=Button(entry_frame,text="confirm",command=self.create_db,pady=10,padx=10)
        self.send_db_button.grid(row=2,column=0,pady=10)
        #######
        second_frame=Frame(self.my_notebook)
        second_frame.pack()


        self.my_notebook.add(entry_frame,text="Entry Frame")
        self.my_notebook.add(second_frame, text="show Frame")

        #####TItle frame
        self.title_frame = Frame(second_frame, bg="yellow", bd=5)
        self.title_frame.grid(row=0, column=0, columnspan=2)
        #####Label for title
        name_title = Label(self.title_frame, text="Names", anchor=E)
        name_title.grid(row=0, column=0, ipadx=110)
        f_date_title = Label(self.title_frame, text="f_date", anchor=E)
        f_date_title.grid(row=0, column=1, ipadx=110)
        l_date_title = Label(self.title_frame, text="l_Date", anchor=E)
        l_date_title.grid(row=0, column=2, ipadx=160)

        #######FRame for name and process bar

        self.name_frame = Frame(second_frame, bg="blue", bd=5)
        self.name_frame.grid(row=1, column=0)
        self.processbar_frame = Frame(second_frame, bg="brown", bd=5)
        self.processbar_frame.grid(row=1, column=1)
        self.test1_button = Button(second_frame, text="Databese it", command=self.database_it)
        self.test1_button.grid(row=43, column=0, columnspan=2)
        self.test3_button = Button(second_frame, text="time module check it", command=self.database_it)
        self.test3_button.grid(row=44, column=0, columnspan=2)

    def time_module(self, month1, day1, month2, day2):
        import datetime

        now_for_me = datetime.datetime.now()
        uno_date = datetime.datetime(now_for_me.year, month1, day1)
        dos_date = datetime.datetime(now_for_me.year, month2, day2)
        mi = dos_date - uno_date
        formula = 100 * ((now_for_me - uno_date) / (dos_date - uno_date))
        #
        print(int(formula))

        return int(formula)

    def database_it(self):
        conn = sqlite3.connect("shred_life.db")

        c = conn.cursor()

        c.execute("SELECT * FROM shred_life")
        self.my_list = c.fetchall()
        for i in range(len(self.my_list)):
            self.my_name = Label(self.name_frame, text=self.my_list[i][0] + ">>>>>>>>")
            self.my_name.grid(row=i, column=0, ipadx=200, ipady=40)

            date_frame = Frame(self.processbar_frame, width=600, bg="grey")
            date_frame.pack()
            bar_frame = Frame(self.processbar_frame)
            bar_frame.pack()

            ############date for progress bar
            f_date = Label(date_frame, text=str(self.my_list[i][1]) + "/" + str(self.my_list[i][2]), anchor=W, width=28,
                           height=3)
            f_date.pack(side=LEFT)
            ############date for progress bar
            l_date = Label(date_frame, text=str(self.my_list[i][3]) + "/" + str(self.my_list[i][4]), anchor=E, width=27)
            l_date.pack(side=RIGHT)

            ####### PRogress bar

            my_progress = ttk.Progressbar(bar_frame, orient=HORIZONTAL, length=400, mode="determinate")
            my_progress.pack(ipady=15, side=BOTTOM)
            #### progres bar value
            berge = self.time_module(self.my_list[i][1], self.my_list[i][2], self.my_list[i][3], self.my_list[i][4])
            my_progress["value"] = berge

        conn.commit()

        conn.close()

    def create_db(self):
        ###Create a connection or new db file
        conn=sqlite3.connect("shred_life.db")
        c=conn.cursor()

        # c.execute("INSERT INTO shreder VALUES('Zack','Berge','05/25','06/10')")
        #c.execute("INSERT INTO shreder VALUES(:first,:last,:pay)",{'first':emp1,'last':emp2,'pay':pay})
        c.execute("INSERT INTO shred_life VALUES(:name,:a1,:a2,:b1,:b2)",{"name":self.name_entry.get(),"a1":self.date_entrya1.get(),"a2":self.date_entrya2.get(),
                                                                       "b1":self.date_entryab1.get(),"b2":self.date_entryab2.get()})



        conn.commit()

        conn.close()


if __name__ == '__main__':
    app=App()
    app.geometry("500x500")
    app.title("shredlife")
    app.mainloop()





