from ctypes import alignment
from tkinter import *
from tkinter.ttk import Combobox
import mysql.connector

# Create a connection to the database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "zoodatabase"
)

mycursor = mydb.cursor()

def show_fundraiser(event):
    fundraiser = fundraiserSelection.get()
    fundraiserLabel.config(text="Fundraiser ID: " + fundraiser)

    mycursor.execute("SELECT Theme FROM Fundraiser WHERE FundraiserID = '%s'"%fundraiser)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    themeLabel.config(text="Theme: " + result)

def set_fundraisers_frame(sFrame):
    global fundraisersFrame
    fundraisersFrame = sFrame

    text = Label(fundraisersFrame, text="Browse fundraisers")
    text.grid(column = 1, row = 0, sticky=S, ipadx=300, ipady=20)
    global fundraiserSelection
    currValue = StringVar()
    fundraiserSelection = Combobox(fundraisersFrame, width = 30, textvariable = currValue)
    fundraiserSelection.grid(column = 1, row = 1, padx=300, pady=20, sticky=N+S+E+W)

    mycursor.execute("SELECT FundraiserID FROM Fundraiser")
    result = mycursor.fetchall()

    fundraiserSelection['values'] = result
    fundraiserSelection['state'] = 'readonly'

    fundraiserSelection.bind('<<ComboboxSelected>>', show_fundraiser)

    # Create text for fundraiser info
    global fundraiserLabel
    global themeLabel

    fundraiserLabel = Label(fundraisersFrame, text="Fundraiser ID: None selected")
    fundraiserLabel.grid(column = 1, row = 2, padx=300, pady=20, sticky=S+E+W)
    themeLabel = Label(fundraisersFrame, text="Theme: ")
    themeLabel.grid(column = 1, row = 3, padx=300, pady=20, sticky=N+S+E+W)
