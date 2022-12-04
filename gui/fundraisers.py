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
    
    set_fundraisers_frame(savedFFrame, True)
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
    global fselectBox
    delValue = ""
    fselectBox = Combobox(fundraisersFrame, width = 30, textvariable = delValue)
    fselectLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    fselectBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)
    fselectButton = Button(fundraisersFrame, text="Delete", command=deleteClick)
    fselectButton.grid(row=1,column=2,stick=W)

    mycursor.execute("SELECT FundraiserID FROM Fundraiser")
    result = mycursor.fetchall()

    fselectBox['values'] = result
    fselectBox['state'] = 'readonly'

    doneButton = Button(fundraisersFrame, text="Done", command=doneClick)
    doneButton.grid(row=2, columnspan=3)


    return

def modFundraiser(event):

    for w in fundraisersFrame.winfo_children():
        w.destroy()


    mytext = Label(fundraisersFrame, text="yay it worked")
    mytext.grid(row=1, column=1, sticky=N+S+E+W)

    doneButton = Button(fundraisersFrame, text="Done", command=doneClick)
    doneButton.grid(row=2, column=1)


    return


def addFundraiser(event):

    for w in fundraisersFrame.winfo_children():
        w.destroy()


    mytext = Label(fundraisersFrame, text="yay it worked")
    mytext.grid(row=1, column=1, sticky=N+S+E+W)

    doneButton = Button(fundraisersFrame, text="Done", command=doneClick)
    doneButton.grid(row=2, column=1)



    return


def set_fundraisers_frame(sFrame, e):
    global fundraisersFrame
    global savedFFrame
    fundraisersFrame = sFrame
    savedFFrame = sFrame

    global editable
    editable = e

    if editable:
        delB = Button(fundraisersFrame,text="Delete Fundraiser",command=delFundraiser)
        delB.grid(column = 0, row = 0, padx=5, pady=5, sticky=N+W)
        modB = Button(fundraisersFrame,text="Modify Fundraiser",command=modFundraiser)
        modB.grid(column = 0, row = 1, padx=5, pady=5, sticky=N+W)
        addB = Button(fundraisersFrame,text="Add Fundraiser",command=addFundraiser)
        addB.grid(column = 0, row = 2, padx=5, pady=5, sticky=N+W)


    text = Label(fundraisersFrame, text="Browse fundraisers")
    text.grid(column = 1, row = 0, sticky=S, ipadx=300, ipady=20)
    global fundraiserSelection
    currValue = StringVar()
    fundraiserSelection = Combobox(fundraisersFrame, width = 30, textvariable = currValue)
    fundraiserSelection.grid(column = 1, row = 1, padx=300, pady=20, sticky=N+S+E+W)

    mycursor.execute("SELECT FundraiserID FROM Fundraiser")
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
