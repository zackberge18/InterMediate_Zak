from tkinter import *
import pygame
from tkinter import filedialog

class App(Tk):
    def __init__(self):
        super(App, self).__init__()
        self.my_button=Button(self,text="play",font="arial 20 bold",command=self.play)
        self.my_button.pack()
        pygame.mixer.init()

    def play(self):
        self.my_path=filedialog.askopenfilename()
        print(self.my_path)
        pygame.mixer.music.load(self.my_path)
        pygame.mixer.music.play(loops=0)

if __name__ == '__main__':
    app=App()
    app.mainloop()