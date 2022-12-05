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

def show_animal(event):
    animal = animalSelection.get()
    animalLabel.config(text="Name: " + animal)

    mycursor.execute("SELECT Birth_date FROM Animal WHERE Name = '%s'"%animal)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    birthdateLabel.config(text="Birth Date: " + result)

    mycursor.execute("SELECT Sex FROM Animal WHERE Name = '%s'"%animal)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    sexLabel.config(text="Sex: " + result)

    mycursor.execute("SELECT Species_name FROM Animal WHERE Name = '%s'"%animal)
    result = str(mycursor.fetchall()[0][0])
    speciesLabel.config(text="Species: " + result)

    mycursor.execute("SELECT EnclosureID FROM Animal WHERE Name = '%s'"%animal)
    result = str(mycursor.fetchall()[0][0])
    enclosureLabel.config(text="In Enclosure: " + result)

    mycursor.execute("SELECT ExhibitID FROM Animal WHERE Name = '%s'"%animal)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    exhibitLabel.config(text="Currently being shown in exhibit " + result)

def set_animals_frame(sFrame):
    global animalsFrame
    animalsFrame = sFrame

    text = Label(animalsFrame, text="Browse animals")
    text.grid(column = 1, row = 0, sticky=S, ipadx=300, ipady=20)
    global animalSelection
    currValue = StringVar()
    animalSelection = Combobox(animalsFrame, width = 30, textvariable = currValue)
    animalSelection.grid(column = 1, row = 1, padx=300, pady=20, sticky=N+S+E+W)

    mycursor.execute("SELECT Name FROM Animal")
    result = mycursor.fetchall()

    animalSelection['values'] = result
    animalSelection['state'] = 'readonly'

    animalSelection.bind('<<ComboboxSelected>>', show_animal)

    # Create text for animal info
    global animalLabel
    global birthdateLabel
    global sexLabel
    global speciesLabel
    global enclosureLabel
    global exhibitLabel

    animalLabel = Label(animalsFrame, text="Name: None selected")
    animalLabel.grid(column = 1, row = 2, padx=300, pady=20, sticky=S+E+W)
    birthdateLabel = Label(animalsFrame, text="Birth Date: ")
    birthdateLabel.grid(column = 1, row = 3, padx=300, pady=20, sticky=N+S+E+W)
    sexLabel = Label(animalsFrame, text="Sex: ")
    sexLabel.grid(column = 1, row = 4, padx=300, pady=20, sticky=N+S+E+W)
    speciesLabel = Label(animalsFrame, text="Species: ")
    speciesLabel.grid(column = 1, row = 5, padx=300, pady=20, sticky=N+S+E+W)
    enclosureLabel = Label(animalsFrame, text="In Enclosure: ")
    enclosureLabel.grid(column = 1, row = 6, padx=300, pady=20, sticky=N+S+E+W)
    exhibitLabel = Label(animalsFrame, text="Currently being shown in exhibit ")
    exhibitLabel.grid(column = 1, row = 6, padx=300, pady=20, sticky=N+S+E+W)
