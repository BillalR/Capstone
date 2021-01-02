import tkinter as tk
from tkinter import ttk


class popupWindow:

    def __init__(self,master):

        self.master = master


    def popupConnection(self):
        self.popup_window = tk.Toplevel()
        scr_w = self.master.winfo_screenwidth()
        scr_h = self.master.winfo_screenheight()
        pop_w = 600
        pop_h = 200
        self.popup_window.geometry('%dx%d+%d+%d' % (pop_w, pop_h, (scr_w/2)-(pop_w/2), (scr_h/2)-(pop_h/2)))
        #self.popup_window.overrideredirect(True)
        self.popup_window.title("Connecting")
        self.popupFrame = ttk.Frame(self.popup_window, style = 'TFrame')
        for rows in range (0,3):
            self.popupFrame.rowconfigure(rows, weight = 1)
        for cols in range (0,2):
            self.popupFrame.columnconfigure(cols, weight = 1)

        popupLabel = ttk.Label(self.popupFrame,style='TLabel', text="Connection is being established")
        popupLabel.grid(column=0, row=0, rowspan=1, columnspan=2, padx=20, pady=0)

        self.p = ttk.Progressbar(self.popupFrame, orient=tk.HORIZONTAL,length=200,mode="indeterminate",takefocus=True,maximum=100)
        self.p.grid(column=0, row=1, rowspan=1, columnspan=2, padx=20, pady=5)
        self.p.start()

        popupLabel2 = ttk.Label(self.popupFrame,style='TLabel', text="Please wait until popup is destroyed")
        popupLabel2.grid(column=0, row=2, rowspan=1, columnspan=2, padx=20, pady=10)
        #text prompt and password entry
        '''
        popupLabel = ttk.Label(popupFrame, style='displaypop.TLabel', text=message)
        passwordVar = tk.StringVar()
        passwordEntry = ttk.Entry(popupFrame, style='TEntry', textvariable=passwordVar)
        passwordEntry.bind("<ButtonPress>", lambda e: osk.kb(master, passwordVar, writeOnLostFocus=True))
        if password==True:
            popupLabel.grid(column=0, row=0, rowspan=1, columnspan=2, padx=20, pady=5)
            passwordEntry.grid(column=0, row=1, rowspan=1, columnspan=2, padx=20, pady=5)
        else:
            popupLabel.grid(column=0, row=0, rowspan=2, columnspan=2, padx=20, pady=20)

        #cancel button
        cancelButton = ttk.Button(popupFrame, text = cancelLabel, style = 'gui.TButton', command = lambda: cancelPressed(cancelCommand))

        #okay button
        OKButton = ttk.Button(popupFrame, text = okayLabel, style = 'gui.TButton')
        if password == True:
            OKButton.configure(command = lambda: okayPressed(okayCommand, passwordVar.get()))
        else:
            OKButton.configure(command = lambda: okayPressed(okayCommand))

        #grid the buttons
        if cancel==True:
            cancelButton.grid(column=0, row=2, pady=20, padx=20)
            OKButton.grid(column=1, row=2, pady=20, padx=20)
        else:
            OKButton.grid(column=0,columnspan=2, row=2, pady=20, padx=20)
        '''
        self.popupFrame.pack(expand = 1, fill = 'both')
    '''
    def okayPressed(action=None, password=None):
        if password == None or password == PASSWORD:
            if action != None:
                action()
        closePopup()

    def cancelPressed(action=None):
        if action != None:
            action()
        closePopup()
    '''

    def popupInfo(self):
        self.popup_window = tk.Toplevel()
        scr_w = self.master.winfo_screenwidth()
        scr_h = self.master.winfo_screenheight()
        pop_w = 600
        pop_h = 400
        self.popup_window.geometry('%dx%d+%d+%d' % (pop_w, pop_h, (scr_w/2)-(pop_w/2), (scr_h/2)-(pop_h/2)))
        self.popup_window.title("Gen C. Team")
        self.popupFrame = ttk.Frame(self.popup_window, style = 'TFrame')

        popupLabel = ttk.Label(self.popupFrame,style='TLabel', text="Team info section")
        popupLabel.grid(column=0, row=0, rowspan=1, columnspan=2, padx=20, pady=0)

        self.popupFrame.pack(expand = 1, fill = 'both')

    def closePopup(self):
        self.p.stop()
        self.popupFrame.destroy()
        self.popup_window.destroy()
        self.popup_window = None
