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

mycursor = mydb.cursor()

def show_employee(event):

    """
    global worksAtStoreLabel
    worksAtStoreLabel = Label(employeesFrame, text="Works at store: ")
    worksAtStoreLabel.grid(row=8)



    #Erase the details of any previous zookeeper/manager that are still on the screen
    if previousEmployee == "storeEmp":
        worksAtStoreLabel.destroy()

    """

    employee = employeeSelection.get()
    employeeLabel.config(text="Employee ID: " + employee)

    mycursor.execute("SELECT Name FROM Employee WHERE EmployeeID = '%s'"%employee)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    nameLabel.config(text="Name: " + result)

    mycursor.execute("SELECT Address FROM Employee WHERE EmployeeID = '%s'"%employee)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    addressLabel.config(text="Address: " + result)

    mycursor.execute("SELECT Email FROM Employee WHERE EmployeeID = '%s'"%employee)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    emailLabel.config(text="Email: " + result)

    mycursor.execute("SELECT Phone_number FROM Employee WHERE EmployeeID = '%s'"%employee)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    phoneLabel.config(text="Phone: " + result)

    mycursor.execute("SELECT Start_date FROM Employee WHERE EmployeeID = '%s'"%employee)
    result = str(mycursor.fetchall()[0][0])
    if result == "None":
        result = "N/A"
    startdateLabel.config(text="Start Date: " + result)

    '''
    mycursor.execute("SELECT * FROM Zookeeper WHERE EmployeeID = '%s'"%employee)
    result = mycursor.fetchall()
    if len(result) > 0: #Employee is a zookeeper
        show_zookeeper(employee)
    else:
        mycursor.execute("SELECT * FROM Manager WHERE EmployeeID = '%s'"%employee)
        result = mycursor.fetchall()
        if len(result) > 0: #Employee is a manager
            show_manager(employee)
        else: #Employee has some other role
            show_other(employee)
    '''

"""
def show_zookeeper(employee):
    global previousEmployee
    global specializationLabel
    global caresforLabel

    #Erase the details of any previous zookeeper/manager that are still on the screen
    if previousEmployee == "zookeeper":
        specializationLabel.destroy()
        caresforLabel.destroy()
    elif previousEmployee == "manager":
        previousroleLabel.destroy()
        overlooksLabel.destroy()

    previousEmployee = "zookeeper"

    specializationLabel = Label(employeesFrame, text="Specialization: ")
    specializationLabel.grid(column = 1, row = 2, pady=20, sticky=S+E+W)
    caresforLabel = Label(employeesFrame, text="Cares for ")
    caresforLabel.grid(column = 1, row = 3, pady=20, sticky=N+S+E+W)

    mycursor.execute("SELECT Specialization FROM Zookeeper_specialization WHERE Zookeeper_EID = '%s'"%employee)
    result = str(mycursor.fetchall()[0][0])
    specializationLabel.config(text="Specialization: " + result)

    mycursor.execute("SELECT Species_name FROM Cares_for WHERE Zookeeper_EID = '%s'"%employee)
    result = mycursor.fetchall()
    caresforString = "Cares for "
    for species in result:
        caresforString = caresforString + species[0] + " "
    caresforLabel.config(text=caresforString)

def show_manager(employee):
    global previousEmployee
    global previousroleLabel
    global overlooksLabel

    #Erase the details of any previous zookeeper/manager that are still on the screen
    if previousEmployee == "zookeeper":
        specializationLabel.destroy()
        caresforLabel.destroy()
    elif previousEmployee == "manager":
        previousroleLabel.destroy()
        overlooksLabel.destroy()

    previousEmployee = "manager"

    previousroleLabel = Label(employeesFrame, text="Previous Roles: ")
    previousroleLabel.grid(column = 1, row = 2, pady=20, sticky=S+E+W)
    overlooksLabel = Label(employeesFrame, text="Overlooks ")
    overlooksLabel.grid(column = 1, row = 3, pady=20, sticky=N+S+E+W)

    mycursor.execute("SELECT Previous_role FROM Manager_previousrole WHERE Manager_EID = '%s'"%employee)
    result = mycursor.fetchall()
    previousroleString = "Previous Roles: "
    for role in result:
        previousroleString = previousroleString + role[0] + " "
    previousroleLabel.config(text=previousroleString)

    mycursor.execute("SELECT FundraiserID FROM Overlooks WHERE Manager_EID = '%s'"%employee)
    result = mycursor.fetchall()
    overlooksString = "Overlooks fundraisers: "
    for fundraiser in result:
        overlooksString = overlooksString + fundraiser[0] + " "
    overlooksLabel.config(text=overlooksString)
"""
"""
def show_other(employee):
    #Erase the details of any previous zookeeper/manager that are still on the screen
    if previousEmployee == "zookeeper":
        specializationLabel.destroy()
        caresforLabel.destroy()
    elif previousEmployee == "manager":
        previousroleLabel.destroy()
        overlooksLabel.destroy()
"""

#################################################

def doneClick():
    for w in employeesFrame.winfo_children():
        w.destroy()
    set_employees_frame(employeesFrame, managerID)
    return

def deleteClick():
    delValue = eselectBox.get()
    mycursor.execute("DELETE FROM Employee WHERE EmployeeID=" + delValue)
    return

def delEmployee():
    # Refresh the page
    for w in employeesFrame.winfo_children():
        w.destroy()

    # create delete page
    eselectLabel = Label(employeesFrame,text="Select Employee: ")
    global eselectBox
    delValue = ""
    eselectBox = Combobox(employeesFrame, width = 30, textvariable = delValue)
    eselectLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    eselectBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)
    fselectButton = Button(employeesFrame, text="Delete", command=deleteClick)
    fselectButton.grid(row=1,column=2,stick=W)

    mycursor.execute("SELECT EmployeeID FROM Employee")
    result = mycursor.fetchall()

    eselectBox['values'] = result
    eselectBox['state'] = 'readonly'

    doneButton = Button(employeesFrame, text="Done", command=doneClick)
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
        mycursor.execute("SELECT Name FROM Employee WHERE EmployeeID="+originalid)
        newname = str(mycursor.fetchall()[0][0])

    newphone = modphoneBox.get()
    if newphone == '':
        mycursor.execute("SELECT Phone_number FROM Employee WHERE EmployeeID="+originalid)
        newphone = str(mycursor.fetchall()[0][0])

    newemail = modemailBox.get()
    if newemail == '':
        mycursor.execute("SELECT Email FROM Employee WHERE EmployeeID="+originalid)
        newemail = str(mycursor.fetchall()[0][0])

    newaddress = modaddressBox.get()
    if newaddress == '':
        mycursor.execute("SELECT Address FROM Employee WHERE EmployeeID="+originalid)
        newaddress = str(mycursor.fetchall()[0][0])

    # Update table
    try:
        mycursor.execute("UPDATE Employee SET \
                EmployeeID='"+newid+"', Name='"+newname+"', Phone_number='"+newphone+"', \
                Email='"+newemail+"', Address='"+newaddress+"' WHERE EmployeeID=" + originalid)
    except:
        showerror(title="Error", message="Invalid input. Please try again.")
    return

def modEmployee():

    for w in employeesFrame.winfo_children():
        w.destroy()

    eselectLabel = Label(employeesFrame,text="Select Employee: ")
    global modESelectBox
    mVal = ""
    modESelectBox = Combobox(employeesFrame, width = 30, textvariable = mVal)
    eselectLabel.grid(row=0,column=0,sticky=E,padx=5,pady=10)
    modESelectBox.grid(row=0,column=1,sticky=E+W,padx=5,pady=10)

    mycursor.execute("SELECT EmployeeID FROM Employee")
    result = mycursor.fetchall()

    modESelectBox['values'] = tuple(result)
    modESelectBox['state'] = 'readonly'

    # ID
    idLabel = Label(employeesFrame,text="Set EmployeeID: ")
    global modidBox
    id = ""
    modidBox = Entry(employeesFrame, width = 30, textvariable = id)
    idLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    modidBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)

    # Name
    nameLabel = Label(employeesFrame,text="Set Name: ")
    global modnameBox
    name = ""
    modnameBox = Entry(employeesFrame, width = 30, textvariable = name)
    nameLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
    modnameBox.grid(row=2,column=1,sticky=E+W,padx=5,pady=10)

    # Address
    addressLabel = Label(employeesFrame,text="Set Address: ")
    global modaddressBox
    address = ""
    modaddressBox = Entry(employeesFrame, width = 30, textvariable = address)
    addressLabel.grid(row=3,column=0,sticky=E,padx=5,pady=10)
    modaddressBox.grid(row=3,column=1,sticky=E+W,padx=5,pady=10)

    # Email
    emailLabel = Label(employeesFrame,text="Set Email: ")
    global modemailBox
    email = ""
    modemailBox = Entry(employeesFrame, width = 30, textvariable = email)
    emailLabel.grid(row=4,column=0,sticky=E,padx=5,pady=10)
    modemailBox.grid(row=4,column=1,sticky=E+W,padx=5,pady=10)

    # Phone
    phoneLabel = Label(employeesFrame,text="Set Phone: ")
    global modphoneBox
    phone = ""
    modphoneBox = Entry(employeesFrame, width = 30, textvariable = phone)
    phoneLabel.grid(row=5,column=0,sticky=E,padx=5,pady=10)
    modphoneBox.grid(row=5,column=1,sticky=E+W,padx=5,pady=10)

    modButton = Button(employeesFrame, text="Update", command=modClick)
    modButton.grid(row=6,columnspan=2)

    doneButton = Button(employeesFrame, text="Done", command=doneClick)
    doneButton.grid(row=7,columnspan=2)

    return


def addClick():
    eid = idBox.get()
    name = nameBox.get()
    address = addressBox.get()
    email = emailBox.get()
    phone = phoneBox.get()
    date = dateBox.get()
    role = roleBox.get()
    #store = storeBox.get()

    try:
        mycursor.execute("INSERT INTO Employee \
                VALUES ('"+eid+"', '"+name+"', '"+address+"', '"+email+"', '"+phone+"', '"+date+"')")
        
        if (role == 'Receptionist'):
                mycursor.execute("INSERT INTO Receptionist VALUES ("+eid+")")
        elif (role == 'Entertainer'):
                mycursor.execute("INSERT INTO Entertainer VALUES ("+eid+")")
        elif (role == 'Zookeeper'):
                mycursor.execute("INSERT INTO Zookeeper VALUES ("+eid+")")
        elif (role == 'Manager'):
                mycursor.execute("INSERT INTO Manager VALUES ("+eid+")")
        elif (role == 'Store Employee'):
                mycursor.execute("INSERT INTO Other_employee VALUES ("+eid+", 'NULL')")
    except:
        showerror(title="Error",message="Invalid input. Please try again.")
    return

def addEmployee():

    for w in employeesFrame.winfo_children():
        w.destroy()

    # ID
    idLabel = Label(employeesFrame,text="EmployeeID: ")
    global idBox
    id = ""
    idBox = Entry(employeesFrame, width = 30, textvariable = id)
    idLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    idBox.grid(row=1,column=1,sticky=E+W,padx=5,pady=10)

    # Name
    nameLabel = Label(employeesFrame,text="Name: ")
    global nameBox
    name = ""
    nameBox = Entry(employeesFrame, width = 30, textvariable = name)
    nameLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
    nameBox.grid(row=2,column=1,sticky=E+W,padx=5,pady=10)

    # Address
    addressLabel = Label(employeesFrame,text="Address: ")
    global addressBox
    address = ""
    addressBox = Entry(employeesFrame, width = 30, textvariable = address)
    addressLabel.grid(row=3,column=0,sticky=E,padx=5,pady=10)
    addressBox.grid(row=3,column=1,sticky=E+W,padx=5,pady=10)

    # Email
    emailLabel = Label(employeesFrame,text="Email: ")
    global emailBox
    email = ""
    emailBox = Entry(employeesFrame, width = 30, textvariable = email)
    emailLabel.grid(row=4,column=0,sticky=E,padx=5,pady=10)
    emailBox.grid(row=4,column=1,sticky=E+W,padx=5,pady=10)

    # Phone
    phoneLabel = Label(employeesFrame,text="Phone: ")
    global phoneBox
    phone = ""
    phoneBox = Entry(employeesFrame, width = 30, textvariable = phone)
    phoneLabel.grid(row=5,column=0,sticky=E,padx=5,pady=10)
    phoneBox.grid(row=5,column=1,sticky=E+W,padx=5,pady=10)

    # Start date
    dateLabel = Label(employeesFrame,text="Start Date (yyyy-mm-dd): ")
    global dateBox
    date = ""
    dateBox = Entry(employeesFrame, width = 30, textvariable = date)
    dateLabel.grid(row=6,column=0,sticky=E,padx=5,pady=10)
    dateBox.grid(row=6,column=1,sticky=E+W,padx=5,pady=10)

    # Role:
    roleLabel = Label(employeesFrame,text="Role: ")
    global roleBox
    role = ""
    roleBox = Combobox(employeesFrame, width = 30, textvariable = role)
    roleBox['values'] = ('Receptionist', 'Entertainer', 'Zookeeper', 'Manager', 'Store Employee')
    roleBox['state'] = 'readonly'
    roleLabel.grid(row=7,column=0,sticky=E,padx=5,pady=10)
    roleBox.grid(row=7,column=1,sticky=E+W,padx=5,pady=10)

    '''
    # Store
    storeLabel = Label(employeesFrame,text="Store (If store employee): ")
    global storeBox
    store = ""
    storeBox = Combobox(employeesFrame, width = 30, textvariable = role)
    mycursor.execute("SELECT Store_name FROM Store")
    sNames = []
    for i in mycursor.fetchall():
        sNames.append(i[0])
    storeBox['values'] = sNames
    storeBox['state'] = 'readonly'
    storeLabel.grid(row=8,column=0,sticky=E,padx=5,pady=10)
    storeBox.grid(row=8,column=1,sticky=E+W,padx=5,pady=10)
    '''

    addButton = Button(employeesFrame, text="Add", command=addClick)
    addButton.grid(row=9,columnspan=2)

    doneButton = Button(employeesFrame, text="Done", command=doneClick)
    doneButton.grid(row=10, columnspan=2)


    return

#################################################

def set_employees_frame(sFrame, mid):
    global employeesFrame
    employeesFrame = sFrame
    global managerID
    managerID = str(mid)

    delB = Button(employeesFrame,text="Delete an Employee",command=delEmployee)
    delB.grid(column = 0, row = 0, padx=5, pady=5, sticky=N+W)
    modB = Button(employeesFrame,text="Modify an Employee",command=modEmployee)
    modB.grid(column = 0, row = 1, padx=5, pady=5, sticky=N+W)
    addB = Button(employeesFrame,text="Add an Employee",command=addEmployee)
    addB.grid(column = 0, row = 2, padx=5, pady=5, sticky=N+W)

    text = Label(employeesFrame, text="Browse employees")
    text.grid(column = 1, row = 0, sticky=S, ipadx=300, ipady=20)
    global employeeSelection
    currValue = StringVar()
    employeeSelection = Combobox(employeesFrame, width = 30, textvariable = currValue)
    employeeSelection.grid(column = 1, row = 1, padx=300, pady=20, sticky=N+S+E+W)

    mycursor.execute("SELECT EmployeeID FROM Employee")
    result = mycursor.fetchall()

    employeeSelection['values'] = result
    employeeSelection['state'] = 'readonly'

    employeeSelection.bind('<<ComboboxSelected>>', show_employee)

    # Create text for employee info
    global employeeLabel
    global nameLabel
    global addressLabel
    global emailLabel
    global phoneLabel
    global startdateLabel

    employeeLabel = Label(employeesFrame, text="Employee ID: None selected")
    employeeLabel.grid(column = 1, row = 2, pady=20, sticky=S+E+W)
    nameLabel = Label(employeesFrame, text="Name: ")
    nameLabel.grid(column = 1, row = 3, pady=20, sticky=N+S+E+W)
    addressLabel = Label(employeesFrame, text="Address: ")
    addressLabel.grid(column = 1, row = 4, pady=20, sticky=N+S+E+W)
    emailLabel = Label(employeesFrame, text="Email: ")
    emailLabel.grid(column = 1, row = 5, pady=20, sticky=N+S+E+W)
    phoneLabel = Label(employeesFrame, text="Phone: ")
    phoneLabel.grid(column = 1, row = 6, pady=20, sticky=N+S+E+W)
    startdateLabel = Label(employeesFrame, text="Start Date: ")
    startdateLabel.grid(column = 1, row = 7, pady=20, sticky=N+S+E+W)

    '''
    global previousEmployee #Tracks whether a zookeeper or manager was previously selected
    previousEmployee = ""
    '''
