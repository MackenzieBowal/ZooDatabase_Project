from ctypes import alignment
from tkinter import *
from tkinter.messagebox import showerror
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



#################################################

def doneClick():
    for w in storesFrame.winfo_children():
        w.destroy()
    set_stores_frame(storesFrame, True)
    return

def deleteClick():
    delValue = cselectBox.get()
    mycursor.execute("DELETE FROM Store WHERE Store_name='" + delValue +"'")
    return

def delStore():
    # Refresh the page
    for w in storesFrame.winfo_children():
        w.destroy()

    # create delete page
    cselectLabel = Label(storesFrame,text="Select Store: ")
    global cselectBox
    delValue = ""
    cselectBox = Combobox(storesFrame, width = 30, textvariable = delValue)
    cselectLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    cselectBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)
    fselectButton = Button(storesFrame, text="Delete", command=deleteClick)
    fselectButton.grid(row=1,column=2,stick=W)

    mycursor.execute("SELECT Store_name FROM Store")
    result = mycursor.fetchall()
    newResult = []
    for x in result:
        store = x[0]
        newResult.append(store)

    cselectBox['values'] = newResult
    cselectBox['state'] = 'readonly'

    doneButton = Button(storesFrame, text="Done", command=doneClick)
    doneButton.grid(row=2, columnspan=3)

    return


def modClick():
    originalid = modESelectBox.get()
    newid = modidBox.get()

    # Keep original values the same if not modified
    if newid == '':
        newid = originalid

    newtype = modtypeBox.get()
    if newtype == '':
        mycursor.execute("SELECT Type FROM Store WHERE Store_name='"+originalid+"'")
        result = mycursor.fetchall()
        for x in result:
            store = x[0]
            newtype = store
    
    print(newtype)
    print(newid)

    # Update table
    try:
        mycursor.execute("UPDATE Store SET \
            Store_name='"+newid+"', Type='"+newtype+"' WHERE Store_name='" + originalid+"'")
    except:
        showerror(title="Error", message="Invalid Name or Type input. Please try again.")

    # Update daily_revenue table
    newdate = str(moddateBox.get())
    newrev = modrevBox.get()
    if newdate != '' and newrev != '':

        try:
            mycursor.execute("INSERT INTO Daily_revenue VALUES ('"+newdate+"', '"+newrev+"', '"+newid+"')")
        except:
            try:
                mycursor.execute("UPDATE Daily_revenue SET Date='"+newdate+"', Store_name='"+newid+"', Revenue='"+newrev+"' \
                    WHERE Date='"+newdate+"' AND Store_name='"+newid+"'")
            except:
                showerror(title="Error", message="Invalid Revenue Information input. Please try again.")

    return

def modStore():
    for w in storesFrame.winfo_children():
        w.destroy()

    eselectLabel = Label(storesFrame,text="Select Store: ")
    global modESelectBox
    mVal = ""
    modESelectBox = Combobox(storesFrame, width = 30, textvariable = mVal)
    eselectLabel.grid(row=0,column=0,sticky=E,padx=5,pady=10)
    modESelectBox.grid(row=0,column=1,sticky=E+W,padx=5,pady=10)

    mycursor.execute("SELECT Store_name FROM Store")
    result = mycursor.fetchall()
    newResult = []
    for x in result:
        store = x[0]
        newResult.append(store)

    modESelectBox['values'] = tuple(newResult)
    modESelectBox['state'] = 'readonly'

    # ID
    idLabel = Label(storesFrame,text="Set Store Name: ")
    global modidBox
    id = ""
    modidBox = Entry(storesFrame, width = 30, textvariable = id)
    idLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    modidBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)

    # Type
    typeLabel = Label(storesFrame,text="Set Type: ")
    global modtypeBox
    type = ""
    modtypeBox = Entry(storesFrame, width = 30, textvariable = type)
    typeLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
    modtypeBox.grid(row=2,column=1,sticky=E+W,padx=5,pady=10)

    # revenue date
    dateLabel = Label(storesFrame,text="Record Date (yyyy-mm-dd): ")
    global moddateBox
    date = ""
    moddateBox = Entry(storesFrame, width = 30, textvariable = date)
    dateLabel.grid(row=3,column=0,sticky=E,padx=5,pady=10)
    moddateBox.grid(row=3,column=1,sticky=E+W,padx=5,pady=10)

    # revenue amount
    revLabel = Label(storesFrame,text="Record Revenue: ")
    global modrevBox
    rev = ""
    modrevBox = Entry(storesFrame, width = 30, textvariable = rev)
    revLabel.grid(row=4,column=0,sticky=E,padx=5,pady=10)
    modrevBox.grid(row=4,column=1,sticky=E+W,padx=5,pady=10)


    modButton = Button(storesFrame, text="Update", command=modClick)
    modButton.grid(row=5,columnspan=2)

    doneButton = Button(storesFrame, text="Done", command=doneClick)
    doneButton.grid(row=6,columnspan=2)

    return


def addClick():
    eid = idBox.get()
    type = typeBox.get()

    try:
        mycursor.execute("INSERT INTO Store \
                VALUES ('"+eid+"', '"+type+"')")
    except:
        showerror(title="Error", message="Invalid input. Please try again.")
    return

def addStore():
    for w in storesFrame.winfo_children():
        w.destroy()

    # ID
    idLabel = Label(storesFrame,text="Store Name: ")
    global idBox
    id = ""
    idBox = Entry(storesFrame, width = 30, textvariable = id)
    idLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    idBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)

    # Addr Number
    typeLabel = Label(storesFrame,text="Type: ")
    global typeBox
    type = ""
    typeBox = Entry(storesFrame, width = 30, textvariable = type)
    typeLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
    typeBox.grid(row=2,column=1,sticky=E+W,padx=5,pady=10)

    addButton = Button(storesFrame, text="Add", command=addClick)
    addButton.grid(row=3,columnspan=2)

    doneButton = Button(storesFrame, text="Done", command=doneClick)
    doneButton.grid(row=4, columnspan=2)

    return

#################################################



def set_stores_frame(sFrame, e):
    global storesFrame
    storesFrame = sFrame

    global editable
    editable = e

    if editable:
        delB = Button(storesFrame,text="Delete a Store",command=delStore)
        delB.grid(column = 0, row = 0, padx=5, pady=5, sticky=N+W)
        modB = Button(storesFrame,text="Modify a Store/Record Revenue",command=modStore)
        modB.grid(column = 0, row = 1, padx=5, pady=5, sticky=N+W)
        addB = Button(storesFrame,text="Add a Store",command=addStore)
        addB.grid(column = 0, row = 2, padx=5, pady=5, sticky=N+W)


    text = Label(storesFrame, text="Browse Stores")
    text.grid(column = 1, row = 0, sticky=S+N+E+W, ipadx=100, ipady=20)
    global storeSelection
    currValue = StringVar()
    storeSelection = Combobox(storesFrame, width = 30, textvariable = currValue)
    storeSelection.grid(column = 1, row = 1, padx=100, pady=20, sticky=N+S+E+W)

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
    storeLabel.grid(column = 1, row = 2, padx=100, pady=20, sticky=S+E+W)
    typeLabel = Label(storesFrame, text="Type: ")
    typeLabel.grid(column = 1, row = 3, padx=100, pady=20, sticky=N+S+E+W)
    dailyrevenueText = ScrolledText(storesFrame, height=8)
    dailyrevenueText.grid(column =2, row = 2, rowspan=3, pady=20, sticky=N+S+E+W)
    dailyrevenueText.insert('1.0', "Daily Revenue:\n")
    dailyrevenueText['state'] = 'normal'
