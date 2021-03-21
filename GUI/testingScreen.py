import tkinter as tk
from tkinter import ttk
import os
from PIL import ImageTk, Image
from AppSetup.window_setup import *

class testingScreen:

    def __init__(self,master):

        self.master = master
        self.mainFrame = tk.Frame(self.master, bg=background_color)

        #center frame that fits between the header and footer
        self.testFrame = tk.Frame(self.mainFrame, bg=background_color)
        for rows in range (0,20):
            self.testFrame.rowconfigure(rows, weight = 1)
        for columns in range(0,50):
            self.testFrame.columnconfigure(columns, weight = 1)
        #### define center frame widgets

        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "AppSetup/Graphics/calibrationLoading1.png"
        abs_file_path = os.path.join(script_dir, rel_path)
        self.load = Image.open(abs_file_path)
        self.render = ImageTk.PhotoImage(self.load)
        self.neutralImage = ttk.Button(self.testFrame,
                                     image = self.render,
                                     style = 'image.TButton')
        self.neutralImage.grid(column=25,row=3,columnspan=1,rowspan=1,sticky='n')

        self.testingInstruction1 = ttk.Label(self.testFrame,
                                                 text="Welcome to the testing center.",
                                                 style = "overBackground.TLabel")
        self.testingInstruction1.grid(column=25,row=5,columnspan=1,rowspan=1,padx=30)

        self.testingInstruction12 = ttk.Label(self.testFrame,
                                                 text="Upon hitting start, you will be",
                                                 style = "overBackground.TLabel")
        self.testingInstruction12.grid(column=25,row=6,columnspan=1,rowspan=1,padx=30)

        self.testingInstruction13 = ttk.Label(self.testFrame,
                                                 text="able to give your brain commands a shot.",
                                                 style = "overBackground.TLabel")
        self.testingInstruction13.grid(column=25,row=7,columnspan=1,rowspan=1,padx=30)

        self.CNNButton = ttk.Button(self.testFrame,
                                                    text="Generate CNN",
                                                    style="unpressed.TButton")
        self.CNNButton.grid(column=25,row=9,columnspan=1,rowspan=1,padx=30)

        self.KNNButton = ttk.Button(self.testFrame,
                                                    text="Generate KNN",
                                                    style="unpressed.TButton")
        self.KNNButton.grid(column=25,row=10,columnspan=1,rowspan=1,padx=30)

        self.testingButton = ttk.Button(self.testFrame,
                                                    text="Start",
                                                    style="unpressed.TButton")
        self.testingButton.grid(column=25,row=11,columnspan=1,rowspan=1,padx=30)


        #pack the center frame
        self.testFrame.pack(expand = 1, fill = 'both')


    def pack(self):
        self.mainFrame.pack(expand = 1, fill = 'both')

    def pack_forget(self):
        self.mainFrame.pack_forget()
