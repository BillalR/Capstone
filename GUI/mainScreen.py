import tkinter as tk
from tkinter import ttk

from AppSetup.window_setup import *

#window edge padding
pad = 5

class mainScreen:

    def __init__(self,master):

        self.master = master
        self.mainFrame = tk.Frame(self.master, bg=background_color)

        #center frame that fits between the header and footer
        self.screenFrame = tk.Frame(self.mainFrame, bg=background_color)

        for rows in range (0,10):
            self.screenFrame.rowconfigure(rows, weight = 1)
        for columns in range(0,10):
            self.screenFrame.columnconfigure(columns, weight = 1)
        #### define center frame widgets

        #Serial Stream Button
        '''
        self.calibrateButton = ttk.Button(self.screenFrame,
                                     text = 'Start Serial Connection',
                                     style = 'gui.TButton')
        self.calibrateButton.grid(column = 0, row = 0, sticky = 'w')
        #self.calibrateButton.place(x=20,y=20)
        '''

        '''
        #Make LSL Connection
        self.connectLSL = ttk.Button(self.screenFrame,
                                     text = 'Look for LSL Connection',
                                     style = 'gui.TButton')
        self.connectLSL.grid(column = 0, row = 0)
        '''
        #pack the center frame
        self.screenFrame.pack(expand = 1, fill = 'both')



    def pack(self):
        self.mainFrame.pack(expand = 1, fill = 'both')

    def pack_forget(self):
        self.mainFrame.pack_forget()
