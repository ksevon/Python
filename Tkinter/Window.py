from tkinter import *
from tkinter import ttk

class Window:
    def __init__(self, color, title = "Окно", atrib = "-fullscreen", fal = False, tru = True):
        self.window = Tk()
        self.window.title(title)
        # self.window.geometry("1200x800")
        self.window.resizable(fal, fal)
        self.window.attributes(atrib, tru)
        self.window.config(bg=color)

        self.enable = IntVar()

        self.mass = []

    def Create_ttk_button(self, x_pos, y_posm, text):
        self.button = ttk.Button(text=text)
        self.button.place(x=x_pos, y=y_posm)

    def Create_button(self, x_pos, y_posm, text, command):
        self.button = Button(text=text, command=command)
        self.button.place(x=x_pos, y=y_posm)

    def Run_window(self):
        self.window.mainloop()

    def Close_window(self):
        self.window.destroy()

    def Create_check_button(self, x_pos, y_posm, text, command):
        self.checkbutton = Checkbutton(text=text, variable=self.enable, command=command)
        self.checkbutton.place(x=x_pos, y=y_posm)

    def Change_color(self):
        if self.enable.get() == 1:
            self.window.config(bg = 'Grey')
        else:
            self.window.config(bg = 'White')

start_window = Window("White")
start_window.Create_button(1900, 20, "X", start_window.Close_window)
start_window.Create_check_button(1800, 20, "Цвет", start_window.Change_color)

