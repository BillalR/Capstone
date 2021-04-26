import tkinter as tk
from tkinter import ttk
import os
from PIL import ImageTk, Image
from AppSetup.window_setup import *

class tesingScreen2:

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
                                                 text="You have now completed the calibration process. Your ",
                                                 style = "overBackground.TLabel")
        self.blankSpace.grid(column=25,row=5,columnspan=1,rowspan=1,padx=30)

        self.calibrationInstructions2 = ttk.Label(self.calibFrame,
                                                 text="Machine Learning Model has been generated. Head ",
                                                 style = "overBackground.TLabel")
        self.calibrationInstructions2.grid(column=25,row=6,columnspan=1,rowspan=1,padx=30)

        self.calibrationInstructions2 = ttk.Label(self.calibFrame,
                                                 text="over to the test section to utilize your brain powers.",
                                                 style = "overBackground.TLabel")
        self.calibrationInstructions2.grid(column=25,row=7,columnspan=1,rowspan=1,padx=30)


        #pack the center frame
        self.calibFrame.pack(expand = 1, fill = 'both')


    def pack(self):
        self.mainFrame.pack(expand = 1, fill = 'both')

    def pack_forget(self):
        self.mainFrame.pack_forget()
