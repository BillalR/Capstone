import tkinter as tk
import os
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
                                bg = background_color,
                                bd=0,
                                highlightcolor = '#2A363B',
                                highlightbackground = background_color)

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
        self.homeButton.grid(column = 28, row = 0, sticky='e')
        '''


        #back button
        '''
        self.backButton = ttk.Button(self.canvas,
                                     text = 'BACK',
                                     style = 'footer.TButton')
        self.backButton.grid(column = 28, row = 0, sticky='e')
        '''
        #logo image

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
        self.logoButton.grid(column=0,row=0,columnspan=1,rowspan=1, sticky='w')

        '''
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "Graphics/floatingCircle.gif"
        self.frameCnt = 30
        abs_file_path = os.path.join(script_dir, rel_path)
        self.load = Image.open(abs_file_path)
        self.render = [ImageTk.PhotoImage(self.load,format = 'gif -index %i' %(i)) for i in range(self.frameCnt)]
        self.logoButton = ttk.Button(self.canvas,
                                     image = self.render[0],
                                     style='flat.TButton')
                                     #bg="#81899f")
        #self.logoButton.config()
        self.logoButton.grid(column=0,row=0,columnspan=1,rowspan=1, sticky='w')
        '''
        self.canvas.pack(fill = 'x', ipady = 7, side=tk.BOTTOM)

    def updateGif(self, ind):
        frame = self.render[ind]
        ind += 1
        if ind == self.frameCnt:
            ind = 0
        self.logoButton.configure(image = frame)
        self.master.after(5, self.updateGif, ind)
