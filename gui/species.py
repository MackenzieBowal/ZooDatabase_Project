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


def showSpecies(event):
    spec = speciesSelection.get()

    spLabel.config(text="Species: "+ spec)

    mycursor.execute("SELECT Category FROM Species WHERE Species_name = '%s'"%spec)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    catLabel.config(text="Category: " + result)

    mycursor.execute("SELECT Habitat FROM Species WHERE Species_name = '%s'"%spec)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    habLabel.config(text="Habitat: " + result)

    mycursor.execute("SELECT Lifespan FROM Species WHERE Species_name = '%s'"%spec)
    result = str(mycursor.fetchall()[0][0])
    lifeLabel.config(text="Lifespan: " + result)

    mycursor.execute("SELECT Diet FROM Species WHERE Species_name = '%s'"%spec)
    result = str(mycursor.fetchall()[0][0])
    dietLabel.config(text="Diet: " + result)

    return

def setSpeciesFrame(sFrame):

    global speciesFrame
    speciesFrame = sFrame

    text = Label(speciesFrame, text="Browse Species")
    text.grid(column = 1, row = 0, sticky=S, ipadx=300, ipady=20)
    global speciesSelection
    currValue = StringVar()
    speciesSelection = Combobox(speciesFrame, width = 30, textvariable = currValue)
    speciesSelection.grid(column = 1, row = 1, padx=300, pady=20, sticky=N+S+E+W)
    
    mycursor.execute("SELECT Species_name FROM Species")
    result = mycursor.fetchall()

    speciesSelection['values'] = result
    speciesSelection['state'] = 'readonly'

    speciesSelection.bind('<<ComboboxSelected>>', showSpecies)

    # Create text for species info
    global spLabel
    global catLabel
    global habLabel
    global lifeLabel
    global dietLabel

    spLabel = Label(speciesFrame, text="Species: None selected")
    spLabel.grid(column = 1, row = 2, padx=300, pady=20, sticky=S+E+W)
    catLabel = Label(speciesFrame, text="Category: ")
    catLabel.grid(column = 1, row = 3, padx=300, pady=20, sticky=N+S+E+W)
    habLabel = Label(speciesFrame, text="Habitat: ")
    habLabel.grid(column = 1, row = 4, padx=300, pady=20, sticky=N+S+E+W)
    lifeLabel = Label(speciesFrame, text="Lifespan: ")
    lifeLabel.grid(column = 1, row = 5, padx=300, pady=20, sticky=N+S+E+W)
    dietLabel = Label(speciesFrame, text="Diet: ")
    dietLabel.grid(column = 1, row = 6, padx=300, pady=20, sticky=N+S+E+W)

    return