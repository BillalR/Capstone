import tkinter as tk
from tkinter import ttk
import os
from PIL import ImageTk, Image
from AppSetup.window_setup import *



class sideMenu:

    def __init__(self, master):
        self.master = master

        #Side frame
        self.canvas = tk.Canvas(self.master,
                                height = 1280-80-80-80,
                                width = 20,
                                bg = "#81899f",
                                bd=0,
                                highlightcolor = "#81899f",
                                highlightbackground = "#81899f")
        for rows in range (0,1000):
            self.canvas.rowconfigure(rows, weight = 1)
        for columns in range(0,3):
            self.canvas.columnconfigure(columns, weight = 1)

        self.homeButton = ttk.Button(self.canvas,
                                     text = 'Home',
                                     style = 'unpressed.TButton')
        self.homeButton.grid(column = 0, row = 0, sticky = 'ne',ipady=0)

        self.calibrateScreenButton = ttk.Button(self.canvas,
                                     text = 'Calibration',
                                     style = 'unpressed.TButton')
        self.calibrateScreenButton.grid(column = 0, row = 1, sticky = 'ne', ipady=0)

        self.keyboardButton = ttk.Button(self.canvas,
                                         text='Keyboard',
                                         style='unpressed.TButton')
        self.keyboardButton.grid(column=0, row=2, sticky='ne', ipady=0)


        self.testButton = ttk.Button(self.canvas,
                                     text='Testing',
                                     style='unpressed.TButton')
        self.testButton.grid(column=0, row=3, sticky='ne', ipady=0)

        self.quickButton = ttk.Button(self.canvas,
                                      text='Quick Menu',
                                      style='unpressed.TButton')
        self.quickButton.grid(column=0, row=4, sticky='ne', ipady=0)



        '''
        #Get yourself a better logo than this one
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "Graphics/GEN_C_LOGO.png"
        abs_file_path = os.path.join(script_dir, rel_path)
        self.load = Image.open(abs_file_path)
        self.render = ImageTk.PhotoImage(self.load)
        self.logoButton = ttk.Button(self.canvas,
                                     image = self.render,
                                     style='flat.TButton')
                                     #bg="#81899f")
        #self.logoButton.config()
        self.logoButton.grid(column=0, row=990, sticky='sw', padx=40)
        '''

        self.canvas.pack(fill='y', ipady = 0, side=tk.RIGHT)
