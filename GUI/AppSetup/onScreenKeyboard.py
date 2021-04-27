from tkinter import *
import tkinter

Keyboard_App = tkinter.Tk()

def select(value):
    if value == "<-":
        input = entry.get("1.0", 'end-2c')
        entry.delete("1.0", END)
        entry.insert("1.0", input, END)

    elif value == " Space ":
        entry.insert(tkinter.END, ' ')

    elif value == "Tab":
        entry.insert(tkinter.END, '   ')

    else:
        entry.insert(tkinter.END, value)

buttons = [
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '=',
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '<-',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '"',
    'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'SHIFT',
    ' Space ',
]
entry = Text(Keyboard_App, width=97, height=8)
entry.grid(row=1, columnspan=15)

varRow = 2
varColumn = 0

for button in buttons:
    command = lambda x=button: select(x)
    if button != " Space ":
        tkinter.Button(Keyboard_App, text=button, width=5, bg="#000000", fg="#ffffff",
                       activebackground="#ffffff", activeforeground="#000000", relief="raised", padx=12,
                       pady=4, bd=4, command=command).grid(row=varRow, column=varColumn)

    if button == " Space ":
        tkinter.Button(Keyboard_App, text=button, width=60, bg="#000000", fg="#ffffff",
                       activebackground="#ffffff", activeforeground="#000000", relief="raised", padx=4,
                       pady=4, bd=4, command=command).grid(row=6, columnspan=16)

    varColumn += 1
    if varColumn > 10:
        varColumn = 0
        varRow += 1
Keyboard_App.mainloop()
