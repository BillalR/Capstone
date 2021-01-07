import tkinter as tk
from tkinter import ttk

from AppSetup.window_setup import *

class header:

    def __init__(self, master):
        self.master = master
        self.header_height = 80

        #main frame
        self.canvas = tk.Canvas(self.master,
                                height = self.header_height,
                                width = 800,
                                bg = "#81899f",
                                bd=0,
                                highlightcolor = light_grey,
                                highlightbackground = "#81899f")
        for rows in range (0,3):
            self.canvas.rowconfigure(rows, weight = 1)
        for columns in range(0,30):
            self.canvas.columnconfigure(columns, weight = 1)


        #title
        self.pageName = tk.StringVar()
        self.pageName.set("Home")

        self.title=tk.Label(self.canvas,
                        font = ('Helvetica', 16),
                        textvariable = self.pageName,
                        bg = "#81899f")


        self.title.grid(column=14,row=0,columnspan=1,rowspan=3)

        #Drop down menu for users
        self.UserOPTIONS = [
        "New User..."
        ]

        self.individualName = tk.StringVar()
        self.individualName.set("User") # default value

        self.dropDown = tk.OptionMenu(self.canvas, self.individualName, *self.UserOPTIONS)
        self.dropDown.grid(column = 29, row = 1)
        self.dropDown.config(width=11,bg = "#81899f")


        #Drop down menu for Connection types
        self.UserOPTIONSNetwork = [
        "LSL                    ",
        "UDP                    "
        ]

        self.CType = tk.StringVar()
        self.CType.set("Connection Type") # default value

        self.ConnectionTypes = tk.OptionMenu(self.canvas, self.CType, *self.UserOPTIONSNetwork)
        self.ConnectionTypes.grid(column = 0, row = 1)
        self.ConnectionTypes.config(width=15, bg="#81899f")

        #status indicator
        '''
        self.IndicatorButton = ttk.Button(self.canvas,
                                     style = 'gui.TButton',
                                     text="Status",
                                     width=9,
                                     )
        self.IndicatorButton.grid(column = 29, row = 1)
        '''
#
#        self.subText_id = self.canvas.create_text(500, 55, text = '', font = ('Verdana', 10), fill = '#232A34', anchor = 'w')


        self.canvas.pack(fill='x', ipady = 3, side=tk.TOP)
