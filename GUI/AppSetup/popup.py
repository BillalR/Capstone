#this is to generate a popup. plain and simple.
# By: T.J. Krawczynski
# created: March 4, 2019

import tkinter as tk
from tkinter import ttk


popup_window = None
PASSWORD='2233'

def popup(master, message, password=False, cancel=False, okayCommand=None, cancelCommand=None, okayLabel = 'Okay', cancelLabel = 'Cancel'):
    global popup_window
    print('popup: ' + message)
    if popup_window != None:
        closePopup()
    popup_window = tk.Toplevel(master)
    scr_w = master.winfo_screenwidth()
    scr_h = master.winfo_screenheight()
    pop_w = 600
    pop_h = 200
    popup_window.geometry('%dx%d+%d+%d' % (pop_w, pop_h, (scr_w/2)-(pop_w/2), (scr_h/2)-(pop_h/2)))
    popup_window.overrideredirect(True)

    popupFrame = ttk.Frame(popup_window, style = 'apexpop.TFrame')
    for rows in range (0,3):
        popupFrame.rowconfigure(rows, weight = 1)
    for cols in range (0,2):
        popupFrame.columnconfigure(cols, weight = 1)

    #text prompt and password entry
    popupLabel = ttk.Label(popupFrame, style='displaypop.TLabel', text=message)
    passwordVar = tk.StringVar()
    passwordEntry = ttk.Entry(popupFrame, style='apex.TEntry', textvariable=passwordVar)
    passwordEntry.bind("<ButtonPress>", lambda e: osk.kb(master, passwordVar, writeOnLostFocus=True))
    if password==True:
        popupLabel.grid(column=0, row=0, rowspan=1, columnspan=2, padx=20, pady=5)
        passwordEntry.grid(column=0, row=1, rowspan=1, columnspan=2, padx=20, pady=5)
    else:
        popupLabel.grid(column=0, row=0, rowspan=2, columnspan=2, padx=20, pady=20)

    #cancel button
    cancelButton = ttk.Button(popupFrame, text = cancelLabel, style = 'apex.TButton', command = lambda: cancelPressed(cancelCommand))

    #okay button
    OKButton = ttk.Button(popupFrame, text = okayLabel, style = 'apex.TButton')
    if password == True:
        OKButton.configure(command = lambda: okayPressed(okayCommand, passwordVar.get()))
    else:
        OKButton.configure(command = lambda: okayPressed(okayCommand))

    #grid the buttons
    if cancel==True:
        cancelButton.grid(column=0, row=2, pady=20, padx=20)
        OKButton.grid(column=1, row=2, pady=20, padx=20)
    else:
        OKButton.grid(column=0,columnspan=2, row=2, pady=20, padx=20)

    popupFrame.pack(expand = 1, fill = 'both')

def okayPressed(action=None, password=None):
    if password == None or password == PASSWORD:
        if action != None:
            action()
    closePopup()

def cancelPressed(action=None):
    if action != None:
        action()
    closePopup()

def closePopup():
    global popup_window
    popup_window.destroy()
    popup_window = None
