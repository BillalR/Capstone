#this script sets up the gui ttk styles for all GUI elements

import tkinter as tk
from tkinter import ttk


grey = '#E4E4E4'
black = "#000000"

#lighter grey for scroll bars
light_grey = '#D3D7DA'
border_color = "#81899f"
background_color = "#2A363B"
text_over_color = "#3dabd9"


button_width = 20
button_height = 25
button_padding = 15
button_font = ('Helvetica Bold', 10)
button_font_menu = ('Helvetica Bold', 12)
button_font_menu2 = ('Helvetica Bold', 13)
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
    global background_color
    global border_color
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
    style.configure('unpressed.TButton',
                         foreground='black',
                         background = border_color,
                         width = button_width,
                         height = button_height,
                         relief = 'ridged',
                         padding = button_padding,
                         font = button_font_menu,
                         wrap=tk.WORD)
    style.map('unpressed.TButton',background = [('pressed', border_color),('disabled',grey)],foreground=[('active', background_color), ('pressed', background_color)])

    style.configure('unpressedSmall.TButton',
                         foreground='black',
                         background = border_color,
                         width = button_width,
                         height = button_height,
                         relief = 'ridged',
                         padding = button_padding,
                         font = button_font_menu2,
                         wrap=tk.WORD)
    style.map('unpressedSmall.TButton',background = [('pressed', 'red'),('!pressed', border_color),('disabled',grey)],foreground=[('active', background_color), ('pressed', background_color)])


    style.configure('pressed.TButton',
                         foreground='#BEBBBB',
                         background = background_color,
                         width = button_width,
                         height = button_height,
                         relief = 'ridged',
                         padding = button_padding,
                         font = button_font_menu,
                         wrap=tk.WORD)
    style.map('pressed.TButton',background = [('pressed', border_color),('disabled',grey)],foreground=[('active', "#BEBBBB"), ('pressed', background_color)])

    style.configure('popup.TButton',
                         foreground='black',
                         background = "#7EC4CF",
                         width = button_width/4,
                         height = button_height/2,
                         relief = 'flat',
                         padding = button_padding,
                         font=('Helvetica Bold', 12),
                         wrap=tk.WORD)
    style.map('popup.TButton',background = [('pressed', "#7EC4CF"),('disabled',grey)])

    style.configure('popup2.TButton',
                         foreground='black',
                         background = "#C7EBF0",
                         width = 10,
                         height = button_height/3,
                         relief = 'flat',
                         padding = button_padding*0.5,
                         font=('Helvetica Bold', 12),
                         wrap=tk.WORD)
    style.map('popup2.TButton',background = [('pressed', "#C7EBF0"),('disabled',grey)])


    #footer button
    style.configure('footer.TButton', foreground='white', background = "#7EC4CF", width = 10, height = footer_height, relief = 'flat', padding = button_padding, font = button_font, wrap=tk.WORD)
    style.map('footer.TButton',background = [('active', "#7EC4CF")])

    #big button
    style.configure('big.TButton', foreground='white', background = '#14B9D6', width = 5, height = 25, relief = 'flat', padding = 10, font = ('Helvetica Bold', 30),wrap=tk.WORD)
    style.map('big.TButton', background = [('active', 'white')])

    #small buttons
    style.configure('short.TButton', padding=button_padding*0.5)#flat and wide
    style.configure('small.TButton', padding=button_padding*0.5, width=10)#flat and short
    style.configure('tight.TButton', padding=button_padding*0.5, width=0)#flat and tight

    #generic frame style
    style.configure('TFrame', background=border_color, bd=0)
    style.configure('osk.TFrame', background=background_color, bd=0)


    style.configure('TLabel', background=border_color, font=('Helvetica Bold', 20), wrap=tk.WORD)
    style.configure('p.TLabel', background=border_color, font=('Helvetica Bold', 16), wrap=tk.WORD)
    style.configure('overBackground.TLabel', background=background_color,foreground=text_over_color, font=('Helvetica Bold', 20), wrap=tk.WORD)

    style.configure('E.TLabel', background=border_color,foreground = '#C7EBF0', font=('Helvetica Bold', 16), wrap=tk.WORD)

    #style.configure('pageLabel', background = 'red')

    #All of this below might need to be removed, it might tamper with other button styles
    #style.configure("TMenubutton", background=border_color)
    style.configure('flat.TButton',borderwidth=0,background=border_color,bd=-2)

    style.map('flat.TButton',foreground=[('disabled', light_grey),
                    ('pressed', border_color),
                    ('active', border_color)],
        background=[('active', border_color)],
        highlightcolor=[('focus', border_color),
                        ('!focus', border_color)])

    style.configure('image.TButton',borderwidth=0,background=background_color,bd=-2)

    style.map('image.TButton',foreground=[('disabled', light_grey),
                    ('pressed', background_color),
                    ('active', background_color)],
        background=[('active', background_color)],
        highlightcolor=[('focus', background_color),
                        ('!focus', background_color)])
