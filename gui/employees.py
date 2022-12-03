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

def show_employee(event):
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

def show_other(employee):
    #Erase the details of any previous zookeeper/manager that are still on the screen
    if previousEmployee == "zookeeper":
        specializationLabel.destroy()
        caresforLabel.destroy()
    elif previousEmployee == "manager":
        previousroleLabel.destroy()
        overlooksLabel.destroy()

def set_employees_frame(sFrame):
    global employeesFrame
    employeesFrame = sFrame

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
    employeeLabel.grid(column = 0, row = 2, pady=20, sticky=S+E+W)
    nameLabel = Label(employeesFrame, text="Name: ")
    nameLabel.grid(column = 0, row = 3, pady=20, sticky=N+S+E+W)
    addressLabel = Label(employeesFrame, text="Address: ")
    addressLabel.grid(column = 0, row = 4, pady=20, sticky=N+S+E+W)
    emailLabel = Label(employeesFrame, text="Email: ")
    emailLabel.grid(column = 0, row = 5, pady=20, sticky=N+S+E+W)
    phoneLabel = Label(employeesFrame, text="Phone: ")
    phoneLabel.grid(column = 0, row = 6, pady=20, sticky=N+S+E+W)
    startdateLabel = Label(employeesFrame, text="Start Date: ")
    startdateLabel.grid(column = 0, row = 7, pady=20, sticky=N+S+E+W)

    global previousEmployee #Tracks whether a zookeeper or manager was previously selected
    previousEmployee = ""
