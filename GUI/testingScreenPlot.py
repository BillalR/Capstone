import tkinter as tk
from tkinter import ttk
import os
from PIL import ImageTk, Image
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from AppSetup.window_setup import *

class testingScreenPlot:

    def __init__(self,master):

        self.master = master


        '''
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

        self.testingButton = ttk.Button(self.testFrame,
                                                    text="Start",
                                                    style="unpressed.TButton")
        self.testingButton.grid(column=25,row=9,columnspan=1,rowspan=1,padx=30)
        '''

        #pack the center frame
        #self.canvas.pack(expand = 1, fill = 'both')


    def pack(self):
        self.mainFrame.pack(expand = 1, fill = 'both')

    def matplotCanvas(self, x, y):
        f = Figure(figsize(len(x), len(y)), dpi = 100)
        a = f.add_subplot(111)
        a.plot(x, y)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side = BOTTOM, fill=BOTH, expand=True)






    def pack_forget(self):
        self.mainFrame.pack_forget()
