from ctypes import alignment
from tkinter import *
from tkinter.messagebox import showerror
from tkinter.ttk import Combobox
import mysql.connector

# Create a connection to the database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "zoodatabase",
    autocommit = True
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


#################################################

def doneClick():
    for w in speciesFrame.winfo_children():
        w.destroy()
    setSpeciesFrame(speciesFrame, True)
    return

def deleteClick():
    delValue = cselectBox.get()
    mycursor.execute("DELETE FROM Species WHERE Species_name='" + delValue + "'")
    return

def delSpecies():
    # Refresh the page
    for w in speciesFrame.winfo_children():
        w.destroy()

    # create delete page
    cselectLabel = Label(speciesFrame,text="Select Species: ")
    global cselectBox
    delValue = ""
    cselectBox = Combobox(speciesFrame, width = 30, textvariable = delValue)
    cselectLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    cselectBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)
    fselectButton = Button(speciesFrame, text="Delete", command=deleteClick)
    fselectButton.grid(row=1,column=2,stick=W)

    mycursor.execute("SELECT Species_name FROM Species")
    result = mycursor.fetchall()

    cselectBox['values'] = result
    cselectBox['state'] = 'readonly'

    doneButton = Button(speciesFrame, text="Done", command=doneClick)
    doneButton.grid(row=2, columnspan=3)

    return


def modClick():
    originalid = modEselectBox.get()
    newid = modidBox.get()

    # Keep original values the same if not modified
    if newid == '':
        newid = originalid

    newcat = modcBox.get()
    if newcat == '':
        mycursor.execute("SELECT Category FROM Species WHERE `Species_name`='"+originalid+"'")
        newcat = str(mycursor.fetchall()[0][0])

    newhab = modhBox.get()
    if newhab == '':
        mycursor.execute("SELECT Habitat FROM Species WHERE `Species_name`='"+originalid+"'")
        newhab = str(mycursor.fetchall()[0][0])

    newlife = modlBox.get()
    if newlife == '':
        mycursor.execute("SELECT Lifespan FROM Species WHERE `Species_name`='"+originalid+"'")
        newlife = str(mycursor.fetchall()[0][0])

    newdiet = moddBox.get()
    if newdiet == '':
        mycursor.execute("SELECT Diet FROM Species WHERE `Species_name`='"+originalid+"'")
        newdiet = str(mycursor.fetchall()[0][0])

    # Update table
    try:
        mycursor.execute("UPDATE Species SET \
                Species_name='"+newid+"', Category='"+newcat+"', Habitat='"+newhab+"', \
                Lifespan='"+newlife+"', Diet='"+newdiet+"' WHERE `Species_name`='"+originalid+"'")
    except:
        showerror(title="Error", message="Invalid input. Please try again.")
    return

def modSpecies():
    for w in speciesFrame.winfo_children():
        w.destroy()

    # create modify page
    cselectLabel = Label(speciesFrame,text="Select Species: ")
    global modEselectBox
    modValue = ""
    modEselectBox = Combobox(speciesFrame, width = 30, textvariable = modValue)
    cselectLabel.grid(row=0,column=0,sticky=E,padx=5,pady=10)
    modEselectBox.grid(row=0,column=1,sticky=E+W,padx=5,pady=10)

    mycursor.execute("SELECT Species_name FROM Species")
    result = mycursor.fetchall()

    modEselectBox['values'] = result
    modEselectBox['state'] = 'readonly'

    # ID
    idLabel = Label(speciesFrame,text="Set Species Name: ")
    global modidBox
    id = ""
    modidBox = Entry(speciesFrame, width = 30, textvariable = id)
    idLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    modidBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)

    # Category
    cLabel = Label(speciesFrame,text="Set Category: ")
    global modcBox
    cat = ""
    modcBox = Entry(speciesFrame, width = 30, textvariable = cat)
    cLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
    modcBox.grid(row=2,column=1,sticky=E+W,padx=5,pady=10)

    # Habitat
    hLabel = Label(speciesFrame,text="Set Habitat: ")
    global modhBox
    hab = ""
    modhBox = Entry(speciesFrame, width = 30, textvariable = hab)
    hLabel.grid(row=3,column=0,sticky=E,padx=5,pady=10)
    modhBox.grid(row=3,column=1,sticky=E+W,padx=5,pady=10)

    # Lifespan
    lLabel = Label(speciesFrame,text="Set Lifespan: ")
    global modlBox
    life = ""
    modlBox = Entry(speciesFrame, width = 30, textvariable = life)
    lLabel.grid(row=4,column=0,sticky=E,padx=5,pady=10)
    modlBox.grid(row=4,column=1,sticky=E+W,padx=5,pady=10)

    # Diet
    dLabel = Label(speciesFrame,text="Set Diet: ")
    global moddBox
    die = ""
    moddBox = Entry(speciesFrame, width = 30, textvariable = die)
    dLabel.grid(row=5,column=0,sticky=E,padx=5,pady=10)
    moddBox.grid(row=5,column=1,sticky=E+W,padx=5,pady=10)

    modButton = Button(speciesFrame, text="Update", command=modClick)
    modButton.grid(row=7,columnspan=2)

    doneButton = Button(speciesFrame, text="Done", command=doneClick)
    doneButton.grid(row=8,columnspan=2)

    return


def addClick():
    eid = idBox.get()
    cat = cBox.get()
    hab = hBox.get()
    life = lBox.get()
    diet = dBox.get()

    try:
        mycursor.execute("INSERT INTO Species \
            VALUES ('"+eid+"', '"+cat+"', '"+hab+"', '"+life+"', '"+diet+"')")
    except:
        showerror(title="Error", message="Invalid input. Please try again.")
    return

def addSpecies():
    for w in speciesFrame.winfo_children():
        w.destroy()

    # ID
    idLabel = Label(speciesFrame,text="Species Name: ")
    global idBox
    id = ""
    idBox = Entry(speciesFrame, width = 30, textvariable = id)
    idLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    idBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)

    # Category
    cLabel = Label(speciesFrame,text="Category: ")
    global cBox
    cat = ""
    cBox = Entry(speciesFrame, width = 30, textvariable = cat)
    cLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
    cBox.grid(row=2,column=1,sticky=E+W,padx=5,pady=10)

    # Habitat
    hLabel = Label(speciesFrame,text="Habitat: ")
    global hBox
    hab = ""
    hBox = Entry(speciesFrame, width = 30, textvariable = hab)
    hLabel.grid(row=3,column=0,sticky=E,padx=5,pady=10)
    hBox.grid(row=3,column=1,sticky=E+W,padx=5,pady=10)

    # Lifespan
    lLabel = Label(speciesFrame,text="Lifespan: ")
    global lBox
    life = ""
    lBox = Entry(speciesFrame, width = 30, textvariable = life)
    lLabel.grid(row=4,column=0,sticky=E,padx=5,pady=10)
    lBox.grid(row=4,column=1,sticky=E+W,padx=5,pady=10)

    # Diet
    dLabel = Label(speciesFrame,text="Diet: ")
    global dBox
    die = ""
    dBox = Entry(speciesFrame, width = 30, textvariable = die)
    dLabel.grid(row=5,column=0,sticky=E,padx=5,pady=10)
    dBox.grid(row=5,column=1,sticky=E+W,padx=5,pady=10)

    addButton = Button(speciesFrame, text="Add", command=addClick)
    addButton.grid(row=6,columnspan=2)

    doneButton = Button(speciesFrame, text="Done", command=doneClick)
    doneButton.grid(row=7, columnspan=2)

    return

#################################################


def setSpeciesFrame(sFrame, e):

    global speciesFrame
    speciesFrame = sFrame

    global editable
    editable = e

    if editable:
        delB = Button(speciesFrame,text="Delete a Species",command=delSpecies)
        delB.grid(column = 0, row = 0, padx=5, pady=5, sticky=N+W)
        modB = Button(speciesFrame,text="Modify a Species",command=modSpecies)
        modB.grid(column = 0, row = 1, padx=5, pady=5, sticky=N+W)
        addB = Button(speciesFrame,text="Add a Species",command=addSpecies)
        addB.grid(column = 0, row = 2, padx=5, pady=5, sticky=N+W)


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