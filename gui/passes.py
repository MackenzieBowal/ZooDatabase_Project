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

def show_pass(event):
    passid = passSelection.get()
    passLabel.config(text="Pass ID: " + passid)

    mycursor.execute("SELECT Sold_price FROM Pass WHERE PassID = '%s'"%passid)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    priceLabel.config(text="Price: " + result)

    mycursor.execute("SELECT Date_issued FROM Pass WHERE PassID = '%s'"%passid)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    dateLabel.config(text="Date Issued: " + result)

    mycursor.execute("SELECT Receptionist_EID FROM Pass WHERE PassID = '%s'"%passid)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    receptionistLabel.config(text="Issued by: " + result)

    mycursor.execute("SELECT * FROM Membership WHERE PassID = '%s'"%passid)
    result = mycursor.fetchall()
    if len(result) > 0: #Pass is a membership
        show_membership(passid)
    else: #Pass is a ticket
        show_ticket(passid)

def show_membership(passid):
    global previousPass
    global nameLabel
    global emailLabel
    global durationLabel

    #Erase the details of any previous membership/ticket that are still on the screen
    if previousPass == "membership":
        nameLabel.destroy()
        emailLabel.destroy()
        durationLabel.destroy()
    elif previousPass == "ticket":
        ticketLabel.destroy()

    previousPass = "membership"

    nameLabel = Label(passesFrame, text="Member Name: ")
    nameLabel.grid(column = 1, row = 2, pady=20, sticky=S+E+W)
    emailLabel = Label(passesFrame, text="Email: ")
    emailLabel.grid(column = 1, row = 3, pady=20, sticky=N+S+E+W)
    durationLabel = Label(passesFrame, text="Days Left: ")
    durationLabel.grid(column = 1, row = 4, pady=20, sticky=N+S+E+W)

    mycursor.execute("SELECT Member_name FROM Membership WHERE PassID = '%s'"%passid)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    nameLabel.config(text="Member Name: " + result)

    mycursor.execute("SELECT Email FROM Membership WHERE PassID = '%s'"%passid)
    result = str(mycursor.fetchall()[0][0])
    emailLabel.config(text="Email: " + result)

    mycursor.execute("SELECT Duration FROM Membership WHERE PassID = '%s'"%passid)
    result = str(mycursor.fetchall()[0][0])
    durationLabel.config(text="Days Left: " + result)

def show_ticket(passid):
    global previousPass
    global ticketLabel

    #Erase the details of any previous membership/ticket that are still on the screen
    if previousPass == "membership":
        nameLabel.destroy()
        emailLabel.destroy()
        durationLabel.destroy()
    elif previousPass == "ticket":
        ticketLabel.destroy()

    previousPass = "ticket"

    ticketLabel = Label(passesFrame, text="Ticket ID: ")
    ticketLabel.grid(column = 1, row = 2, pady=20, sticky=S+E+W)

    mycursor.execute("SELECT TicketID FROM Ticket WHERE PassID = '%s'"%passid)
    result = str(mycursor.fetchall()[0][0])
    ticketLabel.config(text="Ticket ID: " + result)




#################################################

def doneClick():
    for w in passesFrame.winfo_children():
        w.destroy()
    set_passes_frame(passesFrame, receptionistID)
    return


def addMembershipClick():
    email = str(idBox.get())
    name = str(nameBox.get())
    dur = str(durBox.get())
    passid = str(passBox.get())
    price = str(prBox.get())
    date = str(dateBox.get())

    try:
        mycursor.execute("INSERT INTO Pass \
                VALUES ('"+str(passid)+"', '"+str(price)+"', '"+str(date)+"', '"+str(receptionistID)+"')")
        mycursor.execute("INSERT INTO Membership \
                VALUES ('"+email+"', '"+name+"', "+dur+", '"+passid+"')")
    except:
        showerror(title="Error", message="Invalid input. Please try again.")
    return

def addMembership():
    for w in passesFrame.winfo_children():
        w.destroy()

    # ID
    idLabel = Label(passesFrame,text="Member Email: ")
    global idBox
    id = ""
    idBox = Entry(passesFrame, width = 30, textvariable = id)
    idLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    idBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)

    # Name
    nameLabel = Label(passesFrame,text="Member Name: ")
    global nameBox
    name = ""
    nameBox = Entry(passesFrame, width = 30, textvariable = name)
    nameLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
    nameBox.grid(row=2,column=1,sticky=E+W,padx=5,pady=10)

    # Duration
    durLabel = Label(passesFrame,text="Duration (days): ")
    global durBox
    dur = ""
    durBox = Entry(passesFrame, width = 30, textvariable = dur)
    durLabel.grid(row=3,column=0,sticky=E,padx=5,pady=10)
    durBox.grid(row=3,column=1,sticky=E+W,padx=5,pady=10)

    # pass id
    passLabel = Label(passesFrame,text="PassID: ")
    global passBox
    pa = ""
    passBox = Entry(passesFrame, width = 30, textvariable = pa)
    passLabel.grid(row=4,column=0,sticky=E,padx=5,pady=10)
    passBox.grid(row=4,column=1,sticky=E+W,padx=5,pady=10)

    # Price
    prLabel = Label(passesFrame,text="Price: ")
    global prBox
    pr = ""
    prBox = Entry(passesFrame, width = 30, textvariable = pr)
    prLabel.grid(row=5,column=0,sticky=E,padx=5,pady=10)
    prBox.grid(row=5,column=1,sticky=E+W,padx=5,pady=10)

    # Date
    dateLabel = Label(passesFrame,text="Date (yyyy-mm-dd): ")
    global dateBox
    date = ""
    dateBox = Entry(passesFrame, width = 30, textvariable = date)
    dateLabel.grid(row=6,column=0,sticky=E,padx=5,pady=10)
    dateBox.grid(row=6,column=1,sticky=E+W,padx=5,pady=10)


    addButton = Button(passesFrame, text="Add", command=addMembershipClick)
    addButton.grid(row=7,columnspan=2)

    doneButton = Button(passesFrame, text="Done", command=doneClick)
    doneButton.grid(row=8, columnspan=2)

    return


def addTicketClick():
    ticket = str(idBox.get())
    passid = str(passBox.get())
    price = str(prBox.get())
    date = str(dateBox.get())

    try:
        mycursor.execute("INSERT INTO Pass \
                VALUES ('"+str(passid)+"', '"+str(price)+"', '"+str(date)+"', '"+str(receptionistID)+"')")
        mycursor.execute("INSERT INTO Ticket \
                VALUES ('"+ticket+"', '"+passid+"')")
    except:
        showerror(title="Error", message="Invalid input. Please try again.")
    return

def addTicket():
    for w in passesFrame.winfo_children():
        w.destroy()

    # ID
    idLabel = Label(passesFrame,text="Ticket Number: ")
    global idBox
    id = ""
    idBox = Entry(passesFrame, width = 30, textvariable = id)
    idLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    idBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)

    # pass id
    passLabel = Label(passesFrame,text="PassID: ")
    global passBox
    pa = ""
    passBox = Entry(passesFrame, width = 30, textvariable = pa)
    passLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
    passBox.grid(row=2,column=1,sticky=E+W,padx=5,pady=10)

    # Price
    prLabel = Label(passesFrame,text="Price: ")
    global prBox
    pr = ""
    prBox = Entry(passesFrame, width = 30, textvariable = pr)
    prLabel.grid(row=3,column=0,sticky=E,padx=5,pady=10)
    prBox.grid(row=3,column=1,sticky=E+W,padx=5,pady=10)

    # Date
    dateLabel = Label(passesFrame,text="Date (yyyy-mm-dd): ")
    global dateBox
    date = ""
    dateBox = Entry(passesFrame, width = 30, textvariable = date)
    dateLabel.grid(row=4,column=0,sticky=E,padx=5,pady=10)
    dateBox.grid(row=4,column=1,sticky=E+W,padx=5,pady=10)


    addButton = Button(passesFrame, text="Add", command=addTicketClick)
    addButton.grid(row=5,columnspan=2)

    doneButton = Button(passesFrame, text="Done", command=doneClick)
    doneButton.grid(row=6, columnspan=2)

    return



def modClick():
    originalid = modESelectBox.get()
    newid = modidBox.get()

    # Keep original values the same if not modified
    if newid == '':
        newid = originalid

    newname = modnameBox.get()
    if newname == '':
        mycursor.execute("SELECT Member_name FROM Membership WHERE Email='"+originalid+"'")
        newname = str(mycursor.fetchall()[0][0])

    newdur = moddurBox.get()
    if newdur == '':
        mycursor.execute("SELECT Duration FROM Membership WHERE Email='"+originalid+"'")
        newdur = str(mycursor.fetchall()[0][0])

    # Update table
    try:
        mycursor.execute("UPDATE Membership SET \
                Email='"+newid+"', Member_name='"+newname+"', Duration='"+newdur+"' WHERE Email='" + originalid + "'")
    except:
        showerror(title="Error", message="Invalid input. Please try again.")
    return

def modMembership():
    for w in passesFrame.winfo_children():
        w.destroy()

    eselectLabel = Label(passesFrame,text="Select Membership: ")
    global modESelectBox
    mVal = ""
    modESelectBox = Combobox(passesFrame, width = 30, textvariable = mVal)
    eselectLabel.grid(row=0,column=0,sticky=E,padx=5,pady=10)
    modESelectBox.grid(row=0,column=1,sticky=E+W,padx=5,pady=10)

    mycursor.execute("SELECT Email FROM Membership")
    result = mycursor.fetchall()

    modESelectBox['values'] = tuple(result)
    modESelectBox['state'] = 'readonly'

    # ID
    idLabel = Label(passesFrame,text="Set Member Email: ")
    global modidBox
    id = ""
    modidBox = Entry(passesFrame, width = 30, textvariable = id)
    idLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    modidBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)

    # Name
    nameLabel = Label(passesFrame,text="Set Member Name: ")
    global modnameBox
    name = ""
    modnameBox = Entry(passesFrame, width = 30, textvariable = name)
    nameLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
    modnameBox.grid(row=2,column=1,sticky=E+W,padx=5,pady=10)

    # Duration
    durLabel = Label(passesFrame,text="Set Duration (days): ")
    global moddurBox
    dur = ""
    moddurBox = Entry(passesFrame, width = 30, textvariable = dur)
    durLabel.grid(row=3,column=0,sticky=E,padx=5,pady=10)
    moddurBox.grid(row=3,column=1,sticky=E+W,padx=5,pady=10)


    modButton = Button(passesFrame, text="Update", command=modClick)
    modButton.grid(row=4,columnspan=2)

    doneButton = Button(passesFrame, text="Done", command=doneClick)
    doneButton.grid(row=5,columnspan=2)

    return


#################################################



def set_passes_frame(sFrame, r):
    global passesFrame
    passesFrame = sFrame

    global receptionistID
    receptionistID = r

    delB = Button(passesFrame,text="Add a Ticket",command=addTicket)
    delB.grid(column = 0, row = 0, padx=5, pady=5, sticky=N+W)
    modB = Button(passesFrame,text="Add a Membership",command=addMembership)
    modB.grid(column = 0, row = 1, padx=5, pady=5, sticky=N+W)
    addB = Button(passesFrame,text="Modify a Membership",command=modMembership)
    addB.grid(column = 0, row = 2, padx=5, pady=5, sticky=N+W)


    text = Label(passesFrame, text="Browse passes")
    text.grid(column = 1, row = 0, sticky=S, ipadx=300, ipady=20)
    global passSelection
    currValue = StringVar()
    passSelection = Combobox(passesFrame, width = 30, textvariable = currValue)
    passSelection.grid(column = 1, row = 1, padx=300, pady=20, sticky=N+S+E+W)

    mycursor.execute("SELECT PassID FROM Pass")
    result = mycursor.fetchall()

    passSelection['values'] = result
    passSelection['state'] = 'readonly'

    passSelection.bind('<<ComboboxSelected>>', show_pass)

    # Create text for pass info
    global passLabel
    global priceLabel
    global dateLabel
    global receptionistLabel

    passLabel = Label(passesFrame, text="Pass ID: None selected")
    passLabel.grid(column = 1, row = 2, pady=20, sticky=S+E+W)
    priceLabel = Label(passesFrame, text="Price: ")
    priceLabel.grid(column = 1, row = 3, pady=20, sticky=N+S+E+W)
    dateLabel = Label(passesFrame, text="Date Issued: ")
    dateLabel.grid(column = 1, row = 4, pady=20, sticky=N+S+E+W)
    receptionistLabel = Label(passesFrame, text="Issued by: ")
    receptionistLabel.grid(column = 1, row = 5, pady=20, sticky=N+S+E+W)

    global previousPass #Tracks whether a membership or ticket was previously selected
    previousPass = ""
