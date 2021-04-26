import tkinter as tk
from tkinter import ttk

from AppSetup.window_setup import *
from AppSetup.base_app import *

buttons = [
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', 'BACK',
'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'CAPS',
'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '\\','/', '-', 'SHIFT',
'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '?', '!', '_', 'CANCEL',
'SPACE', 'ENTER']

class keyboardScreen:

    def __init__(self,master):

        self.master = master
        self.keyBoard = tk.TopLevel(self.master)
        scr_w = self.master.winfo_screenwidth()
        scr_h = self.master.winfo_screenheight()
        x = (scr_w/2) - (w/2)
        y = (scr_h) - (h)
        self.keyBoard.geometry('%dx%d+%d+%d' % (w, h, x, y))

        #Text entry setup
        self.entryText = tk.StringVar()
        self.entryText.set('')

        #Entry box
        self.Entry

        self.keybFrame = ttk.Frame(self.master, style = 'TFrame')
        self.keybFrame.pack(expand = 1, fill = 'both')

        for rows in range(0,6):
            self.keybFrame.rowconfigure(rows, weight = 1)
        for cols in range(0,12):
            self.keybFrame.columnconfigure(cols, weight = 1)

        self.initButtons()
        #center frame that fits between the header and footer
        self.keyboardFrame = tk.Frame(self.mainFrame, bg=background_color)
        for rows in range (0,20):
            self.keyboardFrame.rowconfigure(rows, weight = 1)
        for columns in range(0,150):
            self.keyboardFrame.columnconfigure(columns, weight = 1)
        #### define center frame widgets


        #pack the center frame
        self.keyboardFrame.pack(expand = 1, fill = 'both')



    def initButtons(self):
        varRow = 1
        varColumn = 0
        for button in buttons:
            command = lambda x=button: self.select(x)

            if button == "SPACE":
                ttk.Button(self.keyboardFrame,text= button,command=command, style = 'space.osk.TButton').grid(row=varRow,column=varColumn, columnspan=13)
                varColumn +=11
            elif button == "ENTER":
                ttk.Button(self.keyboardFrame,text= button,command=command, style = 'osk.TButton').grid(row=varRow,column=varColumn, columnspan=2)
                varColumn +=1
            else:
                ttk.Button(self.keyboardFrame,text= button,command=command, style = 'osk.TButton').grid(row=varRow,column=varColumn)
                varColumn +=1

            if varColumn > 12:
                varColumn = 0
                varRow+=1

    def select(self,value):
        global shiftActive
        global capsActive
        if value == "CANCEL":
            entryText.set('')
            finish()
        elif value == "BACK":
            entryText.set(entryText.get()[:-1])
        elif value == "CAPS":
            if capsActive:
                capsActive = False
            else:
                capsActive = True
        elif value == "SPACE":
            entryText.set(entryText.get()+' ')
        elif value == "SHIFT":
            shiftActive = True
        elif value == "ENTER":
            finish()
        elif shiftActive or capsActive:
            entryText.set(entryText.get()+value.upper())
            shiftActive = False
        else :
            entryText.set(entryText.get()+value)

    def pack(self):
        self.mainFrame.pack(expand = 1, fill = 'both')

    def pack_forget(self):
        self.mainFrame.pack_forget()
