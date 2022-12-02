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

def show_store(event):
    store = storeSelection.get()
    storeLabel.config(text="Name: " + store)

    mycursor.execute("SELECT Type FROM Store WHERE Store_name = '%s'"%store)
    result = mycursor.fetchall()[0][0]
    if result == None:
        result = "N/A"
    typeLabel.config(text="Type: " + result)

    mycursor.execute("SELECT Name FROM Employee, Store WHERE Store_name = '%s' AND EmployeeID = Manager_EID"%store)
    result = mycursor.fetchall()[0][0]
    if result == None:
        result = "N/A"
    managerLabel.config(text="Manager: " + result)

def set_stores_frame(sFrame):
    global storesFrame
    storesFrame = sFrame

    text = Label(storesFrame, text="Browse Stores")
    text.grid(column = 1, row = 0, sticky=S, ipadx=300, ipady=20)
    global storeSelection
    currValue = StringVar()
    storeSelection = Combobox(storesFrame, width = 30, textvariable = currValue)
    storeSelection.grid(column = 1, row = 1, padx=300, pady=20, sticky=N+S+E+W)

    mycursor.execute("SELECT Store_name FROM Store")
    result = mycursor.fetchall()
    newResult = []
    for x in result:
        store = x[0]
        newResult.append(store)

    storeSelection['values'] = newResult
    storeSelection['state'] = 'readonly'

    storeSelection.bind('<<ComboboxSelected>>', show_store)

    # Create text for store info
    global storeLabel
    global typeLabel
    global managerLabel

    storeLabel = Label(storesFrame, text="Name: None selected")
    storeLabel.grid(column = 1, row = 2, padx=300, pady=20, sticky=S+E+W)
    typeLabel = Label(storesFrame, text="Type: ")
    typeLabel.grid(column = 1, row = 3, padx=300, pady=20, sticky=N+S+E+W)
    managerLabel = Label(storesFrame, text="Manager: ")
    managerLabel.grid(column = 1, row = 4, padx=300, pady=20, sticky=N+S+E+W)
