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
    donorLabel.config(text="Donor ID: " + donor)

    mycursor.execute("SELECT Name FROM Donor WHERE DonorID = '%s'"%donor)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    nameLabel.config(text="Name: " + result)

    mycursor.execute("SELECT Address FROM Donor WHERE DonorID = '%s'"%donor)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    addressLabel.config(text="Address: " + result)

    mycursor.execute("SELECT Email FROM Donor WHERE DonorID = '%s'"%donor)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    emailLabel.config(text="Email: " + result)

    mycursor.execute("SELECT Phone_number FROM Donor WHERE DonorID = '%s'"%donor)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    phoneLabel.config(text="Phone: " + result)

def set_donors_frame(sFrame):
    global donorsFrame
    donorsFrame = sFrame

    text = Label(donorsFrame, text="Browse donors")
    text.grid(column = 1, row = 0, sticky=S, ipadx=300, ipady=20)
    global donorSelection
    currValue = StringVar()
    donorSelection = Combobox(donorsFrame, width = 30, textvariable = currValue)
    donorSelection.grid(column = 1, row = 1, padx=300, pady=20, sticky=N+S+E+W)

    mycursor.execute("SELECT DonorID FROM Donor")
    result = mycursor.fetchall()

    donorSelection['values'] = result
    donorSelection['state'] = 'readonly'

    donorSelection.bind('<<ComboboxSelected>>', show_donor)

    # Create text for donor info
    global donorLabel
    global nameLabel
    global addressLabel
    global emailLabel
    global phoneLabel

    donorLabel = Label(donorsFrame, text="Donor ID: None selected")
    donorLabel.grid(column = 1, row = 2, padx=300, pady=20, sticky=S+E+W)
    nameLabel = Label(donorsFrame, text="Name: ")
    nameLabel.grid(column = 1, row = 3, padx=300, pady=20, sticky=N+S+E+W)
    addressLabel = Label(donorsFrame, text="Address: ")
    addressLabel.grid(column = 1, row = 4, padx=300, pady=20, sticky=N+S+E+W)
    emailLabel = Label(donorsFrame, text="Email: ")
    emailLabel.grid(column = 1, row = 5, padx=300, pady=20, sticky=N+S+E+W)
    phoneLabel = Label(donorsFrame, text="Phone: ")
    phoneLabel.grid(column = 1, row = 6, padx=300, pady=20, sticky=N+S+E+W)
