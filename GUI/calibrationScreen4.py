import tkinter as tk
from tkinter import ttk
import os
from PIL import ImageTk, Image
from AppSetup.window_setup import *

class calibrationScreen4:

    def __init__(self,master):

        self.master = master
        self.mainFrame = tk.Frame(self.master, bg=background_color)

        #center frame that fits between the header and footer
        self.calibFrame = tk.Frame(self.mainFrame, bg=background_color)
        for rows in range (0,20):
            self.calibFrame.rowconfigure(rows, weight = 1)
        for columns in range(0,50):
            self.calibFrame.columnconfigure(columns, weight = 1)
        #### define center frame widgets

        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "AppSetup/Graphics/calibrationLoading1.png"
        abs_file_path = os.path.join(script_dir, rel_path)
        self.load = Image.open(abs_file_path)
        self.render = ImageTk.PhotoImage(self.load)
        self.neutralImage = ttk.Button(self.calibFrame,
                                     image = self.render,
                                     style = 'image.TButton')
        self.neutralImage.grid(column=25,row=3,columnspan=1,rowspan=1,sticky='n')

        self.calibrationRedoLabel = ttk.Label(self.calibFrame,
                                                 text="Would you like to redo the neutral state calibration?",
                                                 style = "overBackground.TLabel")
        self.calibrationRedoLabel.grid(column=25,row=4,columnspan=1,rowspan=1,padx=30)

        self.calibrationRedoButton = ttk.Button(self.calibFrame,
                                                    text="Redo",
                                                    style="unpressed.TButton")
        self.calibrationRedoButton.grid(column=25,row=6,columnspan=1,rowspan=1,padx=30)

        self.calibrationContinueButton = ttk.Button(self.calibFrame,
                                                    text="Continue",
                                                    style="unpressed.TButton")
        self.calibrationContinueButton.grid(column=25,row=7,columnspan=1,rowspan=1,padx=30)

        '''
        self.calibrationInstructions2 = ttk.Label(self.calibFrame,
                                                 text="We will begin with a Neutral State.",
                                                 style = "overBackground.TLabel")
        self.calibrationInstructions2.grid(column=25,row=6,columnspan=1,rowspan=1,padx=30)

        self.calibrationInstructions3 = ttk.Label(self.calibFrame,
                                                 text="Press button below to continue.",
                                                 style = "overBackground.TLabel")
        self.calibrationInstructions3.grid(column=25,row=7,columnspan=1,rowspan=1,padx=30)
        '''

        #pack the center frame
        self.calibFrame.pack(expand = 1, fill = 'both')


    def pack(self):
        self.mainFrame.pack(expand = 1, fill = 'both')

    def pack_forget(self):
        self.mainFrame.pack_forget()
