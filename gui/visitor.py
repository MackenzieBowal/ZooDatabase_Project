from tkinter import *
from tkinter.ttk import Notebook
import species

def backClicked():
    visitorPage.destroy()
    backFrame.place(relwidth=1,relheight=1)

def handleVisitorPage(window, bFrame):
    global backFrame
    backFrame = bFrame

    global visitorPage
    visitorPage = Frame(window)
    visitorPage.place(relwidth=1, relheight = 1)

    backButton = Button(visitorPage, text="Back", command=backClicked)
    visitorNotebook = Notebook(visitorPage)
    visitorNotebook.pack(expand=True)
    backButton.grid(row=0,column=0,columnspan=2,sticky=N+W,padx=5)
    visitorNotebook.grid(row=1,column=0)

    visitorPage.rowconfigure(0,weight=1)
    visitorPage.rowconfigure(1,weight=1)
    visitorPage.columnconfigure(0,weight=1)
    visitorPage.columnconfigure(1,weight=1)

    # create frames
    frame1 = Frame(visitorNotebook, width=1000, height=700)
    frame2 = Frame(visitorNotebook, width=1000, height=700)
    speciesFrame = Frame(visitorNotebook, width=1000, height=700)

    frame1.pack(fill='both', expand=True)
    frame2.pack(fill='both', expand=True)
    speciesFrame.pack(fill='both', expand=True)

    visitorNotebook.add(frame1, text='Exhibits')
    visitorNotebook.add(frame2, text='Enclosures')
    visitorNotebook.add(speciesFrame, text='Species')

    species.setSpeciesFrame(speciesFrame)
    

