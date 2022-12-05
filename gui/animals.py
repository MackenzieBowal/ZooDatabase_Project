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
    if result == "None" or result == "0000000":
        exhibitLabel.config(text="Not currently shown at any exhibit")
    else:
        exhibitLabel.config(text="Currently being shown in exhibit " + result)



#################################################

def doneClick():
    for w in animalsFrame.winfo_children():
        w.destroy()
    set_animals_frame(animalsFrame)
    return

def deleteClick():
    delValue = cselectBox.get()
    mycursor.execute("DELETE FROM Animal WHERE Name='%s'", tuple(delValue))
    return

def delAnimal():
    # Refresh the page
    for w in animalsFrame.winfo_children():
        w.destroy()

    # create delete page
    cselectLabel = Label(animalsFrame,text="Select Animal: ")
    global cselectBox
    delValue = ""
    cselectBox = Combobox(animalsFrame, width = 30, textvariable = delValue)
    cselectLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    cselectBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)
    fselectButton = Button(animalsFrame, text="Delete", command=deleteClick)
    fselectButton.grid(row=1,column=2,stick=W)

    mycursor.execute("SELECT Name FROM Animal")
    result = mycursor.fetchall()

    cselectBox['values'] = result
    cselectBox['state'] = 'readonly'

    doneButton = Button(animalsFrame, text="Done", command=doneClick)
    doneButton.grid(row=2, columnspan=3)

    return


def modClick():
    originalid = modcselectBox.get()
    newid = modidBox.get()

    # Keep original values the same if not modified
    if newid == '':
        newid = originalid

    newenc = modeBox.get()
    if newenc == '':
        mycursor.execute("SELECT EnclosureID FROM Animal WHERE `Name`='%s'", (originalid,))
        newenc = str(mycursor.fetchall()[0][0])

    newex = modexBox.get()
    if newex == '':
        mycursor.execute("SELECT ExhibitID FROM Animal WHERE `Name`='%s'", (originalid,))
        newex = str(mycursor.fetchall()[0][0])

    # Update table
    try:
        if newex == 'None':
            mycursor.execute("UPDATE Animal SET \
                    Name='%s', EnclosureID='%s', ExhibitID='0000000' WHERE `Name`='%s'", (newid, newenc, originalid))
        else:
            mycursor.execute("UPDATE Animal SET \
                    Name='%s', EnclosureID='%s', ExhibitID='%s' WHERE `Name`='%s'", (newid, newenc, newex, originalid))
    except:
        showerror(title="Error", message="Invalid input. Please try again.")
    return

def modAnimal():
    for w in animalsFrame.winfo_children():
        w.destroy()

    # create delete page
    cselectLabel = Label(animalsFrame,text="Select Animal: ")
    global modcselectBox
    delValue = ""
    modcselectBox = Combobox(animalsFrame, width = 30, textvariable = delValue)
    cselectLabel.grid(row=0,column=0,sticky=E,padx=5,pady=10)
    modcselectBox.grid(row=0,column=1,sticky=E+W,padx=5,pady=10)

    mycursor.execute("SELECT Name FROM Animal")
    result = mycursor.fetchall()

    modcselectBox['values'] = result
    modcselectBox['state'] = 'readonly'

    # ID
    idLabel = Label(animalsFrame,text="Set Animal Name: ")
    global modidBox
    id = ""
    modidBox = Entry(animalsFrame, width = 30, textvariable = id)
    idLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    modidBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)

    # Enclosure
    eLabel = Label(animalsFrame,text="Set Enclosure: ")
    global modeBox
    enc = ""
    modeBox = Entry(animalsFrame, width = 30, textvariable = enc)
    eLabel.grid(row=5,column=0,sticky=E,padx=5,pady=10)
    modeBox.grid(row=5,column=1,sticky=E+W,padx=5,pady=10)

    # Exhibit
    exLabel = Label(animalsFrame,text="Set Exhibit (optional or \"None\"): ")
    global modexBox
    ex = ""
    modexBox = Entry(animalsFrame, width = 30, textvariable = ex)
    exLabel.grid(row=6,column=0,sticky=E,padx=5,pady=10)
    modexBox.grid(row=6,column=1,sticky=E+W,padx=5,pady=10)


    modButton = Button(animalsFrame, text="Update", command=modClick)
    modButton.grid(row=7,columnspan=2)

    doneButton = Button(animalsFrame, text="Done", command=doneClick)
    doneButton.grid(row=8,columnspan=2)

    return


def addClick():
    eid = idBox.get()
    bdate = bBox.get()
    sex = sBox.get()
    species = spBox.get()
    enc = eBox.get()

    # Set to empty exhibit
    if enc == '':
        enc = "0000000"

    try:
        mycursor.execute("INSERT INTO Animal \
            VALUES ('%s', '%s', '%s', '%s', '%s', NULL)", (eid, bdate, sex, species, enc))
    except:
        showerror(title="Error", message="Invalid input. Please try again.")
    return

def addAnimal():
    for w in animalsFrame.winfo_children():
        w.destroy()

    # ID
    idLabel = Label(animalsFrame,text="Animal Name: ")
    global idBox
    id = ""
    idBox = Entry(animalsFrame, width = 30, textvariable = id)
    idLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    idBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)

    # Birthdate
    bLabel = Label(animalsFrame,text="Birthdate (yyyy-mm-dd): ")
    global bBox
    bdate = ""
    bBox = Entry(animalsFrame, width = 30, textvariable = bdate)
    bLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
    bBox.grid(row=2,column=1,sticky=E+W,padx=5,pady=10)

    # Sex
    sLabel = Label(animalsFrame,text="Sex (M/F): ")
    global sBox
    sex = ""
    sBox = Entry(animalsFrame, width = 30, textvariable = sex)
    sLabel.grid(row=3,column=0,sticky=E,padx=5,pady=10)
    sBox.grid(row=3,column=1,sticky=E+W,padx=5,pady=10)

    # Species
    spLabel = Label(animalsFrame,text="Species: ")
    global spBox
    sp = ""
    spBox = Entry(animalsFrame, width = 30, textvariable = sp)
    spLabel.grid(row=4,column=0,sticky=E,padx=5,pady=10)
    spBox.grid(row=4,column=1,sticky=E+W,padx=5,pady=10)

    # Enclosure
    eLabel = Label(animalsFrame,text="Enclosure: ")
    global eBox
    enc = ""
    eBox = Entry(animalsFrame, width = 30, textvariable = enc)
    eLabel.grid(row=5,column=0,sticky=E,padx=5,pady=10)
    eBox.grid(row=5,column=1,sticky=E+W,padx=5,pady=10)


    addButton = Button(animalsFrame, text="Add", command=addClick)
    addButton.grid(row=6,columnspan=2)

    doneButton = Button(animalsFrame, text="Done", command=doneClick)
    doneButton.grid(row=7, columnspan=2)

    return

#################################################



def set_animals_frame(sFrame):
    global animalsFrame
    animalsFrame = sFrame

    delB = Button(animalsFrame,text="Delete an Animal",command=delAnimal)
    delB.grid(column = 0, row = 0, padx=5, pady=5, sticky=N+W)
    modB = Button(animalsFrame,text="Modify an Animal",command=modAnimal)
    modB.grid(column = 0, row = 1, padx=5, pady=5, sticky=N+W)
    addB = Button(animalsFrame,text="Add an Animal",command=addAnimal)
    addB.grid(column = 0, row = 2, padx=5, pady=5, sticky=N+W)

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
