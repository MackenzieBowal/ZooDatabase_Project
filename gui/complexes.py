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

mycursor = mydb.cursor(prepared=True)

def show_complex(event):
    indoorcomplex = complexSelection.get()
    complexLabel.config(text="Complex ID: " + indoorcomplex)

    mycursor.execute("SELECT Address_nbr FROM Indoor_complex WHERE ComplexID = '%s'"%indoorcomplex)
    addressnbr = str(mycursor.fetchall()[0][0])
    mycursor.execute("SELECT Street_name FROM Indoor_complex WHERE ComplexID = '%s'"%indoorcomplex)
    streetname = str(mycursor.fetchall()[0][0])
    addressLabel.config(text="Address: " + addressnbr + " " + streetname)


#################################################

def doneClick():
    for w in complexesFrame.winfo_children():
        w.destroy()
    set_complexes_frame(complexesFrame)
    return

def deleteClick():
    delValue = cselectBox.get()
    mycursor.execute("DELETE FROM Indoor_complex WHERE ComplexID=" + delValue)
    return

def delComplex():
    # Refresh the page
    for w in complexesFrame.winfo_children():
        w.destroy()

    # create delete page
    cselectLabel = Label(complexesFrame,text="Select Complex: ")
    global cselectBox
    delValue = ""
    cselectBox = Combobox(complexesFrame, width = 30, textvariable = delValue)
    cselectLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    cselectBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)
    fselectButton = Button(complexesFrame, text="Delete", command=deleteClick)
    fselectButton.grid(row=1,column=2,stick=W)

    mycursor.execute("SELECT ComplexID FROM Indoor_complex")
    result = mycursor.fetchall()

    cselectBox['values'] = result
    cselectBox['state'] = 'readonly'

    doneButton = Button(complexesFrame, text="Done", command=doneClick)
    doneButton.grid(row=2, columnspan=3)

    return


def modClick():
    originalid = modESelectBox.get()
    newid = modidBox.get()

    # Keep original values the same if not modified
    if newid == '':
        newid = originalid

    newaddnum = modaddressBox.get()
    if newaddnum == '':
        mycursor.execute("SELECT Address_nbr FROM Indoor_complex WHERE ComplexID="+originalid)
        newaddnum = str(mycursor.fetchall()[0][0])

    newst = modstBox.get()
    if newst == '':
        mycursor.execute("SELECT Street_name FROM Indoor_complex WHERE ComplexID="+originalid)
        newst = str(mycursor.fetchall()[0][0])

    # Update table
    try:
        sql_update_query = """UPDATE Indoor_complex SET ComplexID=%s, Address_nbr=%s, Street_name=%s WHERE ComplexID=%s"""
        data_tuple = (newid,newaddnum,newst,originalid)
        mycursor.execute(sql_update_query, data_tuple)
    except:
        showerror(title="Error", message="Invalid input. Please try again.")
    return

def modComplex():
    for w in complexesFrame.winfo_children():
        w.destroy()

    eselectLabel = Label(complexesFrame,text="Select Complex: ")
    global modESelectBox
    mVal = ""
    modESelectBox = Combobox(complexesFrame, width = 30, textvariable = mVal)
    eselectLabel.grid(row=0,column=0,sticky=E,padx=5,pady=10)
    modESelectBox.grid(row=0,column=1,sticky=E+W,padx=5,pady=10)

    mycursor.execute("SELECT ComplexID FROM Indoor_complex")
    result = mycursor.fetchall()

    modESelectBox['values'] = tuple(result)
    modESelectBox['state'] = 'readonly'

    # ID
    idLabel = Label(complexesFrame,text="Set ComplexID: ")
    global modidBox
    id = ""
    modidBox = Entry(complexesFrame, width = 30, textvariable = id)
    idLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    modidBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)

    # Addr Number
    addressLabel = Label(complexesFrame,text="Set Address Number: ")
    global modaddressBox
    address = ""
    modaddressBox = Entry(complexesFrame, width = 30, textvariable = address)
    addressLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
    modaddressBox.grid(row=2,column=1,sticky=E+W,padx=5,pady=10)

    # Street name
    stLabel = Label(complexesFrame,text="Set Street Name: ")
    global modstBox
    st = ""
    modstBox = Entry(complexesFrame, width = 30, textvariable = st)
    stLabel.grid(row=3,column=0,sticky=E,padx=5,pady=10)
    modstBox.grid(row=3,column=1,sticky=E+W,padx=5,pady=10)


    modButton = Button(complexesFrame, text="Update", command=modClick)
    modButton.grid(row=4,columnspan=2)

    doneButton = Button(complexesFrame, text="Done", command=doneClick)
    doneButton.grid(row=5,columnspan=2)

    return


def addClick():
    eid = idBox.get()
    addNum = addressBox.get()
    stName = stBox.get()

    try:
        sql_insert_query = """INSERT INTO Indoor_complex VALUES (%s, %s, %s)"""
        data_tuple = (eid,addNum,stName)
        mycursor.execute(sql_insert_query, data_tuple)
    except:
        showerror(title="Error", message="Invalid input. Please try again.")
    return

def addComplex():
    for w in complexesFrame.winfo_children():
        w.destroy()

    # ID
    idLabel = Label(complexesFrame,text="ComplexID: ")
    global idBox
    id = ""
    idBox = Entry(complexesFrame, width = 30, textvariable = id)
    idLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    idBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)

    # Addr Number
    addressLabel = Label(complexesFrame,text="Address Number: ")
    global addressBox
    address = ""
    addressBox = Entry(complexesFrame, width = 30, textvariable = address)
    addressLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
    addressBox.grid(row=2,column=1,sticky=E+W,padx=5,pady=10)

    # Street name
    stLabel = Label(complexesFrame,text="Street Name: ")
    global stBox
    st = ""
    stBox = Entry(complexesFrame, width = 30, textvariable = st)
    stLabel.grid(row=3,column=0,sticky=E,padx=5,pady=10)
    stBox.grid(row=3,column=1,sticky=E+W,padx=5,pady=10)

    addButton = Button(complexesFrame, text="Add", command=addClick)
    addButton.grid(row=4,columnspan=2)

    doneButton = Button(complexesFrame, text="Done", command=doneClick)
    doneButton.grid(row=5, columnspan=2)

    return

#################################################


def set_complexes_frame(sFrame):
    global complexesFrame
    complexesFrame = sFrame

    delB = Button(complexesFrame,text="Delete a Complex",command=delComplex)
    delB.grid(column = 0, row = 0, padx=5, pady=5, sticky=N+W)
    modB = Button(complexesFrame,text="Modify a Complex",command=modComplex)
    modB.grid(column = 0, row = 1, padx=5, pady=5, sticky=N+W)
    addB = Button(complexesFrame,text="Add a Complex",command=addComplex)
    addB.grid(column = 0, row = 2, padx=5, pady=5, sticky=N+W)

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
