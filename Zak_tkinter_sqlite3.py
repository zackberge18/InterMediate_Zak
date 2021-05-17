from tkinter import *

import sqlite3

root=Tk()

root.geometry("500x400")
#Database

#Create a database or connect to one
conn=sqlite3.connect("address_book.db")

#Create cursor
c=conn.cursor()

##Create TAble
#c.execute("""CREATE TABLE addresses(
#    first_name text,
#    last_name text,
#    address text,
#    city text,
#    state text,
#    zipcode integer)""")
#create save func


#CREATE EDIT FUNC
def edit():
    editor=Toplevel()
    editor.geometry("500x400")
    editor.title("update a record")
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # Create cursor
    c = conn.cursor()
    record_id=delete_box.get()
    # query database
    c.execute(f"SELECT * FROM addresses WHERE oid ={record_id}")
    records = c.fetchall()
    print(records)
    #print_records = ""


    # Create TExt box
    f_name_ed = Entry(editor, width=30)
    f_name_ed.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_ed = Entry(editor, width=30)
    l_name_ed.grid(row=1, column=1, padx=20)
    address_ed = Entry(editor, width=30)
    address_ed.grid(row=2, column=1, padx=20)
    city_ed = Entry(editor, width=30)
    city_ed.grid(row=3, column=1, padx=20)
    state_ed = Entry(editor, width=30)
    state_ed.grid(row=4, column=1, padx=20)
    zipcode_ed = Entry(editor, width=30)
    zipcode_ed.grid(row=5, column=1, padx=20)
    #
    for record in records:
       f_name_ed.insert(0,record[0])
       l_name_ed.insert(0, record[1])
       address_ed.insert(0, record[2])
       city_ed.insert(0, record[3])
       state_ed.insert(0, record[4])
       zipcode_ed.insert(0, record[5])
    # create TExt box label
    f_name_label = Label(editor, text="First name")
    f_name_label.grid(row=0, column=0)
    l_name_label = Label(editor, text="Last name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="city")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="state")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="zipcode", anchor=W)
    zipcode_label.grid(row=5, column=0)

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

    def save():
        # Create a database or connect to one
        conn = sqlite3.connect("address_book.db")

        # Create cursor
        c = conn.cursor()

        c.execute("""UPDATE addresses SET
         first_name=:first,
         last_name=:last,
         address=:address,
         city=:city,
         state=:state,
         zipcode=:zipcode

        WHERE oid=:oid """,
                  {
                      'first': f_name_ed.get(),
                      'last':l_name_ed.get(),
                      'address':address_ed.get(),
                      'city':city_ed.get(),
                      'state':state_ed.get(),
                      'zipcode':zipcode_ed.get(),
                      'oid':record_id

                  }

                  )

        # Commit changes
        conn.commit()
        # Close connection
        conn.close()
        # creeate an update button

    save_btn = Button(editor, text="SAVE button", command=save, anchor=N)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=105)


def delete():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # Create cursor
    c = conn.cursor()

    # Delete a erecord
    c.execute("DELETE from addresses WHERE oid="+delete_box.get())

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()


#Create submit function for datebase
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # Create cursor
    c = conn.cursor()


    #Inser into tabbles
    c.execute("INSERT INTO addresses VALUES (:f_name,:l_name,:address,:city,:state,:zipcode)",
              {
                  "f_name":f_name.get(),
                  "l_name":l_name.get(),
                  "address":address.get(),
                  "city":city.get(),
                  "state":state.get(),
                  "zipcode":zipcode.get()
              }

              )



    # Commit changes
    conn.commit()
    # Close connection
    conn.close()




    f_name.delete(0,END)
    l_name.delete(0, END)
    address.delete(0, END)
    state.delete(0, END)
    city.delete(0, END)
    zipcode.delete(0, END)

def query():
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")

    # Create cursor
    c = conn.cursor()


    #query database
    c.execute("SELECT *,oid FROM addresses")
    records=c.fetchall()
    print(records)
    print_records=""
    for record in records:
        print_records +=str(record[0])+"\t "+str(record[6])+ "\n"

    query_label=Label(root,text=print_records,bd=5,relief=GROOVE)
    query_label.grid(row=8,column=0,columnspan=2,ipadx=100)

    # Commit changes
    conn.commit()
    # Close connection
    conn.close()


#
#Create TExt box
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))
l_name=Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)
address=Entry(root,width=30)
address.grid(row=2,column=1,padx=20)
city=Entry(root,width=30)
city.grid(row=3,column=1,padx=20)
state=Entry(root,width=30)
state.grid(row=4,column=1,padx=20)
zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1,padx=20)
delete_box=Entry(root,width=30)
delete_box.grid(row=9,column=1,padx=20)

#

#
#create TExt box label
f_name_label=Label(root,text="First name")
f_name_label.grid(row=0,column=0)

l_name_label=Label(root,text="Last name")
l_name_label.grid(row=1,column=0)

address_label=Label(root,text="address")
address_label.grid(row=2,column=0)

city_label=Label(root,text="city")
city_label.grid(row=3,column=0)

state_label=Label(root,text="state")
state_label.grid(row=4,column=0)

zipcode_label=Label(root,text="zipcode",anchor=W)
zipcode_label.grid(row=5,column=0)

delete_box_label=Label(root,text="select")
delete_box_label.grid(row=9,column=0)



#Commit changes
conn.commit()

#creta Submit Button
submit_btn=Button(root,text=" Add REcord",command=submit,anchor=E)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10, ipadx=100)

#creeate a querry button
query_btn=Button(root,text="show record",command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#creeate a DELETE button
delete_btn=Button(root,text="DELETE button",command=delete,anchor=N)
delete_btn.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=95)

#creeate an update button

edit_btn=Button(root,text="EDIT button",command=edit,anchor=N)
edit_btn.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=105)



#Close connection
conn.close()


root.mainloop()