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

def set_passes_frame(sFrame):
    global passesFrame
    passesFrame = sFrame

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
    passLabel.grid(column = 0, row = 2, pady=20, sticky=S+E+W)
    priceLabel = Label(passesFrame, text="Price: ")
    priceLabel.grid(column = 0, row = 3, pady=20, sticky=N+S+E+W)
    dateLabel = Label(passesFrame, text="Date Issued: ")
    dateLabel.grid(column = 0, row = 4, pady=20, sticky=N+S+E+W)
    receptionistLabel = Label(passesFrame, text="Issued by: ")
    receptionistLabel.grid(column = 0, row = 5, pady=20, sticky=N+S+E+W)

    global previousPass #Tracks whether a membership or ticket was previously selected
    previousPass = ""
