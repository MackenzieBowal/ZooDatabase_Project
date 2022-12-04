from tkinter import *
from tkinter.ttk import Notebook
import species
import enclosures
import exhibits
import donors

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
    enclosuresFrame = Frame(visitorNotebook, width=1000, height=700)
    exhibitsFrame = Frame(visitorNotebook, width=1000, height=700)
    speciesFrame = Frame(visitorNotebook, width=1000, height=700)
    donorFrame = Frame(visitorNotebook, width=1000, height=700)

    enclosuresFrame.pack(fill='both', expand=True)
    exhibitsFrame.pack(fill='both', expand=True)
    speciesFrame.pack(fill='both', expand=True)
    donorFrame.pack(fill='both', expand=True)

    visitorNotebook.add(enclosuresFrame, text='Enclosures')
    visitorNotebook.add(exhibitsFrame, text='Exhibits')
    visitorNotebook.add(speciesFrame, text='Species')
    visitorNotebook.add(donorFrame, text='Donors')

    enclosures.set_enclosures_frame(enclosuresFrame)
    exhibits.set_exhibits_frame(exhibitsFrame, False)
    species.setSpeciesFrame(speciesFrame)
    donors.set_donors_frame(donorFrame, True)
