from tkinter import *
from tkinter.ttk import Notebook
import mysql.connector

import passes, exhibits, enclosures

# Create a connection to the database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "zoodatabase"
)

mycursor = mydb.cursor()

def signout_clicked():
    receptionistPage.destroy()
    mainFrame.place(relwidth=1,relheight=1)

def handle_receptionist_page(window,eid,mFrame):
    global mainFrame
    mainFrame = mFrame

    global receptionistPage
    receptionistPage = Frame(window)

    receptionistPage.rowconfigure(0,weight=1)
    receptionistPage.rowconfigure(1,weight=1)
    receptionistPage.columnconfigure(0,weight=1)

    receptionistPage.place(relwidth=1,relheight=1)

    signoutButton = Button(receptionistPage, text="Sign Out", command=signout_clicked)
    signoutButton.grid(row=0,column=0,columnspan=2,sticky=N+W,padx=5)

    receptionistNotebook = Notebook(receptionistPage)
    receptionistNotebook.grid(row=1,column=0)

    #Create frames
    homeFrame = Frame(receptionistNotebook, width=1000, height=700)
    passesFrame = Frame(receptionistNotebook, width=1000, height=700)
    exhibitsFrame = Frame(receptionistNotebook, width=1000, height=700)
    enclosuresFrame = Frame(receptionistNotebook, width=1000, height=700)

    homeFrame.pack(fill='both', expand=True)
    passesFrame.pack(fill='both', expand=True)
    exhibitsFrame.pack(fill='both', expand=True)
    enclosuresFrame.pack(fill='both', expand=True)

    receptionistNotebook.add(homeFrame, text='Home')
    receptionistNotebook.add(passesFrame, text='Passes')
    receptionistNotebook.add(exhibitsFrame, text='Exhibits')
    receptionistNotebook.add(enclosuresFrame, text='Enclosures')
    
    set_home_frame(homeFrame,eid)
    passes.set_passes_frame(passesFrame)
    exhibits.set_exhibits_frame(exhibitsFrame)
    enclosures.set_enclosures_frame(enclosuresFrame)

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