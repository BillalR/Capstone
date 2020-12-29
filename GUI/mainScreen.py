import tkinter as tk
from tkinter import ttk

from AppSetup.header_bar import *
from AppSetup.window_setup import *

#window edge padding
pad = 5

class mainScreen:

    def __init__(self,master):

        self.master = master
        self.mainFrame = tk.Frame(self.master, bg='white')


        #center frame that fits between the header and footer
        self.leftFrame = tk.Frame(self.mainFrame, bg='white')
        for rows in range (0,5):
            self.leftFrame.rowconfigure(rows, weight = 1)
        for columns in range(0,5):
            self.leftFrame.columnconfigure(columns, weight = 1)

        #### define center frame widgets

        #Serial Stream Button
        self.serialData = ttk.Button(self.leftFrame,
                                     text = 'Start Serial Connection',
                                     style = 'gui.TButton')
        self.serialData.grid(column = 0, row = 0)

        #Make LSL Connection
        self.connectLSL = ttk.Button(self.leftFrame,
                                     text = 'Look for LSL Connection',
                                     style = 'gui.TButton')
        self.connectLSL.grid(column = 0, row = 0)

        #pack the center frame
        self.leftFrame.pack(expand = 1, fill = 'both')



    def pack(self):
        self.mainFrame.pack(expand = 1, fill = 'both')

    def pack_forget(self):
        self.mainFrame.pack_forget()
