from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
import mysql.connector

from receptionist import handle_receptionist_page
from entertainer import handle_entertainer_page
from zookeeper import handle_zookeeper_page
from manager import handle_manager_page
from storeemployee import handle_storeemployee_page

# Create a connection to the database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "zoodatabase"
)

mycursor = mydb.cursor()

def clear_fields():
    employeeidBox.delete(0, 'end')
    passwordBox.delete(0, 'end')
    empTypeBox.current(0)

def backClicked():
    signinPage.destroy()
    backFrame.place(relwidth=1,relheight=1)

def handle_signin_page(w, b):
    global window
    window = w

    global backFrame
    backFrame = b

    global signinPage
    signinPage = Frame(window)

    backButton = Button(signinPage, text="Back", command=backClicked)

    signinMessage = Label(signinPage,text="Please sign in to access the system.")
    signinMessage.grid(row=0,column=0,columnspan=2,sticky=N+S+W+E,padx=5,pady=10)

    employeeid = StringVar()
    employeeidLabel = Label(signinPage,text="EmployeeID")
    global employeeidBox
    employeeidBox = Entry(signinPage,textvariable=employeeid)
    employeeidLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
    employeeidBox.grid(row=1,column=1,sticky=W,padx=5,pady=10)

    password = StringVar()
    passwordLabel = Label(signinPage,text="Password")
    global passwordBox
    passwordBox = Entry(signinPage,textvariable=password,show='*')
    passwordLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
    passwordBox.grid(row=2,column=1,sticky=W,padx=5,pady=10)

    employeeType = StringVar()
    empTypeLabel = Label(signinPage,text="Employee Type")
    global empTypeBox
    empTypeBox = ttk.Combobox(signinPage,textvariable=employeeType)
    empTypeBox['values'] = ("", "Receptionist","Entertainer","Zookeeper","Manager","Store Employee")
    empTypeBox['state'] = 'readonly'
    empTypeLabel.grid(row=3,column=0,sticky=E,padx=5,pady=10)
    empTypeBox.grid(row=3,column=1,sticky=W,padx=5,pady=10)

    signinButton = Button(signinPage,text="Sign In",command=signin)
    signinButton.grid(row=4,column=1,sticky=W,padx=5,pady=10)

    signinPage.rowconfigure(0,weight=3)
    signinPage.rowconfigure(1,weight=1)
    signinPage.rowconfigure(2,weight=1)
    signinPage.rowconfigure(3,weight=1)
    signinPage.columnconfigure(0,weight=1)
    signinPage.columnconfigure(1,weight=1)

    signinPage.place(relwidth=1,relheight=1)

    employeeidBox.focus()

def signin():
    global eid
    eid = employeeidBox.get()
    pwd = passwordBox.get()
    etype = empTypeBox.get()
    mycursor.execute("SELECT * FROM Emp_signin")
    result = mycursor.fetchall()
    if (eid,pwd) not in result:
        showerror(title="Error",message="Invalid username/password combination, or incorrect employee type. Please try again.")
    elif etype == "Store Employee":
        mycursor.execute("SELECT * FROM Other_employee WHERE EmployeeID = %s"%eid)
        result = mycursor.fetchall()
        if len(result) == 0:
            showerror(title="Error",message="Invalid username/password combination, or incorrect employee type. Please try again.")
        else:
            clear_fields()
            goto_employee(etype,eid)
    else: #etype != "Store Employee"
        mycursor.execute("SELECT * FROM %s WHERE EmployeeID = %s"%(etype,eid))
        result = mycursor.fetchall()
        if len(result) == 0:
            showerror(title="Error",message="Invalid username/password combination, or incorrect employee type. Please try again.")
        else:
            clear_fields()
            goto_employee(etype,eid)

#Switch to the homepage for the selected employee type
def goto_employee(etype,eid):
    if etype == "Receptionist":
        handle_receptionist_page(window,eid,signinPage)
    elif etype == "Entertainer":
        handle_entertainer_page(window,eid,signinPage)
    elif etype == "Zookeeper":
        handle_zookeeper_page(window,eid,signinPage)
    elif etype == "Manager":
        handle_manager_page(window,eid,signinPage)
    elif etype == "Store Employee":
        handle_storeemployee_page(window,eid,signinPage)

#A list of valid (employeeID, password, employee type) combinations
employees = [("12345","password1"),("23456","password2"),
            ("34567","password3"),("45678","password4"),("56789","password5")]