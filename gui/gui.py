from tkinter import *
from visitor import handleVisitorPage
from signin import handle_signin_page

def visitorClick():
    handleVisitorPage(window, welcomePage)

def signin_click():
    handle_signin_page(window, welcomePage)

def mainMenu():
    welcomePage.place(relwidth=1,relheight=1)

def initiate():
    global window
    window = Tk()
    window.title("Our Zoo Database System") # Set the title of the window
    window.geometry("1024x768") # Set the size of the window

    # make welcome page
    global welcomePage
    welcomePage = Frame(window)

    welcomeMessage = Label(welcomePage,text="Welcome to the Zoo!\nPlease log in to continue.")
    employeeButton = Button(welcomePage,text="Employee",command=signin_click)
    visitorButton = Button(welcomePage,text="Visitor", command=visitorClick)

    welcomeMessage.grid(row=0,column=0,columnspan=2,sticky=N+S+W+E,padx=5)
    employeeButton.grid(row=1,column=0,sticky=N+S+W+E,padx=10,pady=5)
    visitorButton.grid(row=1,column=1,sticky=N+S+W+E,padx=10,pady=5)

    #Configure the grid elements to expand to fill extra space
    welcomePage.rowconfigure(0,weight=1)
    welcomePage.rowconfigure(1,weight=1)
    welcomePage.columnconfigure(0,weight=1)
    welcomePage.columnconfigure(1,weight=1)

    welcomePage.place(relwidth=1,relheight=1)

    window.mainloop() #An infinite loop, runs until we close the window

initiate()