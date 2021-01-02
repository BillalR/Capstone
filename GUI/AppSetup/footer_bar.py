import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from .window_setup import *

class footer:

    def __init__(self, master):
        self.master = master
        self.footer_height = 40


        #configure frame
        self.canvas = tk.Canvas(self.master,
                                height = self.footer_height,
                                width = 800,
                                bg = "#81899f",
                                bd=0,
                                highlightcolor = '#81899f',
                                highlightbackground = "#81899f")

        for rows in range (0,1):
            self.canvas.rowconfigure(rows, weight = 1)
        for columns in range(0,30):
            self.canvas.columnconfigure(columns, weight = 1)

        ####configure buttons

        #home button
        '''
        self.homeButton = ttk.Button(self.canvas,
                                     text = 'HOME',
                                     style = 'footer.TButton')
        self.homeButton.grid(column = 0, row = 0, sticky='e')
        '''
        #settings button
        '''
        self.settingsButton = ttk.Button(self.canvas,
                                     text = 'SETTINGS',
                                     style = 'footer.TButton')
        self.settingsButton.grid(column = 1, row = 0, sticky='e')

        #back button
        self.backButton = ttk.Button(self.canvas,
                                     text = 'BACK',
                                     style = 'footer.TButton')
        self.backButton.grid(column = 2, row = 0, sticky='e')
        '''
        #logo image
        self.load = Image.open("/Users/billalrahimi/Desktop/Capstone/GUI/AppSetup/Graphics/GEN_C_LOGO.png")
        self.render = ImageTk.PhotoImage(self.load)

        self.logoButton = ttk.Button(self.canvas,
                                     image = self.render,
                                     style='flat.TButton')
                                     #bg="#81899f")
        #self.logoButton.config()
        self.logoButton.grid(column=0,row=0,columnspan=1,rowspan=1, sticky='w')


        self.canvas.pack(fill = 'x', ipady = 7, side=tk.BOTTOM)
