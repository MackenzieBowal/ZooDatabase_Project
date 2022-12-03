from ctypes import alignment
from tkinter import *
from tkinter.ttk import Combobox

speciesData = [["Lion", "Feline", "Savannah", "12 years", "Diet"], 
                ["Buffalo", "Bovine", "Plains", "25 years", "Diet"], 
                ["Platypus", "Weird", "Small Creeks", "7 years", "Diet"]]

def showSpecies(event):
    spec = speciesSelection.get()

    # Replace this with querying the database
    for i in range(len(speciesData)):
        if (speciesData[i][0] == spec):
            spLabel.config(text="Species: " + spec)
            catLabel.config(text="Category: " + speciesData[i][1])
            habLabel.config(text="Habitat: " + speciesData[i][2])
            lifeLabel.config(text="Lifespan: " + speciesData[i][3])
            dietLabel.config(text="Diet: " + speciesData[i][4])
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

    # This will be replaced by querying the database
    sNames = []
    for i in range(len(speciesData)):
        sNames.append(speciesData[i][0])
    
    speciesNames = tuple(sNames)

    speciesSelection['values'] = speciesNames
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