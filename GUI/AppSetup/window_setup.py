#this script sets up the gui ttk styles for all GUI elements

import tkinter as tk
from tkinter import ttk

#from .header_bar import *

#orange
orange = '#F47920'

#green
green = '#55A098'
br_green = '#3CDB4C'
#gui_green = '#0ddb36'

#yellow
yellow  = '#E7EC59'

#blue
blue = '#6620f4'

#nice blue
#blue = '#14B9D6'
nice_blue = '#00bfb3'

#grey
gui_grey = '#232A34'
grey = '#E4E4E4'
black = "#000000"

#lighter grey for scroll bars
light_grey = '#D3D7DA'

#lightest grey for backgrounds
lightest_grey = '#EFF0F2'

#red
red = '#A05558'


button_width = 20
button_height = 25
button_padding = 15
button_font = ('Helvetica Bold', 10)
text_font = ('Helvetica', 11)
app_font = ('Helvetica', 11)

#screen dimensions
w = 1280
h = 800

header_height = 80
footer_height = 80

def init_default_window(master, style):

    global button_width
    global button_height
    global button_padding
    global button_font
    global text_font
    global app_font
    button_width = 20
    button_height = 10
    button_padding = 15
    button_font = ('Helvetica Bold', 10)
    text_font = ('Helvetica', 11)
    app_font = ('Helvetica', 11)

    #Screen dimensioning
    scr_w = master.winfo_screenwidth()
    scr_h = master.winfo_screenheight()
    x = (scr_w/2) - (w/2)
    y = (scr_h/2) - (h/2)
    print('screen resolution:',w,h)
    master.geometry('%dx%d+%d+%d' % (w, h, x, y))

    style.theme_use('clam')

    #coloured button styles
    style.configure('gui.TButton',
                         foreground='black',
                         background = 'white',
                         width = button_width,
                         height = button_height,
                         relief = 'ridged',
                         padding = button_padding,
                         font = button_font,
                         wrap=tk.WORD)
    style.map('gui.TButton',background = [('pressed', black),('disabled',grey)])

    style.configure('popup.TButton',
                         foreground='black',
                         background = nice_blue,
                         width = button_width/4,
                         height = button_height/2,
                         relief = 'flat',
                         padding = button_padding,
                         font=('Helvetica Bold', 12),
                         wrap=tk.WORD)
    style.map('popup.TButton',background = [('pressed', nice_blue),('disabled',grey)])


    #footer button
    style.configure('footer.TButton', foreground='white', background = blue, width = 10, height = footer_height, relief = 'flat', padding = button_padding, font = button_font, wrap=tk.WORD)
    style.map('footer.TButton',background = [('active', blue)])

    #big button
    style.configure('big.TButton', foreground='white', background = '#14B9D6', width = 5, height = 25, relief = 'flat', padding = 10, font = ('Helvetica Bold', 30),wrap=tk.WORD)
    style.map('big.TButton', background = [('active', blue)])

    #small buttons
    style.configure('short.TButton', padding=button_padding*0.5)#flat and wide
    style.configure('small.TButton', padding=button_padding*0.5, width=10)#flat and short
    style.configure('tight.TButton', padding=button_padding*0.5, width=0)#flat and tight

    #generic frame style
    style.configure('TFrame', background='#81899f', bd=0)


    style.configure('TLabel', background='#81899f', font=('Helvetica Bold', 20), wrap=tk.WORD)
    style.configure('p.TLabel', background='#81899f', font=('Helvetica Bold', 16), wrap=tk.WORD)

    style.configure('E.TLabel', background='#81899f',foreground = '#CC0000', font=('Helvetica Bold', 16), wrap=tk.WORD)

    style.configure('pageLabel', background = 'red')

    #All of this below might need to be removed, it might tamper with other button styles
    style.configure("TMenubutton", background="#81899f")
    style.configure('flat.TButton',borderwidth=0,background="#81899f",bd=-2)

    style.map('flat.TButton',foreground=[('disabled', light_grey),
                    ('pressed', '#81899f'),
                    ('active', '#81899f')],
        background=[('active', '#81899f')],
        highlightcolor=[('focus', '#81899f'),
                        ('!focus', '#81899f')])
