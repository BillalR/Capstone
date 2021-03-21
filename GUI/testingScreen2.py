import tkinter as tk
from tkinter import ttk
import os
from PIL import ImageTk, Image
from AppSetup.window_setup import *

class testingScreen2:

    def __init__(self,master):

        self.master = master
        self.mainFrame = tk.Frame(self.master, bg=background_color)

        self.counter_1 = tk.IntVar()
        self.counter_1.set(10)

        #center frame that fits between the header and footer
        self.calibFrame = tk.Frame(self.mainFrame, bg=background_color)
        for rows in range (0,20):
            self.calibFrame.rowconfigure(rows, weight = 1)
        for columns in range(0,50):
            self.calibFrame.columnconfigure(columns, weight = 1)
        #### define center frame widgets

        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "AppSetup/Graphics/onLight.png"
        abs_file_path = os.path.join(script_dir, rel_path)
        self.load = Image.open(abs_file_path)
        self.render = ImageTk.PhotoImage(self.load)
        self.neutralImage = ttk.Button(self.calibFrame,
                                     image = self.render,
                                     style = 'image.TButton')
        self.neutralImage.grid(column=25,row=3,columnspan=1,rowspan=1,sticky='n')

        self.blankSpace = ttk.Label(self.calibFrame,
                                                 text="Light On",
                                                 style = "overBackground.TLabel")
        self.blankSpace.grid(column=25,row=5,columnspan=1,rowspan=1,padx=30)




        #pack the center frame
        self.calibFrame.pack(expand = 1, fill = 'both')


    def pack(self):
        self.mainFrame.pack(expand = 1, fill = 'both')

    def pack_forget(self):
        self.mainFrame.pack_forget()
