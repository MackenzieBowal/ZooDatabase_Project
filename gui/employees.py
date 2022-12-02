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
    employeeLabel.grid(column = 1, row = 2, padx=300, pady=20, sticky=S+E+W)
    nameLabel = Label(employeesFrame, text="Name: ")
    nameLabel.grid(column = 1, row = 3, padx=300, pady=20, sticky=N+S+E+W)
    addressLabel = Label(employeesFrame, text="Address: ")
    addressLabel.grid(column = 1, row = 4, padx=300, pady=20, sticky=N+S+E+W)
    emailLabel = Label(employeesFrame, text="Email: ")
    emailLabel.grid(column = 1, row = 5, padx=300, pady=20, sticky=N+S+E+W)
    phoneLabel = Label(employeesFrame, text="Phone: ")
    phoneLabel.grid(column = 1, row = 6, padx=300, pady=20, sticky=N+S+E+W)
    startdateLabel = Label(employeesFrame, text="Start Date: ")
    startdateLabel.grid(column = 1, row = 6, padx=300, pady=20, sticky=N+S+E+W)
