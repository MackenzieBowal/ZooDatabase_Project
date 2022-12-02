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

def show_pass(event):
    passid = passSelection.get()
    passLabel.config(text="Pass ID: " + passid)

    mycursor.execute("SELECT Sold_price FROM Pass WHERE PassID = '%s'"%passid)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    priceLabel.config(text="Price: " + result)

    mycursor.execute("SELECT Date_issued FROM Pass WHERE PassID = '%s'"%passid)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    dateLabel.config(text="Date Issued: " + result)

    mycursor.execute("SELECT Receptionist_EID FROM Pass WHERE PassID = '%s'"%passid)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    receptionistLabel.config(text="Issued by: " + result)

def set_passes_frame(sFrame):
    global passesFrame
    passesFrame = sFrame

    text = Label(passesFrame, text="Browse passes")
    text.grid(column = 1, row = 0, sticky=S, ipadx=300, ipady=20)
    global passSelection
    currValue = StringVar()
    passSelection = Combobox(passesFrame, width = 30, textvariable = currValue)
    passSelection.grid(column = 1, row = 1, padx=300, pady=20, sticky=N+S+E+W)

    mycursor.execute("SELECT PassID FROM Pass")
    result = mycursor.fetchall()

    passSelection['values'] = result
    passSelection['state'] = 'readonly'

    passSelection.bind('<<ComboboxSelected>>', show_pass)

    # Create text for pass info
    global passLabel
    global priceLabel
    global dateLabel
    global receptionistLabel

    passLabel = Label(passesFrame, text="Pass ID: None selected")
    passLabel.grid(column = 1, row = 2, padx=300, pady=20, sticky=S+E+W)
    priceLabel = Label(passesFrame, text="Price: ")
    priceLabel.grid(column = 1, row = 3, padx=300, pady=20, sticky=N+S+E+W)
    dateLabel = Label(passesFrame, text="Date Issued: ")
    dateLabel.grid(column = 1, row = 4, padx=300, pady=20, sticky=N+S+E+W)
    receptionistLabel = Label(passesFrame, text="Issued by: ")
    receptionistLabel.grid(column = 1, row = 5, padx=300, pady=20, sticky=N+S+E+W)
