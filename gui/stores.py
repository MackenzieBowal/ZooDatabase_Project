from ctypes import alignment
from tkinter import *
from tkinter.ttk import Combobox
from tkinter.scrolledtext import ScrolledText
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

    mycursor.execute("SELECT Date FROM Daily_revenue WHERE Store_name = '%s'"%store)
    dates = mycursor.fetchall()
    dailyrevenueText['state'] = 'normal'
    dailyrevenueText.delete("2.0", "end")
    dailyrevenueText.insert("1.end", '\n')
    line = 2
    for date in dates:
        mycursor.execute("SELECT Revenue FROM Daily_revenue WHERE Store_name = '%s' AND Date = '%s'"%(store,str(date[0])))
        revenue = mycursor.fetchall()[0][0]
        dailyrevenueString = str(date[0]) + ": $" + str(revenue) + '\n'
        position = str(line) + ".0"
        dailyrevenueText.insert(position, dailyrevenueString)
        line += 1
    dailyrevenueText['state'] = 'disabled'

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
    global dailyrevenueText

    storeLabel = Label(storesFrame, text="Name: None selected")
    storeLabel.grid(column = 0, row = 2, padx=300, pady=20, sticky=S+E+W)
    typeLabel = Label(storesFrame, text="Type: ")
    typeLabel.grid(column = 0, row = 3, padx=300, pady=20, sticky=N+S+E+W)
    managerLabel = Label(storesFrame, text="Manager: ")
    managerLabel.grid(column = 0, row = 4, padx=300, pady=20, sticky=N+S+E+W)
    dailyrevenueText = ScrolledText(storesFrame, height=8)
    dailyrevenueText.grid(column = 1, row = 2, rowspan=3, pady=20, sticky=N+S+E+W)
    dailyrevenueText.insert('1.0', "Daily Revenue:\n")
    dailyrevenueText['state'] = 'disabled'
