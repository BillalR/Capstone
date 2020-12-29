import tkinter as tk
from tkinter import ttk

from .window_setup import *

class footer:

    def __init__(self, master, sliderVar, showSlider=False, showFreedrive=True):
        self.master = master
        self.sliderVar = sliderVar
        self.showSlider = showSlider
        self.showFreedrive = showFreedrive
        self.footer_height = 80
        

        #configure frame
        self.canvas = tk.Canvas(self.master,
                                height = self.footer_height,
                                width = 800,
                                bg = "white",
                                bd=0,
                                highlightcolor = light_grey,
                                highlightbackground = light_grey)
        for rows in range (0,1):
            self.canvas.rowconfigure(rows, weight = 1)
        for columns in range(0,30):
            self.canvas.columnconfigure(columns, weight = 1)

        ####configure buttons

        #home button
        self.homeButton = ttk.Button(self.canvas,
                                     text = 'HOME',
                                     style = 'footer.TButton')
        self.homeButton.grid(column = 0, row = 0, sticky='e')

        #settings button
        self.settingsButton = ttk.Button(self.canvas,
                                     text = 'SETTINGS',
                                     style = 'footer.TButton')
        self.settingsButton.grid(column = 1, row = 0, sticky='e')

        #back button
        self.backButton = ttk.Button(self.canvas,
                                     text = 'BACK',
                                     style = 'footer.TButton')
        self.backButton.grid(column = 2, row = 0, sticky='e')

        #speed slider
        self.sliderFrame = ttk.Frame(self.canvas,
                                     style = 'apex.TFrame')
        for rows in range (0,2):
            self.sliderFrame.rowconfigure(rows, weight = 1)
        for columns in range(0,2):
            self.sliderFrame.columnconfigure(columns, weight = 1)
        self.speedLabel = ttk.Label(self.sliderFrame, style = 'display.TLabel', text="Speed:")
        self.speedLabel.grid(column = 0, row = 0, sticky='e')
        self.speedDisplay = ttk.Label(self.sliderFrame, style = 'display.TLabel', textvariable = self.sliderVar)
        self.speedDisplay.grid(column = 1, row = 0, sticky='w')
        self.speedScale = ttk.Scale(self.sliderFrame,
                                    from_ = 0,
                                    to = 100,
                                    value=100,
                                    style = 'speed.Horizontal.TScale',
                                    length=200,
                                    command = self.roundSpeed)
        self.speedScale.grid(column=0, row=1, columnspan=2)
        if self.showSlider:
            self.slider_pack()

        #freedrive button
        self.freedriveButton = ttk.Button(self.canvas,
                                     text = 'FREEDRIVE',
                                     style = 'footer.TButton')
        if (self.showFreedrive==True):
            self.freedrive_pack()
        
        self.canvas.pack(fill = 'x', ipady = 7)

    def roundSpeed(self, x):
        self.sliderVar.set(int(float(x)))

    def slider_pack(self):
        self.sliderFrame.grid(column=3, row=0, columnspan=3)
    def slider_pack_forget(self):
        self.sliderFrame.grid_forget()

    def freedrive_pack(self):
        self.freedriveButton.grid(column = 29, row = 0, sticky='w')
    def freedrive_pack_forget(self):
        self.freedriveButton.grid_forget()
        
