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

def show_donor(event):
    donor = donorSelection.get()
    nameLabel.config(text="Name: " + donor)


    mycursor.execute("SELECT DonorID FROM Donor WHERE Name = '%s'"%donor)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    donorLabel.config(text="Donor ID: " + result)

    if (limitedView == False):
            
        mycursor.execute("SELECT Address FROM Donor WHERE Name = '%s'"%donor)
        result = str(mycursor.fetchall()[0][0])
        if result == "None":
            result = "N/A"
        addressLabel.config(text="Address: " + result)

        mycursor.execute("SELECT Email FROM Donor WHERE Name = '%s'"%donor)
        result = str(mycursor.fetchall()[0][0])
        if result == "None":
            result = "N/A"
        emailLabel.config(text="Email: " + result)

        mycursor.execute("SELECT Phone_number FROM Donor WHERE Name = '%s'"%donor)
        result = str(mycursor.fetchall()[0][0])
        if result == "None":
            result = "N/A"
        phoneLabel.config(text="Phone: " + result)
    
    mycursor.execute("SELECT Amount_donated FROM Donor WHERE Name = '%s'"%donor)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    amountLabel.config(text="Amount donated: " + result)

    return

def set_donors_frame(sFrame, lv):
    global donorsFrame
    donorsFrame = sFrame

    global limitedView
    limitedView = lv

    text = Label(donorsFrame, text="Browse donors")
    text.grid(column = 1, row = 0, sticky=S, ipadx=300, ipady=20)
    global donorSelection
    currValue = StringVar()
    donorSelection = Combobox(donorsFrame, width = 30, textvariable = currValue)
    donorSelection.grid(column = 1, row = 1, padx=300, pady=20, sticky=N+S+E+W)

    mycursor.execute("SELECT Name FROM Donor")

    dNames = []

    for i in mycursor.fetchall():
        dNames.append(i[0])

    donorSelection['values'] = tuple(set(dNames))
    donorSelection['state'] = 'readonly'

    donorSelection.bind('<<ComboboxSelected>>', show_donor)

    # Create text for donor info
    global donorLabel
    global nameLabel
    global addressLabel
    global emailLabel
    global phoneLabel
    global amountLabel

    donorLabel = Label(donorsFrame, text="Donor ID: None selected")
    donorLabel.grid(column = 1, row = 2, padx=300, pady=20, sticky=S+E+W)

    nameLabel = Label(donorsFrame, text="Name: ")
    nameLabel.grid(column = 1, row = 3, padx=300, pady=20, sticky=N+S+E+W)


    if (limitedView == False):

        addressLabel = Label(donorsFrame, text="Address: ")
        addressLabel.grid(column = 1, row = 4, padx=300, pady=20, sticky=N+S+E+W)
        emailLabel = Label(donorsFrame, text="Email: ")
        emailLabel.grid(column = 1, row = 5, padx=300, pady=20, sticky=N+S+E+W)
        phoneLabel = Label(donorsFrame, text="Phone: ")
        phoneLabel.grid(column = 1, row = 6, padx=300, pady=20, sticky=N+S+E+W)
        amountLabel = Label(donorsFrame, text="Amount donated: ")
        amountLabel.grid(column = 1, row = 7, padx=300, pady=20, sticky=N+S+E+W)

    
    else:
        amountLabel = Label(donorsFrame, text="Amount donated: ")
        amountLabel.grid(column = 1, row = 4, padx=300, pady=20, sticky=N+S+E+W)
        thankyouLabel = Label(donorsFrame, text="Thank you to our generous donors!")
        thankyouLabel.grid(column = 1, row = 5, padx=300, pady=20, sticky=N+S+E+W)

