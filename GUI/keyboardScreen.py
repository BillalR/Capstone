import tkinter as tk
from tkinter import ttk

from AppSetup.window_setup import *

class keyboardScreen:

    def __init__(self,master):

        self.master = master
        self.mainFrame = tk.Frame(self.master, bg=background_color)

        #center frame that fits between the header and footer
        self.keyboardFrame = tk.Frame(self.mainFrame, bg=background_color)
        for rows in range (0,20):
            self.keyboardFrame.rowconfigure(rows, weight = 1)
        for columns in range(0,150):
            self.keyboardFrame.columnconfigure(columns, weight = 1)
        #### define center frame widgets


        #pack the center frame
        self.keyboardFrame.pack(expand = 1, fill = 'both')



    def pack(self):
        self.mainFrame.pack(expand = 1, fill = 'both')

    def pack_forget(self):
        self.mainFrame.pack_forget()
