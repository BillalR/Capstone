import tkinter as tk
from tkinter import ttk

from AppSetup.window_setup import *
from AppSetup.base_app import *



class keyboardScreen:

    def __init__(self,master):

        self.buttons = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '<--',
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'ENTER',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '',
            'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'CLEAR',
            'SPACE',
        ]

        self.curBut = [-1,-1]
        self.buttonL = [[]]
        self.read = False

        self.master = master
        self.keybFrame = ttk.Frame(self.master, style = 'osk.TFrame')

        for rows in range(0,6):
            self.keybFrame.rowconfigure(rows, weight = 1)
        for cols in range(0,11):
            self.keybFrame.columnconfigure(cols, weight = 1)

        #Text entry setup
        self.entryText = tk.StringVar()
        self.entryText.set('')

        #Entry box
        self.entryFrame = ttk.Entry(self.keybFrame, textvariable=self.entryText)
        self.entryFrame.grid(row = 0, column = 0, columnspan = 13)


        self.initbuttons()

    def leftKey(self):
        if self.curBut == [-1,-1]:
            self.curBut[:] = [0,0]
            self.buttonL[0][0].state(["pressed"])
        elif self.curBut[0] == 4:
            self.buttonL[self.curBut[0]][self.curBut[1]].state(["!pressed"])
            self.curBut[:] = [0,10]
            self.buttonL[0][10].state(["pressed"])
        else:
            self.buttonL[self.curBut[0]][self.curBut[1]].state(["!pressed"])
            self.curBut[:] = [self.curBut[0], (self.curBut[1]-1)%11]
            self.buttonL[self.curBut[0]][self.curBut[1]%11].state(["pressed"])

    def rightKey(self):
        if self.curBut == [-1,-1]:
            self.curBut[:] = [0,0]
            self.buttonL[0][0].state(["pressed"])
        elif self.curBut[0] == 4:
            self.buttonL[self.curBut[0]][self.curBut[1]].state(["!pressed"])
            self.curBut[:] = [0,0]
            self.buttonL[0][0].state(["pressed"])
        else:
            self.buttonL[self.curBut[0]][self.curBut[1]].state(["!pressed"])
            self.curBut[:] = [self.curBut[0], (self.curBut[1]+1)%11]
            self.buttonL[self.curBut[0]][self.curBut[1]%11].state(["pressed"])

    def upKey(self):
        if self.curBut == [-1,-1]:
            self.curBut[:] = [0,0]
            self.buttonL[0][0].state(["pressed"])
        elif self.curBut[0] == 0:
            self.buttonL[self.curBut[0]][self.curBut[1]].state(["!pressed"])
            self.curBut[:] = [(self.curBut[0]-1)%5, 0]
            self.buttonL[self.curBut[0]][self.curBut[1]%11].state(["pressed"])
        else:
            self.buttonL[self.curBut[0]][self.curBut[1]].state(["!pressed"])
            self.curBut[:] = [(self.curBut[0]-1)%5, self.curBut[1]]
            self.buttonL[self.curBut[0]][self.curBut[1]%11].state(["pressed"])

    def downKey(self):
        if self.curBut == [-1,-1]:
            self.curBut[:] = [0,0]
            self.buttonL[0][0].state(["pressed"])
        elif self.curBut[0] == 3:
            self.buttonL[self.curBut[0]][self.curBut[1]].state(["!pressed"])
            self.curBut[:] = [(self.curBut[0]+1)%5, 0]
            self.buttonL[self.curBut[0]][self.curBut[1]%11].state(["pressed"])
        else:
            self.buttonL[self.curBut[0]][self.curBut[1]].state(["!pressed"])
            self.curBut[:] = [(self.curBut[0]+1)%5, self.curBut[1]]
            self.buttonL[self.curBut[0]][self.curBut[1]%11].state(["pressed"])

    def brainSelect(self):
        if self.curBut == [-1,-1]:
            self.curBut[:] = [0,0]
            self.buttonL[0][0].state(["pressed"])
        else:
            self.buttonL[self.curBut[0]][self.curBut[1]].invoke()

    def select(self,value, x, y):
        if self.curBut != [-1,-1]:
            self.buttonL[self.curBut[0]][self.curBut[1]].state(["!pressed"])
        self.curBut[:] = [x,y]
        self.buttonL[x][y].state(["pressed"])
        if value == "CANCEL":
            self.entryText.set('')
            self.pack_forget()
        elif value == "<--":
            self.entryText.set(self.entryText.get()[:-1])
        elif value == "SPACE":
            self.entryText.set(self.entryText.get()+' ')
        elif value == "ENTER" or value == "CLEAR":
            self.entryText.set('')
        else:
            self.entryText.set(self.entryText.get()+value)

    def initbuttons(self):
        varRow = 1
        varColumn = 0
        for button in self.buttons:
            command=lambda x=button, i=varRow-1, j=varColumn: self.select(x, i, j)

            if button == "SPACE":
                tempButton = ttk.Button(self.keybFrame,text= button,command=command, style = "unpressedSmall.TButton")
                self.buttonL[varRow-1].append(tempButton)
                tempButton.grid(row=varRow,column=varColumn, columnspan=13)
                varColumn +=9
            else:
                tempButton = ttk.Button(self.keybFrame,text= button,command=command, style = "unpressedSmall.TButton")
                self.buttonL[varRow-1].append(tempButton)
                tempButton.grid(row=varRow,column=varColumn, columnspan = 1, rowspan = 1)
                varColumn +=1

            if varColumn > 10:
                varColumn = 0
                varRow+=1
                self.buttonL.append([])

        '''
        #Typical Key Bindings
        self.keybFrame.bind('<Left>', self.leftKey)
        self.keybFrame.bind('<Right>', self.rightKey)
        self.keybFrame.bind('<Up>', self.upKey)
        self.keybFrame.bind('<Down>', self.downKey)
        self.keybFrame.bind('<Return>', self.brainSelect)
        '''
        self.keybFrame.focus_set()



    def pack(self):
        self.keybFrame.pack(expand = 1, fill = 'both')
        self.read = True

    def pack_forget(self):
        self.keybFrame.pack_forget()
        self.read = False
