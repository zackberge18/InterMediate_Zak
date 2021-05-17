"""

## uPPPER TO LOVER
import os


#
print(os.getcwd())
os.chdir("SILHO")
print(os.getcwd())
print(os.listdir())
for i in os.listdir():
    a=i.lower()
    os.rename(f"{i}",a)

#"""


#ALL PHOTO NAMES
#import os
#
#print(os.getcwd())
#os.chdir("SILHO/photo")
#print(os.getcwd())
#print(os.listdir())



####BOSLUK TO UNDERSCORE
#import os
#os.chdir("SILHO")
#for i in os.listdir():
#    a=i.replace(" ","_")

#    os.rename(f"{i}",a)
#
import binascii
#print("résumé".encode("utf-8"))
#b'r\xc3\xa9sum\xc3\xa9'
#print(chr(219))

""""
kurd_low="a b c ç d e ê f g h i î j k l m n o p q r s ş t u û v w x y z"
kurd_upper="A B C Ç D E Ê F G H I Î J K L M N O P Q R S Ş T U Û V W X Y Z"
turk_upper="A	B	C	Ç	D	E	F	G	Ğ	H	I	İ	J	K	L	M	N	O	Ö	P	R	S	Ş	T	U	Ü	V	Y	Z"
turk_lower="a	b	c	ç	d	e	f	g	ğ	h	ı	i	j	k	l	m	n	o	ö	p	r	s	ş	t	u	ü	v	y	z"
a=kurd_low.replace(" ","")
b=kurd_upper.replace(" ","")
c=turk_lower.replace(" ","")
d=turk_upper.replace(" ","")"""
allt="ÂâÇçÊêĞğİıÎîÖöŞşÛûÜü"


"""def translate(my_str):
        allt = "ÂâÇçÊêĞğİıÎîÖöŞşÛûÜü"
        a_2=my_str.replace("Â","A")
        a_2=a_2.replace("â","a")
        a_2=a_2.replace("Ç","C")
        a_2=a_2.replace("ç","c")
        a_2=a_2.replace("Ê","E")
        a_2=a_2.replace("ê","e")
        a_2=a_2.replace("Ğ","G")
        a_2=a_2.replace("ğ","g")
        a_2=a_2.replace("İ","I")
        a_2=a_2.replace("ı","i")
        a_2=a_2.replace("Î","I")
        a_2=a_2.replace("î","i")
        a_2=a_2.replace("Ö","O")
        a_2=a_2.replace("ö","o")
        a_2=a_2.replace("Ş","S")
        a_2=a_2.replace("ş","s")
        a_2=a_2.replace("Û","U")
        a_2=a_2.replace("û","u")
        a_2=a_2.replace("Ü","U")
        a_2=a_2.replace("ü","u")

        return a_2
"""

from tkinter import *
from tkinter import filedialog
import os

"""
my=filedialog.askdirectory()
print(my)
for dirpath,dirnames,filename in os.walk(f"{my}"):
        print("current path: ",dirpath)
        print("Directories: ", dirnames)
        print("Files : ", filename)
        print()"""

#for i in os.listdir("C:\Users\zackb\PycharmProjects\Ruken\silho"):
        #mi=str(i).split('.')
