condition=False
x=1 if condition else 0
print(x)



num=123_432_234

print(f'{num:,}')

#with open('delete_it.txt','w') as f:
#    pass

names=['der','asdf','asd']
for index,name in enumerate(names,start=1):
    print(index,name)

names=['peter','clark','wade']
heroes=['spi','sup','dead']

for index,name in enumerate(names):
    hero=heroes[index]
    print(f"{name} is actuaclly {hero}")

for name,hero in zip(names,heroes):
    print(f"{name} is actuaclly {hero}")
    a=zip(names,heroes)
    print(a)
    for i in a:
        print(i)


a,b=1,2
c,_=(3,5)
print(a,b,c)


print(dir(print))


nums=[11,23,44,56]
for num in nums:
    square=num**2
    print(square)

"""
from tkinter import *

root=Tk()
root.geometry("500x500")
label=Label(root,text="fuck you",wraplength=5,bg="red",bd=5)
label.pack()
root.mainloop()"""