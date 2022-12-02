from tkinter import *
from tkinter.ttk import Notebook
import mysql.connector

# Create a connection to the database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "zoodatabase"
)

mycursor = mydb.cursor()

def signout_clicked():
    managerPage.destroy()
    mainFrame.place(relwidth=1,relheight=1)

def handle_manager_page(window,eid,mFrame):
    global mainFrame
    mainFrame = mFrame

    global managerPage
    managerPage = Frame(window)

    managerPage.rowconfigure(0,weight=1)
    managerPage.rowconfigure(1,weight=1)
    managerPage.columnconfigure(0,weight=1)

    managerPage.place(relwidth=1,relheight=1)

    signoutButton = Button(managerPage, text="Sign Out", command=signout_clicked)
    signoutButton.grid(row=0,column=0,columnspan=2,sticky=N+W,padx=5)

    managerNotebook = Notebook(managerPage)
    managerNotebook.grid(row=1,column=0)

    #Create frames
    homeFrame = Frame(managerNotebook, width=1000, height=700)
    employeesFrame = Frame(managerNotebook, width=1000, height=700)
    exhibitsFrame = Frame(managerNotebook, width=1000, height=700)
    enclosuresFrame = Frame(managerNotebook, width=1000, height=700)
    complexesFrame = Frame(managerNotebook, width=1000, height=700)
    storesFrame = Frame(managerNotebook, width=1000, height=700)
    fundraisersFrame = Frame(managerNotebook, width=1000, height=700)
    donorsFrame = Frame(managerNotebook, width=1000, height=700)

    homeFrame.pack(fill='both', expand=True)
    employeesFrame.pack(fill='both', expand=True)
    exhibitsFrame.pack(fill='both', expand=True)
    enclosuresFrame.pack(fill='both', expand=True)
    complexesFrame.pack(fill='both', expand=True)
    storesFrame.pack(fill='both', expand=True)
    fundraisersFrame.pack(fill='both', expand=True)
    donorsFrame.pack(fill='both', expand=True)

    managerNotebook.add(homeFrame, text='Home')
    managerNotebook.add(employeesFrame, text='Employees')
    managerNotebook.add(exhibitsFrame, text='Exhibits')
    managerNotebook.add(enclosuresFrame, text='Enclosures')
    managerNotebook.add(complexesFrame, text='Indoor Complexes')
    managerNotebook.add(storesFrame, text='Stores')
    managerNotebook.add(fundraisersFrame, text='Fundraisers')
    managerNotebook.add(donorsFrame, text='Donors')
    
    set_home_frame(homeFrame,eid)

def set_home_frame(hFrame,eid):
    global homePage
    homePage = hFrame

    homePage.rowconfigure(0,weight=1)
    homePage.rowconfigure(1,weight=1)
    homePage.rowconfigure(2,weight=1)
    homePage.rowconfigure(3,weight=1)
    homePage.rowconfigure(4,weight=1)

    mycursor.execute("SELECT Name FROM Employee WHERE EmployeeID = %s"%eid)
    result = mycursor.fetchall()
    nameMessage = Label(homePage,text="Welcome %s"%result[0])
    nameMessage.grid(row=0,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Email FROM Employee WHERE EmployeeID = %s"%eid)
    result = mycursor.fetchall()
    emailMessage = Label(homePage,text="Email: %s"%result[0])
    emailMessage.grid(row=1,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Phone_number FROM Employee WHERE EmployeeID = %s"%eid)
    result = mycursor.fetchall()
    phoneMessage = Label(homePage,text="Phone: %s"%result[0])
    phoneMessage.grid(row=2,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Address FROM Employee WHERE EmployeeID = %s"%eid)
    result = mycursor.fetchall()
    addressMessage = Label(homePage,text="Address: %s"%result[0])
    addressMessage.grid(row=3,column=0,sticky=N+S+W+E,padx=5,pady=10)

    mycursor.execute("SELECT Start_date FROM Employee WHERE EmployeeID = %s"%eid)
    result = mycursor.fetchall()
    startdateMessage = Label(homePage,text="You've been working here since %s"%result[0])
    startdateMessage.grid(row=4,column=0,sticky=N+S+W+E,padx=5,pady=10)