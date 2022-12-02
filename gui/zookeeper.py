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
    zookeeperPage.destroy()
    mainFrame.place(relwidth=1,relheight=1)

def handle_zookeeper_page(window,eid,mFrame):
    global mainFrame
    mainFrame = mFrame

    global zookeeperPage
    zookeeperPage = Frame(window)

    zookeeperPage.rowconfigure(0,weight=1)
    zookeeperPage.rowconfigure(1,weight=1)
    zookeeperPage.columnconfigure(0,weight=1)

    zookeeperPage.place(relwidth=1,relheight=1)

    signoutButton = Button(zookeeperPage, text="Sign Out", command=signout_clicked)
    signoutButton.grid(row=0,column=0,columnspan=2,sticky=N+W,padx=5)

    zookeeperNotebook = Notebook(zookeeperPage)
    zookeeperNotebook.grid(row=1,column=0)

    #Create frames
    homeFrame = Frame(zookeeperNotebook, width=1000, height=700)
    speciesFrame = Frame(zookeeperNotebook, width=1000, height=700)
    animalsFrame = Frame(zookeeperNotebook, width=1000, height=700)
    enclosuresFrame = Frame(zookeeperNotebook, width=1000, height=700)
    complexesFrame = Frame(zookeeperNotebook, width=1000, height=700)

    homeFrame.pack(fill='both', expand=True)
    speciesFrame.pack(fill='both', expand=True)
    animalsFrame.pack(fill='both', expand=True)
    enclosuresFrame.pack(fill='both', expand=True)
    complexesFrame.pack(fill='both', expand=True)

    zookeeperNotebook.add(homeFrame, text='Home')
    zookeeperNotebook.add(speciesFrame, text='Species')
    zookeeperNotebook.add(animalsFrame, text='Animals')
    zookeeperNotebook.add(enclosuresFrame, text='Enclosures')
    zookeeperNotebook.add(complexesFrame, text='Indoor Complexes')
    
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