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

def show_complex(event):
    indoorcomplex = complexSelection.get()
    complexLabel.config(text="Complex ID: " + indoorcomplex)

    mycursor.execute("SELECT Address_nbr FROM Indoor_complex WHERE ComplexID = '%s'"%indoorcomplex)
    addressnbr = str(mycursor.fetchall()[0][0])
    mycursor.execute("SELECT Street_name FROM Indoor_complex WHERE ComplexID = '%s'"%indoorcomplex)
    streetname = str(mycursor.fetchall()[0][0])
    addressLabel.config(text="Address: " + addressnbr + " " + streetname)

def set_complexes_frame(sFrame):
    global complexesFrame
    complexesFrame = sFrame

    text = Label(complexesFrame, text="Browse complexes")
    text.grid(column = 1, row = 0, sticky=S, ipadx=300, ipady=20)
    global complexSelection
    currValue = StringVar()
    complexSelection = Combobox(complexesFrame, width = 30, textvariable = currValue)
    complexSelection.grid(column = 1, row = 1, padx=300, pady=20, sticky=N+S+E+W)

    mycursor.execute("SELECT ComplexID FROM Indoor_complex")
    result = mycursor.fetchall()

    complexSelection['values'] = result
    complexSelection['state'] = 'readonly'

    complexSelection.bind('<<ComboboxSelected>>', show_complex)

    # Create text for complex info
    global complexLabel
    global addressLabel

    complexLabel = Label(complexesFrame, text="Complex ID: None selected")
    complexLabel.grid(column = 1, row = 2, padx=300, pady=20, sticky=S+E+W)
    addressLabel = Label(complexesFrame, text="Address: ")
    addressLabel.grid(column = 1, row = 3, padx=300, pady=20, sticky=N+S+E+W)
