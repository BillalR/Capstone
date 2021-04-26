import tkinter as tk
from tkinter import ttk

class numpad():

    def __init__(self, master, entry=None):
        self.master = master
        self.entry = entry

        self.frame = ttk.Frame(self.master)
        self.frame.pack(expand=1, fill='both')

        #Entry box
        self.entryText = tk.StringVar()
        self.entry = ttk.Entry(self.frame, textvariable = self.entryText)
        self.entry.grid(row = 0, column = 0, columnspan = 15, sticky = 'n')


        #button generation
        self.buttons = [
        '7', '8', '9',
        '4', '5', '6',
        '1', '2', '3',
        '0', 'ENTER', 'CANCEL']

        for rows in range(0,5):
            self.frame.rowconfigure(rows, weight = 1)
        for cols in range(0,3):
            self.frame.columnconfigure(cols, weight = 1)

        row = 1
        col = 0
        for button in self.buttons:
            ttk.Button(self.frame, text = button).grid(row = row, column = col, padx = 1, pady = 1)

            col += 1

            if(col > 2):
                col = 0
                row +=1

    def pack(self):
        self.frame.pack(expand = 1, fill = 'both')
