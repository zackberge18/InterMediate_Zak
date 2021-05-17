from tkinter import *

import random

class App(Tk):

    def __init__(self):
        super(App, self).__init__()
        self.geometry("500x500")



        ####CReate OUr Menu
        self.my_menu=Menu(self)
        self.config(menu=self.my_menu)

        #### Create menu item
        self.states_menu=Menu(self.my_menu)
        self.my_menu.add_cascade(label="GEoGrapy",menu=self.states_menu)
        self.states_menu.add_command(label='StaTes',command=self.states)
        self.states_menu.add_command(label='CApital', command=self.capitals)
        self.states_menu.add_separator()
        self.states_menu.add_command(label="Exit",command=self.quit)


    def states(self):
        try :
            self.state_frame.destroy()
        except:
            pass

        self.state_frame = Frame(self, width=500, height=500,bg="blue")
        self.state_frame.pack(fill=BOTH,expand=1)
        # Create list of images
        # Create a list of name
        self.naru = ['boruto', 'isshiki', 'kakashi', 'kawaki', 'koji', 'naruto', 'sasuke']
        # GEnerate a random number
        self.rando = random.randint(0, len(self.naru) - 1)

        self.anime_img = ImageTk.PhotoImage(Image.open(f"char_naruto/{self.naru[self.rando]}.png"))
        self.show_anime = Label(self.state_frame, image=self.anime_img)
        self.show_anime.pack(pady=(100,20))
        self.e=Entry(self.state_frame,width=40, font="arial 20 bold")
        self.e.pack(pady=10)
        self.check_button=Button(self.state_frame,text="Submit answer",command=self.check)
        self.check_button.pack()

    def check(self):
        if str(self.e.get())==self.naru[self.rando]:
            print("yay")
            self.states()
        else:
            print("try again later")

    def capitals(self):
        ###cREate our Frames

        self.states_capitals_frame = Frame(self, width=500, height=500,bg="red")
        self.states_capitals_frame.pack(fill=BOTH,expand=1)
        self.my_label = Label(self.states_capitals_frame, text="char-Anime").pack()


        self.anime_states = ['boruto', 'blackclover', 'dragonball', 'dragonball', 'fullmetal', 'naruto', 'bleach']

        self.our_anime_capitals = {

            'kawaki': 'boruto',
            'asta': 'blackclover',
            'goku': 'dragonball',
            'vegeta': 'dragonball',
            'edward': 'fullmetal',
            'sasuke': 'naruto',
            'ichigo': 'bleach'
        }
        Label(self.states_capitals_frame,text=self.choices()[0]).pack()


        try :
            self.state_frame.forget()
            self.states_capitals_frame.forget()
        except:
            pass

    def choices(self):
        self.answer_list = []
        for i in range(3):
            rand_num = random.randint(0, len(self.anime_states) - 1)
            if i == 0:
                answer = self.anime_states[rand_num]
            self.answer_list.append(self.anime_states[rand_num])
            self.anime_states.remove(self.anime_states[rand_num])
        return  self.answer_list


if __name__ == '__main__':
    app=App()
    app.mainloop()