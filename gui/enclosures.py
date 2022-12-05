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

mycursor = mydb.cursor(prepared=True)

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

#################################################

def doneClick():
    for w in enclosuresFrame.winfo_children():
        w.destroy()
    set_enclosures_frame(enclosuresFrame, True)
    return

def deleteClick():
    delValue = eselectBox.get()
    mycursor.execute("DELETE FROM Enclosure WHERE EnclosureID=" + delValue)
    return

def delEnclosure():
    # Refresh the page
    for w in enclosuresFrame.winfo_children():
        w.destroy()

    # create delete page
    eselectLabel = Label(enclosuresFrame,text="Select Enclosure: ")
    global eselectBox
    delValue = ""
    eselectBox = Combobox(enclosuresFrame, width = 30, textvariable = delValue)
    eselectLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    eselectBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)
    fselectButton = Button(enclosuresFrame, text="Delete", command=deleteClick)
    fselectButton.grid(row=1,column=2,stick=W)

    mycursor.execute("SELECT EnclosureID FROM Enclosure")
    result = mycursor.fetchall()

    eselectBox['values'] = result
    eselectBox['state'] = 'readonly'

    doneButton = Button(enclosuresFrame, text="Done", command=doneClick)
    doneButton.grid(row=2, columnspan=3)

    return


def modClick():
    originalid = modEselectBox.get()
    newid = modidBox.get()

    # Keep original values the same if not modified
    if newid == '':
        newid = originalid

    newtemp = modtempBox.get()
    if newtemp == '':
        mycursor.execute("SELECT Temperature FROM Enclosure WHERE EnclosureID="+originalid)
        newtemp = str(mycursor.fetchall()[0][0])

    newhab = modhabBox.get()
    if newhab == '':
        mycursor.execute("SELECT Habitat FROM Enclosure WHERE EnclosureID="+originalid)
        newhab = str(mycursor.fetchall()[0][0])

    newlen = modlenBox.get()
    if newlen == '':
        mycursor.execute("SELECT Length FROM Enclosure WHERE EnclosureID="+originalid)
        newlen = str(mycursor.fetchall()[0][0])
    
    newwid = modwidBox.get()
    if newwid == '':
        mycursor.execute("SELECT Width FROM Enclosure WHERE EnclosureID="+originalid)
        newwid = str(mycursor.fetchall()[0][0])

    newheight = modheightBox.get()
    if newheight == '':
        mycursor.execute("SELECT Height FROM Enclosure WHERE EnclosureID="+originalid)
        newheight = str(mycursor.fetchall()[0][0])

    newcomp = modcompBox.get()
    if newcomp == '':
        mycursor.execute("SELECT ComplexID FROM Enclosure WHERE EnclosureID="+originalid)
        newcomp = str(mycursor.fetchall()[0][0])

    # Update table
    try:
        sql_update_query = """UPDATE Enclosure SET EnclosureID=%s, Temperature=%s, Habitat=%s, Length=%s, Width=%s, Height=%s, ComplexID=%s WHERE EnclosureID=%s"""
        data_tuple = (newid,newtemp,newhab,newlen,newwid,newheight,newcomp,originalid)
        mycursor.execute(sql_update_query, data_tuple)
    except:
        showerror(title="Error", message="Invalid input. Please try again.")
    return

def modEnclosure():
    for w in enclosuresFrame.winfo_children():
        w.destroy()


    # create modification page
    eselectLabel = Label(enclosuresFrame,text="Select Enclosure: ")
    global modEselectBox
    delValue = ""
    modEselectBox = Combobox(enclosuresFrame, width = 30, textvariable = delValue)
    eselectLabel.grid(row=0,column=0,sticky=E,padx=5,pady=10)
    modEselectBox.grid(row=0,column=1,sticky=E+W,padx=5,pady=10)

    mycursor.execute("SELECT EnclosureID FROM Enclosure")
    result = mycursor.fetchall()

    modEselectBox['values'] = result
    modEselectBox['state'] = 'readonly'

    # ID
    idLabel = Label(enclosuresFrame,text="Set EnclosureID: ")
    global modidBox
    id = ""
    modidBox = Entry(enclosuresFrame, width = 30, textvariable = id)
    idLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    modidBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)

    # Temp
    tempLabel = Label(enclosuresFrame,text="Set Temperature: ")
    global modtempBox
    temp = ""
    modtempBox = Entry(enclosuresFrame, width = 30, textvariable = temp)
    tempLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
    modtempBox.grid(row=2,column=1,sticky=E+W,padx=5,pady=10)

    # Habitat
    habLabel = Label(enclosuresFrame,text="Set Habitat: ")
    global modhabBox
    hab = ""
    modhabBox = Entry(enclosuresFrame, width = 30, textvariable = hab)
    habLabel.grid(row=3,column=0,sticky=E,padx=5,pady=10)
    modhabBox.grid(row=3,column=1,sticky=E+W,padx=5,pady=10)

    # Length
    lenLabel = Label(enclosuresFrame,text="Set Length: ")
    global modlenBox
    length = ""
    modlenBox = Entry(enclosuresFrame, width = 30, textvariable = length)
    lenLabel.grid(row=4,column=0,sticky=E,padx=5,pady=10)
    modlenBox.grid(row=4,column=1,sticky=E+W,padx=5,pady=10)

    # Width
    widLabel = Label(enclosuresFrame,text="Set Width: ")
    global modwidBox
    wid = ""
    modwidBox = Entry(enclosuresFrame, width = 30, textvariable = wid)
    widLabel.grid(row=5,column=0,sticky=E,padx=5,pady=10)
    modwidBox.grid(row=5,column=1,sticky=E+W,padx=5,pady=10)

    # Height
    heightLabel = Label(enclosuresFrame,text="Set Height: ")
    global modheightBox
    height = ""
    modheightBox = Entry(enclosuresFrame, width = 30, textvariable = height)
    heightLabel.grid(row=6,column=0,sticky=E,padx=5,pady=10)
    modheightBox.grid(row=6,column=1,sticky=E+W,padx=5,pady=10)

    # Complex
    compLabel = Label(enclosuresFrame,text="Set ComplexID: ")
    global modcompBox
    comp = ""
    modcompBox = Entry(enclosuresFrame, width = 30, textvariable = comp)
    compLabel.grid(row=7,column=0,sticky=E,padx=5,pady=10)
    modcompBox.grid(row=7,column=1,sticky=E+W,padx=5,pady=10)


    modButton = Button(enclosuresFrame, text="Update", command=modClick)
    modButton.grid(row=8,columnspan=2)

    doneButton = Button(enclosuresFrame, text="Done", command=doneClick)
    doneButton.grid(row=9,columnspan=2)

    return


def addClick():
    eid = idBox.get()
    temp = tempBox.get()
    hab = habBox.get()
    length = lenBox.get()
    width = widBox.get()
    height = heightBox.get()
    comp = compBox.get()

    try:
        sql_insert_query = """INSERT INTO Enclosure VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        data_tuple = (eid,temp,hab,length,width,height,comp)
        mycursor.execute(sql_insert_query, data_tuple)
    except:
        showerror(title="Error", message="Invalid input. Please try again.")
    return

def addEnclosure():
    for w in enclosuresFrame.winfo_children():
        w.destroy()

    # ID
    idLabel = Label(enclosuresFrame,text="EnclosureID: ")
    global idBox
    id = ""
    idBox = Entry(enclosuresFrame, width = 30, textvariable = id)
    idLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    idBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)

    # Temp
    tempLabel = Label(enclosuresFrame,text="Temperature: ")
    global tempBox
    temp = ""
    tempBox = Entry(enclosuresFrame, width = 30, textvariable = temp)
    tempLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
    tempBox.grid(row=2,column=1,sticky=E+W,padx=5,pady=10)

    # Habitat
    habLabel = Label(enclosuresFrame,text="Habitat: ")
    global habBox
    hab = ""
    habBox = Entry(enclosuresFrame, width = 30, textvariable = hab)
    habLabel.grid(row=3,column=0,sticky=E,padx=5,pady=10)
    habBox.grid(row=3,column=1,sticky=E+W,padx=5,pady=10)

    # Length
    lenLabel = Label(enclosuresFrame,text="Length: ")
    global lenBox
    length = ""
    lenBox = Entry(enclosuresFrame, width = 30, textvariable = length)
    lenLabel.grid(row=4,column=0,sticky=E,padx=5,pady=10)
    lenBox.grid(row=4,column=1,sticky=E+W,padx=5,pady=10)

    # Width
    widLabel = Label(enclosuresFrame,text="Width: ")
    global widBox
    wid = ""
    widBox = Entry(enclosuresFrame, width = 30, textvariable = wid)
    widLabel.grid(row=5,column=0,sticky=E,padx=5,pady=10)
    widBox.grid(row=5,column=1,sticky=E+W,padx=5,pady=10)

    # Height
    heightLabel = Label(enclosuresFrame,text="Height: ")
    global heightBox
    height = ""
    heightBox = Entry(enclosuresFrame, width = 30, textvariable = height)
    heightLabel.grid(row=6,column=0,sticky=E,padx=5,pady=10)
    heightBox.grid(row=6,column=1,sticky=E+W,padx=5,pady=10)

    # Complex
    compLabel = Label(enclosuresFrame,text="ComplexID: ")
    global compBox
    comp = ""
    compBox = Entry(enclosuresFrame, width = 30, textvariable = comp)
    compLabel.grid(row=7,column=0,sticky=E,padx=5,pady=10)
    compBox.grid(row=7,column=1,sticky=E+W,padx=5,pady=10)


    addButton = Button(enclosuresFrame, text="Add", command=addClick)
    addButton.grid(row=8,columnspan=2)

    doneButton = Button(enclosuresFrame, text="Done", command=doneClick)
    doneButton.grid(row=9, columnspan=2)

    return

#################################################

def set_enclosures_frame(sFrame, editable):
    global enclosuresFrame
    enclosuresFrame = sFrame

    if editable:
        delB = Button(enclosuresFrame,text="Delete an Enclosure",command=delEnclosure)
        delB.grid(column = 0, row = 0, padx=5, pady=5, sticky=N+W)
        modB = Button(enclosuresFrame,text="Modify an Enclosure",command=modEnclosure)
        modB.grid(column = 0, row = 1, padx=5, pady=5, sticky=N+W)
        addB = Button(enclosuresFrame,text="Add an Enclosure",command=addEnclosure)
        addB.grid(column = 0, row = 2, padx=5, pady=5, sticky=N+W)

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
