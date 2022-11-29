import tkinter as tk
from tkinter import ttk


class App:

    def __init__(self, window):

        self.window = window

        self.welcomeFrame = Frame(window)

        self.welcomeFrame.pack()
        # configure the root window
        self.frame2 = Frame(self)
        self.frame2.title('My Awesome App')
        self.frame2.geometry('300x50')

        # label
        self.label = ttk.Label(self, text='Hello, Tkinter!')
        self.label.pack()

        # button
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()

    def button_clicked(self):
    
