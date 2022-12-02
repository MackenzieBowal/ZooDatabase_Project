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

def show_exhibit(event):
    exhibit = exhibitSelection.get()
    print(exhibit)

    exhibitLabel.config(text="Exhibit ID: " + exhibit)
    mycursor.execute("SELECT Start_date FROM Exhibit WHERE ExhibitID = %s"%exhibit)
    result = mycursor.fetchall()
    startLabel.config(text="Start Date: " + str(result[0][0]))
    mycursor.execute("SELECT End_date FROM Exhibit WHERE ExhibitID = %s"%exhibit)
    result = mycursor.fetchall()
    endLabel.config(text="End Date: " + str(result[0][0]))

def set_exhibits_frame(eFrame):
    global exhibitsFrame
    exhibitsFrame = eFrame

    text = Label(exhibitsFrame, text="Browse Exhibits")
    text.grid(column = 1, row = 0, sticky=S, ipadx=300, ipady=20)
    global exhibitSelection
    currValue = StringVar()
    exhibitSelection = Combobox(exhibitsFrame, width = 30, textvariable = currValue)
    exhibitSelection.grid(column = 1, row = 1, padx=300, pady=20, sticky=N+S+E+W)

    mycursor.execute("SELECT ExhibitID FROM Exhibit")
    result = mycursor.fetchall()

    exhibitSelection['values'] = result
    exhibitSelection['state'] = 'readonly'

    exhibitSelection.bind('<<ComboboxSelected>>', show_exhibit)

    # Create text for exhibit info
    global exhibitLabel
    global startLabel
    global endLabel

    exhibitLabel = Label(exhibitsFrame, text="Exhibit: None selected")
    exhibitLabel.grid(column = 1, row = 2, padx=300, pady=20, sticky=S+E+W)
    startLabel = Label(exhibitsFrame, text="Start Date: ")
    startLabel.grid(column = 1, row = 3, padx=300, pady=20, sticky=N+S+E+W)
    endLabel = Label(exhibitsFrame, text="End Date: ")
    endLabel.grid(column = 1, row = 4, padx=300, pady=20, sticky=N+S+E+W)
