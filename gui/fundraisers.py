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

def show_fundraiser(event):
    fundraiser = fundraiserSelection.get()
    fundraiserLabel.config(text="Fundraiser ID: " + fundraiser)

    mycursor.execute("SELECT Theme FROM Fundraiser WHERE FundraiserID = '%s'"%fundraiser)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    themeLabel.config(text="Theme: " + result)

    return


def doneClick():
    for w in fundraisersFrame.winfo_children():
        w.destroy()
    
    set_fundraisers_frame(savedFFrame, managerID, True)
    return

def deleteClick():
    delValue = fselectBox.get()
    mycursor.execute("DELETE FROM Fundraiser WHERE FundraiserID=" + delValue)
    return

def delFundraiser():
    # Refresh the page
    for w in fundraisersFrame.winfo_children():
        w.destroy()

    # create delete page
    fname = StringVar()
    fselectLabel = Label(fundraisersFrame,text="Select Fundraiser: ")
    global fselectBox
    delValue = ""
    fselectBox = Combobox(fundraisersFrame, width = 30, textvariable = delValue)
    fselectLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    fselectBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)
    fselectButton = Button(fundraisersFrame, text="Delete", command=deleteClick)
    fselectButton.grid(row=1,column=2,stick=W)

    mycursor.execute("SELECT FundraiserID FROM Overlooks WHERE Manager_EID="+managerID)
    result = mycursor.fetchall()

    fselectBox['values'] = result
    fselectBox['state'] = 'readonly'

    doneButton = Button(fundraisersFrame, text="Done", command=doneClick)
    doneButton.grid(row=2, columnspan=3)

    return

def modClick():
    originalFID = modFSelectBox.get()
    newFID = modFidBox.get()

    # Keep original values the same if not modified
    if newFID == '':
        newFID = originalFID

    newFTheme = modFthemeBox.get()
    if newFTheme == '':
        mycursor.execute("SELECT Theme FROM Fundraiser WHERE FundraiserID="+originalFID)
        newFTheme = str(mycursor.fetchall()[0][0])


    mycursor.execute("UPDATE Fundraiser SET \
                FundraiserID='"+newFID+"', Theme='"+newFTheme+"' WHERE FundraiserID=" + originalFID)
        #mycursor.execute("UPDATE Overlooks SET FundraiserID="+newFID+" WHERE FundraiserID="+originalFID)
    #except:
    #    showerror(title="Error", message="Invalid FundraiserID or Theme. Please try again.")
    return

def modFundraiser():

    for w in fundraisersFrame.winfo_children():
        w.destroy()

    fname = StringVar()
    fselectLabel = Label(fundraisersFrame,text="Select Fundraiser: ")
    global modFSelectBox
    delValue = ""
    modFSelectBox = Combobox(fundraisersFrame, width = 30, textvariable = delValue)
    fselectLabel.grid(row=0,column=0,sticky=E,padx=5,pady=10)
    modFSelectBox.grid(row=0,column=1,sticky=E+W,padx=5,pady=10)

    mycursor.execute("SELECT FundraiserID FROM Overlooks WHERE Manager_EID="+managerID)
    result = mycursor.fetchall()

    modFSelectBox['values'] = result
    modFSelectBox['state'] = 'readonly'

    fidLabel = Label(fundraisersFrame,text="Set FundraiserID: ")
    global modFidBox
    fid = ""
    modFidBox = Entry(fundraisersFrame, width = 30, textvariable = fid)
    fidLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    modFidBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)

    fthemeLabel = Label(fundraisersFrame,text="Set Theme: ")
    global modFthemeBox
    ftheme = ""
    modFthemeBox = Entry(fundraisersFrame, width = 30, textvariable = ftheme)
    fthemeLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
    modFthemeBox.grid(row=2,column=1,sticky=E+W,padx=5,pady=10)

    modButton = Button(fundraisersFrame, text="Update", command=modClick)
    modButton.grid(row=3,column=1)

    doneButton = Button(fundraisersFrame, text="Done", command=doneClick)
    doneButton.grid(row=4,column=1)

    return

def addClick():
    fid = fidBox.get()
    ftheme = fthemeBox.get()
    try:
        mycursor.execute("INSERT INTO Fundraiser \
                VALUES ("+fid+", '"+ftheme+"')")
        mycursor.execute("INSERT INTO Overlooks \
                VALUES ("+managerID+", "+fid+")")
    except:
        showerror(title="Error",message="Invalid FundraiserID or Theme. Please try again.")
    return

def addFundraiser():

    for w in fundraisersFrame.winfo_children():
        w.destroy()

    fidLabel = Label(fundraisersFrame,text="FundraiserID: ")
    global fidBox
    fid = ""
    fidBox = Entry(fundraisersFrame, width = 30, textvariable = fid)
    fidLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    fidBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)

    fthemeLabel = Label(fundraisersFrame,text="Theme: ")
    global fthemeBox
    ftheme = ""
    fthemeBox = Entry(fundraisersFrame, width = 30, textvariable = ftheme)
    fthemeLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
    fthemeBox.grid(row=2,column=1,sticky=E+W,padx=5,pady=10)

    addButton = Button(fundraisersFrame, text="Add", command=addClick)
    addButton.grid(row=3,columnspan=2)

    doneButton = Button(fundraisersFrame, text="Done", command=doneClick)
    doneButton.grid(row=4, columnspan=2)

    return


def set_fundraisers_frame(sFrame, mID, e):
    global fundraisersFrame
    global savedFFrame
    fundraisersFrame = sFrame
    savedFFrame = sFrame

    global managerID
    managerID = str(mID)

    global editable
    editable = e

    if editable:
        delB = Button(fundraisersFrame,text="Delete a Fundraiser",command=delFundraiser)
        delB.grid(column = 0, row = 0, padx=5, pady=5, sticky=N+W)
        modB = Button(fundraisersFrame,text="Modify a Fundraiser",command=modFundraiser)
        modB.grid(column = 0, row = 1, padx=5, pady=5, sticky=N+W)
        addB = Button(fundraisersFrame,text="Add a Fundraiser",command=addFundraiser)
        addB.grid(column = 0, row = 2, padx=5, pady=5, sticky=N+W)


    text = Label(fundraisersFrame, text="Browse fundraisers")
    text.grid(column = 1, row = 0, sticky=S, ipadx=300, ipady=20)
    global fundraiserSelection
    currValue = StringVar()
    fundraiserSelection = Combobox(fundraisersFrame, width = 30, textvariable = currValue)
    fundraiserSelection.grid(column = 1, row = 1, padx=300, pady=20, sticky=N+S+E+W)

    mycursor.execute("SELECT FundraiserID FROM Overlooks WHERE Manager_EID="+managerID)
    result = mycursor.fetchall()

    fundraiserSelection['values'] = result
    fundraiserSelection['state'] = 'readonly'

    fundraiserSelection.bind('<<ComboboxSelected>>', show_fundraiser)

    # Create text for fundraiser info
    global fundraiserLabel
    global themeLabel

    fundraiserLabel = Label(fundraisersFrame, text="Fundraiser ID: None selected")
    fundraiserLabel.grid(column = 1, row = 2, padx=300, pady=20, sticky=S+E+W)
    themeLabel = Label(fundraisersFrame, text="Theme: ")
    themeLabel.grid(column = 1, row = 3, padx=300, pady=20, sticky=N+S+E+W)
