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

def show_enclosure(event):
    enclosure = enclosureSelection.get()
    enclosureLabel.config(text="Enclosure ID: " + enclosure)

    mycursor.execute("SELECT Temperature FROM Enclosure WHERE EnclosureID = '%s'"%enclosure)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    temperatureLabel.config(text="Temperature: " + result + "°C")

    mycursor.execute("SELECT Habitat FROM Enclosure WHERE EnclosureID = '%s'"%enclosure)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    habitatLabel.config(text="Habitat: " + result)

    mycursor.execute("SELECT Length FROM Enclosure WHERE EnclosureID = '%s'"%enclosure)
    length = str(mycursor.fetchall()[0][0])
    if length == "None":
        length = "N/A"
    mycursor.execute("SELECT Width FROM Enclosure WHERE EnclosureID = '%s'"%enclosure)
    width = str(mycursor.fetchall()[0][0])
    if width == "None":
        width = "N/A"
    mycursor.execute("SELECT Height FROM Enclosure WHERE EnclosureID = '%s'"%enclosure)
    height = str(mycursor.fetchall()[0][0])
    if height == "None":
        height = "N/A"
    dimensionsLabel.config(text="Dimensions: %s x %s x %s"%(length,width,height))

    mycursor.execute("SELECT ComplexID FROM Enclosure WHERE EnclosureID = '%s'"%enclosure)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    complexLabel.config(text="In Indoor Complex %s"%result)

def set_enclosures_frame(sFrame):
    global enclosuresFrame
    enclosuresFrame = sFrame

    text = Label(enclosuresFrame, text="Browse enclosures")
    text.grid(column = 1, row = 0, sticky=S, ipadx=300, ipady=20)
    global enclosureSelection
    currValue = StringVar()
    enclosureSelection = Combobox(enclosuresFrame, width = 30, textvariable = currValue)
    enclosureSelection.grid(column = 1, row = 1, padx=300, pady=20, sticky=N+S+E+W)

    mycursor.execute("SELECT EnclosureID FROM Enclosure")
    result = mycursor.fetchall()

    enclosureSelection['values'] = result
    enclosureSelection['state'] = 'readonly'

    enclosureSelection.bind('<<ComboboxSelected>>', show_enclosure)

    # Create text for enclosure info
    global enclosureLabel
    global temperatureLabel
    global habitatLabel
    global dimensionsLabel
    global complexLabel

    enclosureLabel = Label(enclosuresFrame, text="Enclosure ID: None selected")
    enclosureLabel.grid(column = 1, row = 2, padx=300, pady=20, sticky=S+E+W)
    temperatureLabel = Label(enclosuresFrame, text="Temperature: ")
    temperatureLabel.grid(column = 1, row = 3, padx=300, pady=20, sticky=N+S+E+W)
    habitatLabel = Label(enclosuresFrame, text="Habitat: ")
    habitatLabel.grid(column = 1, row = 4, padx=300, pady=20, sticky=N+S+E+W)
    dimensionsLabel = Label(enclosuresFrame, text="Dimensions: ")
    dimensionsLabel.grid(column = 1, row = 5, padx=300, pady=20, sticky=N+S+E+W)
    complexLabel = Label(enclosuresFrame, text="In Indoor Complex: ")
    complexLabel.grid(column = 1, row = 6, padx=300, pady=20, sticky=N+S+E+W)
