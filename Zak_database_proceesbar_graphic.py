
from tkinter import *
from tkinter import ttk
import sqlite3


class se(Tk):
    def __init__(self):
        super(se, self).__init__()
#### GET info from    Txt file
        try:
            my_text = open("sample.txt", "r")
            info_people=my_text.read()
            my_text.close()
            info_person=info_people.split(",")
            global info
            info=list()
            for a in info_person:
                info.append(a.split(":"))
            print(info)
        except:
            pass
#####TItle frame
        self.title_frame = Frame(self,bg="yellow",bd=5)
        self.title_frame.grid(row=0, column=0,columnspan=2)
#####Label for title
        name_title=Label(self.title_frame,text="Names",anchor=E)
        name_title.grid(row=0,column=0,ipadx=110)
        f_date_title = Label(self.title_frame, text="f_date",anchor=E)
        f_date_title.grid(row=0, column=1,ipadx=110)
        l_date_title = Label(self.title_frame, text="l_Date",anchor=E)
        l_date_title.grid(row=0, column=2,ipadx=160)

#######FRame for name and process bar

        self.name_frame=Frame(self,bg="blue",bd=5)
        self.name_frame.grid(row=1,column=0)
        self.processbar_frame=Frame(self,bg="brown",bd=5)
        self.processbar_frame.grid(row=1, column=1)
        self.test_button=Button(self,text="test it",command=self.add_func)
        self.test_button.grid(row=40,column=0,columnspan=2)
        self.test1_button = Button(self, text="Databese it", command=self.database_it)
        self.test1_button.grid(row=43, column=0, columnspan=2)
        self.test3_button = Button(self, text="time module check it", command=self.database_it)
        self.test3_button.grid(row=44, column=0, columnspan=2)

    def add_func(self):
        for i in range(len(info)):
            self.my_name = Label(self.name_frame, text=info[i][0]+">>>>>>>>")
            self.my_name.grid(row=i, column=0, ipadx=200,ipady=40)

            date_frame=Frame(self.processbar_frame,width=600,bg="grey")
            date_frame.pack()
            bar_frame=Frame(self.processbar_frame)
            bar_frame.pack()


            ############date for progress bar
            f_date = Label(date_frame, text=info[i][2],anchor=W,width=28,height=3)
            f_date.pack (side=LEFT)
            ############date for progress bar
            l_date = Label(date_frame, text=info[i][3],anchor=E,width=27)
            l_date.pack( side=RIGHT)

            ####### PRogress bar

            my_progress = ttk.Progressbar(bar_frame, orient=HORIZONTAL, length=400, mode="determinate")
            my_progress.pack(ipady=15,side=BOTTOM)
            #### progres bar value
            my_progress["value"] = int(info[i][1])

    def time_module(self,month1,day1,month2,day2):
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
        conn=sqlite3.connect("shred_life.db")

        c=conn.cursor()


        c.execute("SELECT * FROM shred_life")
        self.my_list=c.fetchall()
        for i in range(len(self.my_list)):
            self.my_name = Label(self.name_frame, text=self.my_list[i][0] + ">>>>>>>>")
            self.my_name.grid(row=i, column=0, ipadx=200, ipady=40)

            date_frame = Frame(self.processbar_frame, width=600, bg="grey")
            date_frame.pack()
            bar_frame = Frame(self.processbar_frame)
            bar_frame.pack()

            ############date for progress bar
            f_date = Label(date_frame, text=str(self.my_list[i][1])+"/"+str(self.my_list[i][2]), anchor=W, width=28, height=3)
            f_date.pack(side=LEFT)
            ############date for progress bar
            l_date = Label(date_frame, text=str(self.my_list[i][3])+"/"+str(self.my_list[i][4]), anchor=E, width=27)
            l_date.pack(side=RIGHT)

            ####### PRogress bar

            my_progress = ttk.Progressbar(bar_frame, orient=HORIZONTAL, length=400, mode="determinate")
            my_progress.pack(ipady=15, side=BOTTOM)
            #### progres bar value
            berge=self.time_module(self.my_list[i][1],self.my_list[i][2],self.my_list[i][3],self.my_list[i][4])
            my_progress["value"] = berge



        conn.commit()

        conn.close()

#







if __name__ == '__main__':
    de=se()
    de.title("Staying schedule")
    de.geometry("1000x600")
    de.mainloop()


#my_text=open("sample.txt","w")
#my_text.write("(ZAck berge,20),(Ukena Tora,20)")
#my_text.close()
#### GET info from    Txt file


