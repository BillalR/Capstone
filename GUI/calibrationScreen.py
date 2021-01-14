import tkinter as tk
from tkinter import ttk

from AppSetup.window_setup import *

class calibrationScreen:

    def __init__(self,master):

        self.master = master
        self.mainFrame = tk.Frame(self.master, bg='white')

        #center frame that fits between the header and footer
        self.calibFrame = tk.Frame(self.mainFrame, bg="#2A363B")
        for rows in range (0,20):
            self.calibFrame.rowconfigure(rows, weight = 1)
        for columns in range(0,150):
            self.calibFrame.columnconfigure(columns, weight = 1)
        #### define center frame widgets

        #Serial Stream Button
        self.calibrateButton = ttk.Button(self.calibFrame,
                                     text = 'Start Serial Connection',
                                     style = 'gui.TButton')
        self.calibrateButton.grid(column = 50, row = 0)
        #self.calibrateButton.place(x=20,y=20)

        #pack the center frame
        self.calibFrame.pack(expand = 1, fill = 'both')



    def pack(self):
        self.mainFrame.pack(expand = 1, fill = 'both')

    def pack_forget(self):
        self.mainFrame.pack_forget()
