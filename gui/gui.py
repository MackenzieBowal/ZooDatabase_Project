from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror

def employee():
    signinPage.place(relwidth=1,relheight=1)
    employeeidBox.focus()

def signin():
    eid = employeeidBox.get()
    pwd = passwordBox.get()
    etype = empTypeBox.get()
    if (eid,pwd,etype) in employees:
        employeePage(etype)
    else:
        showerror(title="Error",message="Invalid username/password combination, or incorrect employee type. Please try again.")

#Switch to the homepage for the selected employee type
def employeePage(etype):
    if etype == "Receptionist":
        receptionistPage.place(relwidth=1,relheight=1)
    elif etype == "Entertainer":
        entertainerPage.place(relwidth=1,relheight=1)
    elif etype == "Zookeeper":
        zookeeperPage.place(relwidth=1,relheight=1)
    elif etype == "Manager":
        managerPage.place(relwidth=1,relheight=1)
    elif etype == "Store Employee":
        storeemployeePage.place(relwidth=1,relheight=1)

#A list of valid (employeeID, password, employee type) combinations
employees = [("12345","password1","Receptionist"),("23456","password2","Entertainer"),
            ("34567","password3","Zookeeper"),("45678","password4","Manager"),("56789","password5","Store Employee")]

window = Tk() #Create the main window
window.title("Our Zoo Database System") #Set the title of the window
window.geometry("1024x768") #Set the size of the window

#Welcome page
welcomePage = Frame(window)

welcomeMessage = Label(welcomePage,text="Welcome to the Zoo!\nPlease log in to continue.")
employeeButton = Button(welcomePage,text="Employee",command=employee)
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

receptionistMessage = Label(receptionistPage,text="Welcome receptionist")
receptionistMessage.grid(row=0,column=0,sticky=N+S+W+E,padx=5,pady=10)

receptionistPage.rowconfigure(0,weight=1)
receptionistPage.columnconfigure(0,weight=1)

#Entertainer page
entertainerPage = Frame(window)

entertainerMessage = Label(entertainerPage,text="Welcome entertainer")
entertainerMessage.grid(row=0,column=0,sticky=N+S+W+E,padx=5,pady=10)

entertainerPage.rowconfigure(0,weight=1)
entertainerPage.columnconfigure(0,weight=1)

#Zookeeper page
zookeeperPage = Frame(window)

zookeeperMessage = Label(zookeeperPage,text="Welcome zookeeper")
zookeeperMessage.grid(row=0,column=0,sticky=N+S+W+E,padx=5,pady=10)

zookeeperPage.rowconfigure(0,weight=1)
zookeeperPage.columnconfigure(0,weight=1)

#Manager page
managerPage = Frame(window)

managerMessage = Label(managerPage,text="Welcome manager")
managerMessage.grid(row=0,column=0,sticky=N+S+W+E,padx=5,pady=10)

managerPage.rowconfigure(0,weight=1)
managerPage.columnconfigure(0,weight=1)

#Store employee page
storeemployeePage = Frame(window)

storeemployeeMessage = Label(storeemployeePage,text="Welcome store employee")
storeemployeeMessage.grid(row=0,column=0,sticky=N+S+W+E,padx=5,pady=10)

storeemployeePage.rowconfigure(0,weight=1)
storeemployeePage.columnconfigure(0,weight=1)

#Begin with the welcome page visible
welcomePage.place(relwidth=1,relheight=1)

window.mainloop() #An infinite loop, runs until we close the window
