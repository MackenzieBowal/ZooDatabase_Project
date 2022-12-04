from tkinter import *
from tkinter.ttk import Notebook
import mysql.connector

import exhibits

# Create a connection to the database
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "zoodatabase"
)

mycursor = mydb.cursor()

def signout_clicked():
    entertainerPage.destroy()
    mainFrame.place(relwidth=1,relheight=1)

def handle_entertainer_page(window,eid,mFrame):
    global mainFrame
    mainFrame = mFrame

    global entertainerPage
    entertainerPage = Frame(window)

    entertainerPage.rowconfigure(0,weight=1)
    entertainerPage.rowconfigure(1,weight=1)
    entertainerPage.columnconfigure(0,weight=1)

    entertainerPage.place(relwidth=1,relheight=1)

    signoutButton = Button(entertainerPage, text="Sign Out", command=signout_clicked)
    signoutButton.grid(row=0,column=0,columnspan=2,sticky=N+W,padx=5)

    entertainerNotebook = Notebook(entertainerPage)
    entertainerNotebook.grid(row=1,column=0)

    #Create frames
    homeFrame = Frame(entertainerNotebook, width=1000, height=700)
    exhibitsFrame = Frame(entertainerNotebook, width=1000, height=700)

    homeFrame.pack(fill='both', expand=True)
    exhibitsFrame.pack(fill='both', expand=True)

    entertainerNotebook.add(homeFrame, text='Home')
    entertainerNotebook.add(exhibitsFrame, text='Exhibits')
    
    set_home_frame(homeFrame,eid)
    exhibits.set_exhibits_frame(exhibitsFrame, False)

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