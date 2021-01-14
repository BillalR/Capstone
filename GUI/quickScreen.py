import tkinter as tk
from tkinter import ttk

from AppSetup.window_setup import *

class quickScreen:

    def __init__(self,master):

        self.master = master
        self.mainFrame = tk.Frame(self.master, bg='white')

        #center frame that fits between the header and footer
        self.quickFrame = tk.Frame(self.mainFrame, bg="#2A363B")
        for rows in range (0,20):
            self.quickFrame.rowconfigure(rows, weight = 1)
        for columns in range(0,150):
            self.quickFrame.columnconfigure(columns, weight = 1)
        #### define center frame widgets


        #pack the center frame
        self.quickFrame.pack(expand = 1, fill = 'both')



    def pack(self):
        self.mainFrame.pack(expand = 1, fill = 'both')

    def pack_forget(self):
        self.mainFrame.pack_forget()
