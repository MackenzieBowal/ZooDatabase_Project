import tkinter as tk


class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.welcomePage = Frame(self, )

        self.submitButton = Button(self.buttonClick, text="Submit")
        self.submitButton.grid()


    def buttonClick(self, event):
        """ handle button click event and output text from entry area"""
        print("buttonclicked")
