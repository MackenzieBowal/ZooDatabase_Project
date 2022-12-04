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
    database = "zoodatabase"
)

mycursor = mydb.cursor()

def show_exhibit(event):
    exhibit = exhibitSelection.get()

    exhibitLabel.config(text="Exhibit ID: " + exhibit)
    mycursor.execute("SELECT Theme FROM Exhibit WHERE ExhibitID = %s"%exhibit)
    result = mycursor.fetchall()
    themeLabel.config(text="Theme: " + str(result[0][0]))
    mycursor.execute("SELECT Start_date FROM Exhibit WHERE ExhibitID = %s"%exhibit)
    result = mycursor.fetchall()
    startLabel.config(text="Start Date: " + str(result[0][0]))
    mycursor.execute("SELECT End_date FROM Exhibit WHERE ExhibitID = %s"%exhibit)
    result = mycursor.fetchall()
    endLabel.config(text="End Date: " + str(result[0][0]))


#################################################

def doneClick():
    for w in exhibitsFrame.winfo_children():
        w.destroy()
    set_exhibits_frame(exhibitsFrame, True)
    return

def deleteClick():
    delValue = eselectBox.get()
    mycursor.execute("DELETE FROM Exhibit WHERE ExhibitID=" + delValue)
    return

def delExhibit():
    # Refresh the page
    for w in exhibitsFrame.winfo_children():
        w.destroy()

    # create delete page
    eselectLabel = Label(exhibitsFrame,text="Select Exhibit: ")
    global eselectBox
    delValue = ""
    eselectBox = Combobox(exhibitsFrame, width = 30, textvariable = delValue)
    eselectLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    eselectBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)
    fselectButton = Button(exhibitsFrame, text="Delete", command=deleteClick)
    fselectButton.grid(row=1,column=2,stick=W)

    mycursor.execute("SELECT ExhibitID FROM Exhibit")
    result = mycursor.fetchall()

    eselectBox['values'] = result
    eselectBox['state'] = 'readonly'

    doneButton = Button(exhibitsFrame, text="Done", command=doneClick)
    doneButton.grid(row=2, columnspan=3)

    return


def modClick():
    originalid = modESelectBox.get()
    newid = modidBox.get()

    # Keep original values the same if not modified
    if newid == '':
        newid = originalid

    newtheme = modthemeBox.get()
    if newtheme == '':
        mycursor.execute("SELECT Theme FROM Exhibit WHERE ExhibitID="+originalid)
        newtheme = str(mycursor.fetchall()[0][0])

    newstart = modstartBox.get()
    if newstart == '':
        mycursor.execute("SELECT Start_date FROM Exhibit WHERE ExhibitID="+originalid)
        newstart = str(mycursor.fetchall()[0][0])

    newend = modendBox.get()
    if newend == '':
        mycursor.execute("SELECT End_date FROM Exhibit WHERE ExhibitID="+originalid)
        newend = str(mycursor.fetchall()[0][0])

    # Update table
    try:
        mycursor.execute("UPDATE Exhibit SET \
                ExhibitID='"+newid+"', Theme='"+newtheme+"', Start_date='"+newstart+"', \
                End_date='"+newend+"' WHERE ExhibitID=" + originalid)
    except:
        showerror(title="Error", message="Invalid input. Please try again.")
    return

def modExhibit():
    for w in exhibitsFrame.winfo_children():
        w.destroy()

    eselectLabel = Label(exhibitsFrame,text="Select Exhibit: ")
    global modESelectBox
    mVal = ""
    modESelectBox = Combobox(exhibitsFrame, width = 30, textvariable = mVal)
    eselectLabel.grid(row=0,column=0,sticky=E,padx=5,pady=10)
    modESelectBox.grid(row=0,column=1,sticky=E+W,padx=5,pady=10)

    mycursor.execute("SELECT ExhibitID FROM Exhibit")
    result = mycursor.fetchall()

    modESelectBox['values'] = tuple(result)
    modESelectBox['state'] = 'readonly'

    # ID
    idLabel = Label(exhibitsFrame,text="Set ExhibitID: ")
    global modidBox
    id = ""
    modidBox = Entry(exhibitsFrame, width = 30, textvariable = id)
    idLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    modidBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)

    # Theme
    themeLabel = Label(exhibitsFrame,text="Set Theme: ")
    global modthemeBox
    theme = ""
    modthemeBox = Entry(exhibitsFrame, width = 30, textvariable = theme)
    themeLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
    modthemeBox.grid(row=2,column=1,sticky=E+W,padx=5,pady=10)

    # Start date
    startLabel = Label(exhibitsFrame,text="Set Start date (yyyy-mm-dd): ")
    global modstartBox
    start = ""
    modstartBox = Entry(exhibitsFrame, width = 30, textvariable = start)
    startLabel.grid(row=3,column=0,sticky=E,padx=5,pady=10)
    modstartBox.grid(row=3,column=1,sticky=E+W,padx=5,pady=10)

    # End date
    endLabel = Label(exhibitsFrame,text="Set End date (yyyy-mm-dd): ")
    global modendBox
    end = ""
    modendBox = Entry(exhibitsFrame, width = 30, textvariable = end)
    endLabel.grid(row=4,column=0,sticky=E,padx=5,pady=10)
    modendBox.grid(row=4,column=1,sticky=E+W,padx=5,pady=10)


    modButton = Button(exhibitsFrame, text="Update", command=modClick)
    modButton.grid(row=6,columnspan=2)

    doneButton = Button(exhibitsFrame, text="Done", command=doneClick)
    doneButton.grid(row=7,columnspan=2)

    return


def addClick():
    eid = idBox.get()
    theme = themeBox.get()
    start = startBox.get()
    end = endBox.get()

    try:
        mycursor.execute("INSERT INTO Exhibit \
                VALUES ('"+eid+"', '"+theme+"', '"+start+"', '"+end+"')")
    except:
        showerror(title="Error", message="Invalid input. Please try again.")
    return

def addExhibit():
    for w in exhibitsFrame.winfo_children():
        w.destroy()

    # ID
    idLabel = Label(exhibitsFrame,text="ExhibitID: ")
    global idBox
    id = ""
    idBox = Entry(exhibitsFrame, width = 30, textvariable = id)
    idLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    idBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)

    # Theme
    themeLabel = Label(exhibitsFrame,text="Theme: ")
    global themeBox
    theme = ""
    themeBox = Entry(exhibitsFrame, width = 30, textvariable = theme)
    themeLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
    themeBox.grid(row=2,column=1,sticky=E+W,padx=5,pady=10)

    # Start date
    startLabel = Label(exhibitsFrame,text="Start date (yyyy-mm-dd): ")
    global startBox
    start = ""
    startBox = Entry(exhibitsFrame, width = 30, textvariable = start)
    startLabel.grid(row=3,column=0,sticky=E,padx=5,pady=10)
    startBox.grid(row=3,column=1,sticky=E+W,padx=5,pady=10)

    # End date
    endLabel = Label(exhibitsFrame,text="End date (yyyy-mm-dd): ")
    global endBox
    end = ""
    endBox = Entry(exhibitsFrame, width = 30, textvariable = end)
    endLabel.grid(row=4,column=0,sticky=E,padx=5,pady=10)
    endBox.grid(row=4,column=1,sticky=E+W,padx=5,pady=10)


    addButton = Button(exhibitsFrame, text="Add", command=addClick)
    addButton.grid(row=9,columnspan=2)

    doneButton = Button(exhibitsFrame, text="Done", command=doneClick)
    doneButton.grid(row=10, columnspan=2)

    return

#################################################

def set_exhibits_frame(eFrame, editable):
    global exhibitsFrame
    exhibitsFrame = eFrame

    if editable:
        delB = Button(exhibitsFrame,text="Delete an Exhibit",command=delExhibit)
        delB.grid(column = 0, row = 0, padx=5, pady=5, sticky=N+W)
        modB = Button(exhibitsFrame,text="Modify an Exhibit",command=modExhibit)
        modB.grid(column = 0, row = 1, padx=5, pady=5, sticky=N+W)
        addB = Button(exhibitsFrame,text="Add an Exhibit",command=addExhibit)
        addB.grid(column = 0, row = 2, padx=5, pady=5, sticky=N+W)

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
    global themeLabel
    global startLabel
    global endLabel

    exhibitLabel = Label(exhibitsFrame, text="Exhibit: None selected")
    exhibitLabel.grid(column = 1, row = 2, padx=300, pady=20, sticky=S+E+W)
    themeLabel = Label(exhibitsFrame, text="Theme: ")
    themeLabel.grid(column = 1, row = 3, padx=300, pady=20, sticky=N+S+E+W)
    startLabel = Label(exhibitsFrame, text="Start Date: ")
    startLabel.grid(column = 1, row = 4, padx=300, pady=20, sticky=N+S+E+W)
    endLabel = Label(exhibitsFrame, text="End Date: ")
    endLabel.grid(column = 1, row = 5, padx=300, pady=20, sticky=N+S+E+W)
