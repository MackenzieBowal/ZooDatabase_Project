from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror
import mysql.connector

# Create a connection to the database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "zoodatabase"
)

mycursor = mydb.cursor()

window = Tk() #Create the main window
window.title("Our Zoo Database System") #Set the title of the window
window.geometry("1024x768") #Set the size of the window

#The employee ID of the currently logged-in employee
eid = StringVar()

#A list of valid (employeeID, password, employee type) combinations
employees = [("12345","password1"),("23456","password2"),
            ("34567","password3"),("45678","password4"),("56789","password5")]

def display_signin_page():
    signinPage.place(relwidth=1,relheight=1)

    employeeidBox.focus()

def signin():
    eid.set(employeeidBox.get())
    pwd = passwordBox.get()
    etype = empTypeBox.get()
    if (eid.get(),pwd) not in employees:
        showerror(title="Error",message="Invalid username/password combination, or incorrect employee type. Please try again.")
    elif etype == "Store Employee":
        mycursor.execute("SELECT * FROM Other_employee WHERE EmployeeID = %s"%eid.get())
        result = mycursor.fetchall()
        if len(result) == 0:
            showerror(title="Error",message="Invalid username/password combination, or incorrect employee type. Please try again.")
        else:
            goto_employee(etype)
    else: #etype != "Store Employee"
        mycursor.execute("SELECT * FROM %s WHERE EmployeeID = %s"%(etype,eid.get()))
        result = mycursor.fetchall()
        if len(result) == 0:
            showerror(title="Error",message="Invalid username/password combination, or incorrect employee type. Please try again.")
        else:
            goto_employee(etype)

#Switch to the homepage for the selected employee type
def goto_employee(etype):
    if etype == "Receptionist":
        display_receptionist_page()
    elif etype == "Entertainer":
        display_entertainer_page()
    elif etype == "Zookeeper":
        display_zookeeper_page()
    elif etype == "Manager":
        display_manager(_page)
    elif etype == "Store Employee":
        display_storeemployee_page()

def display_receptionist_page():
    receptionistPage.place(relwidth=1,relheight=1)

    mycursor.execute("SELECT Name FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    nameMessage = Label(receptionistPage,text="Welcome %s"%result[0])
    nameMessage.grid(row=0,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Email FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    emailMessage = Label(receptionistPage,text="Email: %s"%result[0])
    emailMessage.grid(row=1,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Phone_number FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    phoneMessage = Label(receptionistPage,text="Phone: %s"%result[0])
    phoneMessage.grid(row=2,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Address FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    addressMessage = Label(receptionistPage,text="Address: %s"%result[0])
    addressMessage.grid(row=3,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Start_date FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    startdateMessage = Label(receptionistPage,text="You've been working here since %s"%result[0])
    startdateMessage.grid(row=4,column=0,sticky=N+S+W+E,padx=5,pady=10)

def display_entertainer_page():
    entertainerPage.place(relwidth=1,relheight=1)

    mycursor.execute("SELECT Name FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    nameMessage = Label(entertainerPage,text="Welcome %s"%result[0])
    nameMessage.grid(row=0,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Email FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    emailMessage = Label(entertainerPage,text="Email: %s"%result[0])
    emailMessage.grid(row=1,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Phone_number FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    phoneMessage = Label(entertainerPage,text="Phone: %s"%result[0])
    phoneMessage.grid(row=2,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Address FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    addressMessage = Label(entertainerPage,text="Address: %s"%result[0])
    addressMessage.grid(row=3,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Start_date FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    startdateMessage = Label(entertainerPage,text="You've been working here since %s"%result[0])
    startdateMessage.grid(row=4,column=0,sticky=N+S+W+E,padx=5,pady=10)

def display_zookeeper_page():
    zookeeperPage.place(relwidth=1,relheight=1)
    mycursor.execute("SELECT Name FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    nameMessage = Label(zookeeperPage,text="Welcome %s"%result[0])
    nameMessage.grid(row=0,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Email FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    emailMessage = Label(zookeeperPage,text="Email: %s"%result[0])
    emailMessage.grid(row=1,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Phone_number FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    phoneMessage = Label(zookeeperPage,text="Phone: %s"%result[0])
    phoneMessage.grid(row=2,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Address FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    addressMessage = Label(zookeeperPage,text="Address: %s"%result[0])
    addressMessage.grid(row=3,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Start_date FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    startdateMessage = Label(zookeeperPage,text="You've been working here since %s"%result[0])
    startdateMessage.grid(row=4,column=0,sticky=N+S+W+E,padx=5,pady=10)

def display_manager_page():
    managerPage.place(relwidth=1,relheight=1)

    mycursor.execute("SELECT Name FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    nameMessage = Label(managerPage,text="Welcome %s"%result[0])
    nameMessage.grid(row=0,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Email FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    emailMessage = Label(managerPage,text="Email: %s"%result[0])
    emailMessage.grid(row=1,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Phone_number FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    phoneMessage = Label(managerPage,text="Phone: %s"%result[0])
    phoneMessage.grid(row=2,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Address FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    addressMessage = Label(managerPage,text="Address: %s"%result[0])
    addressMessage.grid(row=3,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Start_date FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    startdateMessage = Label(managerPage,text="You've been working here since %s"%result[0])
    startdateMessage.grid(row=4,column=0,sticky=N+S+W+E,padx=5,pady=10)

def display_storeemployee_page():
    storeemployeePage.place(relwidth=1,relheight=1)

    mycursor.execute("SELECT Name FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    nameMessage = Label(storeemployeePage,text="Welcome %s"%result[0])
    nameMessage.grid(row=0,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Email FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    emailMessage = Label(storeemployeePage,text="Email: %s"%result[0])
    emailMessage.grid(row=1,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Phone_number FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    phoneMessage = Label(storeemployeePage,text="Phone: %s"%result[0])
    phoneMessage.grid(row=2,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Address FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    addressMessage = Label(storeemployeePage,text="Address: %s"%result[0])
    addressMessage.grid(row=3,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Start_date FROM Employee WHERE EmployeeID = %s"%eid.get())
    result = mycursor.fetchall()
    startdateMessage = Label(storeemployeePage,text="You've been working here since %s"%result[0])
    startdateMessage.grid(row=4,column=0,sticky=N+S+W+E,padx=5,pady=10)

#Welcome page
welcomePage = Frame(window)

welcomeMessage = Label(welcomePage,text="Welcome to the Zoo!\nPlease log in to continue.")
employeeButton = Button(welcomePage,text="Employee",command=display_signin_page)
visitorButton = Button(welcomePage,text="Visitor")

welcomeMessage.grid(row=0,column=0,columnspan=2,sticky=N+S+W+E,padx=5)
employeeButton.grid(row=1,column=0,sticky=N+S+W+E,padx=10,pady=5)
visitorButton.grid(row=1,column=1,sticky=N+S+W+E,padx=10,pady=5)

#Configure the grid elements to expand to fill extra space
welcomePage.rowconfigure(0,weight=1)
welcomePage.rowconfigure(1,weight=1)
welcomePage.columnconfigure(0,weight=1)
welcomePage.columnconfigure(1,weight=1)

#Sign-in page
signinPage = Frame(window)

signinMessage = Label(signinPage,text="Please sign in to access the system.")
signinMessage.grid(row=0,column=0,columnspan=2,sticky=N+S+W+E,padx=5,pady=10)

employeeid = StringVar()
employeeidLabel = Label(signinPage,text="EmployeeID")
employeeidBox = Entry(signinPage,textvariable=employeeid)
employeeidLabel.grid(row=1,column=0,sticky=E,padx=5,pady=10)
employeeidBox.grid(row=1,column=1,sticky=W,padx=5,pady=10)

password = StringVar()
passwordLabel = Label(signinPage,text="Password")
passwordBox = Entry(signinPage,textvariable=password,show='*')
passwordLabel.grid(row=2,column=0,sticky=E,padx=5,pady=10)
passwordBox.grid(row=2,column=1,sticky=W,padx=5,pady=10)

employeetype = StringVar()
empTypeLabel = Label(signinPage,text="Employee Type")
empTypeBox = ttk.Combobox(signinPage,textvariable=employeetype)
empTypeBox['values'] = ("Receptionist","Entertainer","Zookeeper","Manager","Store Employee")
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

#Receptionist page
receptionistPage = Frame(window)

receptionistPage.rowconfigure(0,weight=1)
receptionistPage.rowconfigure(1,weight=1)
receptionistPage.rowconfigure(2,weight=1)
receptionistPage.rowconfigure(3,weight=1)
receptionistPage.rowconfigure(4,weight=1)
receptionistPage.columnconfigure(0,weight=1)

#Entertainer page
entertainerPage = Frame(window)

entertainerPage.rowconfigure(0,weight=1)
entertainerPage.rowconfigure(1,weight=1)
entertainerPage.rowconfigure(2,weight=1)
entertainerPage.rowconfigure(3,weight=1)
entertainerPage.rowconfigure(4,weight=1)
entertainerPage.columnconfigure(0,weight=1)

#Zookeeper page
zookeeperPage = Frame(window)

zookeeperPage.rowconfigure(0,weight=1)
zookeeperPage.rowconfigure(1,weight=1)
zookeeperPage.rowconfigure(2,weight=1)
zookeeperPage.rowconfigure(3,weight=1)
zookeeperPage.rowconfigure(4,weight=1)
zookeeperPage.columnconfigure(0,weight=1)

#Manager page
managerPage = Frame(window)

managerPage.rowconfigure(0,weight=1)
managerPage.rowconfigure(1,weight=1)
managerPage.rowconfigure(2,weight=1)
managerPage.rowconfigure(3,weight=1)
managerPage.rowconfigure(4,weight=1)
managerPage.columnconfigure(0,weight=1)

#Store employee page
storeemployeePage = Frame(window)

storeemployeePage.rowconfigure(0,weight=1)
storeemployeePage.rowconfigure(1,weight=1)
storeemployeePage.rowconfigure(2,weight=1)
storeemployeePage.rowconfigure(3,weight=1)
storeemployeePage.rowconfigure(4,weight=1)
storeemployeePage.columnconfigure(0,weight=1)

#Begin with the welcome page visible
welcomePage.place(relwidth=1,relheight=1)

window.mainloop() #An infinite loop, runs until we close the window
