import tkinter as tk
from tkinter import ttk
TK_SILENCE_DEPRECATION=1

class App:

    def __init__(self, window):

        self.window = window

        self.welcomeFrame = ttk.Frame(self.window)

        self.welcomeFrame.pack()
        self.welcomeFrame.place(window)

        # label
        self.empButton = ttk.Button(self.welcomeFrame, text='Employee')
        self.empButton.pack()
        self.visButton = ttk.Button(self.welcomeFrame, text='Visitor')
        self.visButton.pack()



        # button
        self.empButton['command'] = self.button_clicked

    def button_clicked(self):
        print("clicked!")

win = tk.Tk()
win.geometry("750x250")
myApp = App(win)