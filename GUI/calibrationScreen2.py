import tkinter as tk
from tkinter import ttk
import os
from PIL import ImageTk, Image
from AppSetup.window_setup import *

class calibrationScreen2:

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

        self.blankSpace = ttk.Label(self.calibFrame,
                                                 text="Begin with a couple of deep breathes, to relax your mind. By ",
                                                 style = "overBackground.TLabel")
        self.blankSpace.grid(column=25,row=5,columnspan=1,rowspan=1,padx=30)

        self.calibrationInstructions2 = ttk.Label(self.calibFrame,
                                                 text="pressing the Start Button, we will take 30 seconds of your neutral",
                                                 style = "overBackground.TLabel")
        self.calibrationInstructions2.grid(column=25,row=6,columnspan=1,rowspan=1,padx=30)

        self.calibrationInstructions3 = ttk.Label(self.calibFrame,
                                                 text="state brain wave data. A redo will be offered. Once you press",
                                                 style = "overBackground.TLabel")
        self.calibrationInstructions3.grid(column=25,row=7,columnspan=1,rowspan=1,padx=30)

        self.calibrationInstructions4 = ttk.Label(self.calibFrame,
                                                 text="start, make sure to close your eyes and remain calm.",
                                                 style = "overBackground.TLabel")
        self.calibrationInstructions4.grid(column=25,row=8,columnspan=1,rowspan=1,padx=30)

        self.neutralStateReadButton = ttk.Button(self.calibFrame,
                                                    text="Start",
                                                    style="unpressed.TButton")
        self.neutralStateReadButton.grid(column=25,row=9,columnspan=1,rowspan=1,padx=30)


        #pack the center frame
        self.calibFrame.pack(expand = 1, fill = 'both')


    def pack(self):
        self.mainFrame.pack(expand = 1, fill = 'both')

    def pack_forget(self):
        self.mainFrame.pack_forget()
