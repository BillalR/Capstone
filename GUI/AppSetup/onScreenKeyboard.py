# https://github.com/ajinkyapadwad/Tkinter-HosoKeys

import tkinter as tk
from tkinter import ttk

w = 800
h = 250

buttons = [
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', 'BACK',
'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'CAPS',
'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '\\','/', '-', 'SHIFT',
'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '?', '!', '_', 'CANCEL',
'SPACE', 'ENTER']

shiftActive = False
capsActive = False

root = None
frame = None
entryText = None
entryFinal = None
wolf = False

def kb(master, entry, writeOnLostFocus=False):
    global root
    global frame
    if root is not None:
        return
    root = tk.Toplevel(master)

    scr_w = master.winfo_screenwidth()
    scr_h = master.winfo_screenheight()
    x = (scr_w/2) - (w/2)
    y = (scr_h) - (h)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #remove borders
    root.overrideredirect(False)

    global entryFinal
    entryFinal = entry

    global wolf
    wolf = writeOnLostFocus

    #Frame
    frame = ttk.Frame(root, style = 'osk.TFrame')
    frame.pack(expand = 1, fill = 'both')

    for rows in range(0,6):
        frame.rowconfigure(rows, weight = 1)
    for cols in range(0,12):
        frame.columnconfigure(cols, weight = 1)

    frame.bind("<Leave>", lambda e: lostFocus())

    #Entry box
    global entryText
    entryText = tk.StringVar()
    entryText.set(entryFinal.get())
    entry = ttk.Entry(frame, style='apex.TEntry', textvariable = entryText)
    entry.grid(row = 0, column = 0, columnspan = 13)#, sticky = 'n')

    initButtons()

def lostFocus():
    global wolf
    if wolf == True:
        select('ENTER')
    else:
        select('CANCEL')

def select(value):
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

def initButtons():
    varRow = 1
    varColumn = 0
    for button in buttons:
        command = lambda x=button: select(x)

        if button == "SPACE":
            ttk.Button(frame,text= button,command=command, style = 'space.osk.TButton').grid(row=varRow,column=varColumn, columnspan=13)
            varColumn +=11
        elif button == "ENTER":
            ttk.Button(frame,text= button,command=command, style = 'osk.TButton').grid(row=varRow,column=varColumn, columnspan=2)
            varColumn +=1
        else:
            ttk.Button(frame,text= button,command=command, style = 'osk.TButton').grid(row=varRow,column=varColumn)
            varColumn +=1

        if varColumn > 12:
            varColumn = 0
            varRow+=1

def finish():
    #return the string
    var = entryText.get()
    if var != '':
        global entryFinal
        entryFinal.set(var)
    global root
    root.destroy()
    root = None

#Launcher
#######################################
def main():
    print(kb())


#stops code from executing unless it is the main,
#aka avoids executing code if just importing a class
if __name__ == '__main__':
    main()
