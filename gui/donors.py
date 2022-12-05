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

#################################################

def doneClick():
    for w in donorsFrame.winfo_children():
        w.destroy()
    set_donors_frame(donorsFrame, False)
    return

def deleteClick():
    delValue = cselectBox.get()
    mycursor.execute("DELETE FROM Donor WHERE DonorID=" + delValue)
    return

def delDonor():
    # Refresh the page
    for w in donorsFrame.winfo_children():
        w.destroy()

    # create delete page
    cselectLabel = Label(donorsFrame,text="Select Donor: ")
    global cselectBox
    delValue = ""
    cselectBox = Combobox(donorsFrame, width = 30, textvariable = delValue)
    cselectLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    cselectBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)
    fselectButton = Button(donorsFrame, text="Delete", command=deleteClick)
    fselectButton.grid(row=1,column=2,stick=W)

    mycursor.execute("SELECT DonorID FROM Donor")
    result = mycursor.fetchall()

    cselectBox['values'] = result
    cselectBox['state'] = 'readonly'

    doneButton = Button(donorsFrame, text="Done", command=doneClick)
    doneButton.grid(row=2, columnspan=3)

    return


def modClick():
    originalid = modESelectBox.get()
    newid = modidBox.get()

    # Keep original values the same if not modified
    if newid == '':
        newid = originalid

    newname = modnameBox.get()
    if newname == '':
        mycursor.execute("SELECT Name FROM Donor WHERE DonorID="+originalid)
        newname = str(mycursor.fetchall()[0][0])

    newphone = modphoneBox.get()
    if newphone == '':
        mycursor.execute("SELECT Phone_number FROM Donor WHERE DonorID="+originalid)
        newphone = str(mycursor.fetchall()[0][0])

    newemail = modemailBox.get()
    if newemail == '':
        mycursor.execute("SELECT Email FROM Donor WHERE DonorID="+originalid)
        newemail = str(mycursor.fetchall()[0][0])

    newaddress = modaddressBox.get()
    if newaddress == '':
        mycursor.execute("SELECT Address FROM Donor WHERE DonorID="+originalid)
        newaddress = str(mycursor.fetchall()[0][0])

    newamt = modamtBox.get()
    if newamt == '':
        newamt = 0
    else:
        newamt = int(newamt)
    mycursor.execute("SELECT Amount_donated FROM Donor WHERE DonorID="+originalid)
    newamt = newamt + int(mycursor.fetchall()[0][0])

    # Update table
    try:
        sql_update_query = """UPDATE Donor SET DonorID=%s, Name=%s, Phone_number=%s, Email=%s, Address=%s, Amount_donated=%s WHERE DonorID=%s"""
        data_tuple = (newid,newname,newphone,newemail,newaddress,newamt,originalid)
        mycursor.execute(sql_update_query, data_tuple)
    except:
        showerror(title="Error", message="Invalid input. Please try again.")
    return

def modDonor():
    for w in donorsFrame.winfo_children():
        w.destroy()

    eselectLabel = Label(donorsFrame,text="Select Donor: ")
    global modESelectBox
    mVal = ""
    modESelectBox = Combobox(donorsFrame, width = 30, textvariable = mVal)
    eselectLabel.grid(row=0,column=0,sticky=E,padx=5,pady=10)
    modESelectBox.grid(row=0,column=1,sticky=E+W,padx=5,pady=10)

    mycursor.execute("SELECT DonorID FROM Donor")
    result = mycursor.fetchall()

    modESelectBox['values'] = tuple(result)
    modESelectBox['state'] = 'readonly'

    # ID
    idLabel = Label(donorsFrame,text="Set DonorID: ")
    global modidBox
    id = ""
    modidBox = Entry(donorsFrame, width = 30, textvariable = id)
    idLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    modidBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)

    # Name
    nameLabel = Label(donorsFrame,text="Set Name: ")
    global modnameBox
    name = ""
    modnameBox = Entry(donorsFrame, width = 30, textvariable = name)
    nameLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
    modnameBox.grid(row=2,column=1,sticky=E+W,padx=5,pady=10)

    # Address
    addressLabel = Label(donorsFrame,text="Set Address: ")
    global modaddressBox
    address = ""
    modaddressBox = Entry(donorsFrame, width = 30, textvariable = address)
    addressLabel.grid(row=3,column=0,sticky=E,padx=5,pady=10)
    modaddressBox.grid(row=3,column=1,sticky=E+W,padx=5,pady=10)

    # Email
    emailLabel = Label(donorsFrame,text="Set Email: ")
    global modemailBox
    email = ""
    modemailBox = Entry(donorsFrame, width = 30, textvariable = email)
    emailLabel.grid(row=4,column=0,sticky=E,padx=5,pady=10)
    modemailBox.grid(row=4,column=1,sticky=E+W,padx=5,pady=10)

    # Phone
    phoneLabel = Label(donorsFrame,text="Set Phone: ")
    global modphoneBox
    phone = ""
    modphoneBox = Entry(donorsFrame, width = 30, textvariable = phone)
    phoneLabel.grid(row=5,column=0,sticky=E,padx=5,pady=10)
    modphoneBox.grid(row=5,column=1,sticky=E+W,padx=5,pady=10)

    # Phone
    amtLabel = Label(donorsFrame,text="Change donation amount by: ")
    global modamtBox
    amt = ""
    modamtBox = Entry(donorsFrame, width = 30, textvariable = amt)
    amtLabel.grid(row=6,column=0,sticky=E,padx=5,pady=10)
    modamtBox.grid(row=6,column=1,sticky=E+W,padx=5,pady=10)

    modButton = Button(donorsFrame, text="Update", command=modClick)
    modButton.grid(row=7,columnspan=2)

    doneButton = Button(donorsFrame, text="Done", command=doneClick)
    doneButton.grid(row=8,columnspan=2)

    return


def addClick():
    eid = idBox.get()
    name = nameBox.get()
    address = addressBox.get()
    email = emailBox.get()
    phone = phoneBox.get()
    amt = amtBox.get()

    try:
        sql_insert_query = """INSERT INTO Donor VALUES (%s, %s, %s, %s, %s, %s)"""
        data_tuple = (eid,name,address,email,phone,amt)
        mycursor.execute(sql_insert_query, data_tuple)
    except:
        showerror(title="Error", message="Invalid input. Please try again.")
    return

def addDonor():
    for w in donorsFrame.winfo_children():
        w.destroy()

    # ID
    idLabel = Label(donorsFrame,text="DonorID: ")
    global idBox
    id = ""
    idBox = Entry(donorsFrame, width = 30, textvariable = id)
    idLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    idBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)

    # Name
    nameLabel = Label(donorsFrame,text="Name: ")
    global nameBox
    name = ""
    nameBox = Entry(donorsFrame, width = 30, textvariable = name)
    nameLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
    nameBox.grid(row=2,column=1,sticky=E+W,padx=5,pady=10)

    # Address
    addressLabel = Label(donorsFrame,text="Address: ")
    global addressBox
    address = ""
    addressBox = Entry(donorsFrame, width = 30, textvariable = address)
    addressLabel.grid(row=3,column=0,sticky=E,padx=5,pady=10)
    addressBox.grid(row=3,column=1,sticky=E+W,padx=5,pady=10)

    # Email
    emailLabel = Label(donorsFrame,text="Email: ")
    global emailBox
    email = ""
    emailBox = Entry(donorsFrame, width = 30, textvariable = email)
    emailLabel.grid(row=4,column=0,sticky=E,padx=5,pady=10)
    emailBox.grid(row=4,column=1,sticky=E+W,padx=5,pady=10)

    # Phone
    phoneLabel = Label(donorsFrame,text="Phone: ")
    global phoneBox
    phone = ""
    phoneBox = Entry(donorsFrame, width = 30, textvariable = phone)
    phoneLabel.grid(row=5,column=0,sticky=E,padx=5,pady=10)
    phoneBox.grid(row=5,column=1,sticky=E+W,padx=5,pady=10)

    # Amount donated
    amtLabel = Label(donorsFrame,text="Donation amount: ")
    global amtBox
    amt = ""
    amtBox = Entry(donorsFrame, width = 30, textvariable = amt)
    amtLabel.grid(row=6,column=0,sticky=E,padx=5,pady=10)
    amtBox.grid(row=6,column=1,sticky=E+W,padx=5,pady=10)

    addButton = Button(donorsFrame, text="Add", command=addClick)
    addButton.grid(row=7,columnspan=2)

    doneButton = Button(donorsFrame, text="Done", command=doneClick)
    doneButton.grid(row=8, columnspan=2)

    return

#################################################


def set_donors_frame(sFrame, lv):
    global donorsFrame
    donorsFrame = sFrame

    global limitedView
    limitedView = lv

    if (not limitedView):
        delB = Button(donorsFrame,text="Delete a Donor",command=delDonor)
        delB.grid(column = 0, row = 0, padx=5, pady=5, sticky=N+W)
        modB = Button(donorsFrame,text="Modify a Donor",command=modDonor)
        modB.grid(column = 0, row = 1, padx=5, pady=5, sticky=N+W)
        addB = Button(donorsFrame,text="Add a Donor",command=addDonor)
        addB.grid(column = 0, row = 2, padx=5, pady=5, sticky=N+W)


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

