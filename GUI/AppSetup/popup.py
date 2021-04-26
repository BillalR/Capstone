import tkinter as tk
from tkinter import ttk
import os
import csv
import pathlib
from AppSetup.base_app import *

class popupWindow:

    def __init__(self,master):
        self.master = master
        self.t1 = tk.StringVar()
        self.t1.set("")
        self.userFlag = False

    def popupConnection(self):
        self.popup_window = tk.Toplevel()
        scr_w = self.master.winfo_screenwidth()
        scr_h = self.master.winfo_screenheight()
        pop_w = 600
        pop_h = 200

        self.popup_window.geometry('%dx%d+%d+%d' % (pop_w, pop_h, (scr_w/2)-(pop_w/2), (scr_h/2)-(pop_h/2)))
        self.popup_window.title("Connecting")
        self.popupFrame = ttk.Frame(self.popup_window, style = 'TFrame')

        for rows in range (0,3):
            self.popupFrame.rowconfigure(rows, weight = 1)
        for cols in range (0,2):
            self.popupFrame.columnconfigure(cols, weight = 1)

        self.popupLabel = ttk.Label(self.popupFrame,style='TLabel', text="Connection is being established")
        self.popupLabel.grid(column=0, row=0, rowspan=1, columnspan=2, padx=20, pady=0)
        self.progressBar = ttk.Progressbar(self.popupFrame, orient=tk.HORIZONTAL,length=200,mode="indeterminate",takefocus=True,maximum=100)
        self.progressBar.grid(column=0, row=1, rowspan=1, columnspan=2, padx=20, pady=5)
        self.progressBar.start()

        self.popupLabel2 = ttk.Label(self.popupFrame,style='TLabel', text="Please wait until popup is destroyed")
        self.popupLabel2.grid(column=0, row=2, rowspan=1, columnspan=2, padx=20, pady=10)
        self.popupFrame.pack(expand = 1, fill = 'both')

    def popupInfo(self):
        self.popup_window = tk.Toplevel()
        scr_w = self.master.winfo_screenwidth()
        scr_h = self.master.winfo_screenheight()
        pop_w = 600
        pop_h = 400
        self.popup_window.geometry('%dx%d+%d+%d' % (pop_w, pop_h, (scr_w/2)-(pop_w/2), (scr_h/2)-(pop_h/2)))
        self.popup_window.title("Gen C. Team")
        self.popupFrame = ttk.Frame(self.popup_window, style = 'TFrame')

        self.popupLabel = ttk.Label(self.popupFrame,style='TLabel', text="Team info section")
        self.popupLabel.grid(column=0, row=0, rowspan=1, columnspan=2, padx=20, pady=0)

        self.popupFrame.pack(expand = 1, fill = 'both')

    def popupNoUser(self):
        self.popup_window = tk.Toplevel()
        scr_w = self.master.winfo_screenwidth()
        scr_h = self.master.winfo_screenheight()
        pop_w = 400
        pop_h = 100
        self.popup_window.geometry('%dx%d+%d+%d' % (pop_w, pop_h, (scr_w/2)-(pop_w/2), (scr_h/2)-(pop_h/2)))
        self.popup_window.title("Error")
        self.popupFrame = ttk.Frame(self.popup_window, style = 'TFrame')
        for rows in range (0,3):
            self.popupFrame.rowconfigure(rows, weight = 1)
        for cols in range (0,3):
            self.popupFrame.columnconfigure(cols, weight = 1)

        self.popupLabel = ttk.Label(self.popupFrame, style='E.TLabel', text="You must select a user to continue calibration")
        self.popupLabel.grid(column=0, row=0, rowspan=1, columnspan=2, padx=30, pady=0)

        self.okButton = ttk.Button(self.popupFrame,
                                     text = 'Ok',
                                     style = 'popup2.TButton',
                                     command = self.closePopupNewUser)
        self.okButton.grid(column=0, row=1, rowspan=1, columnspan=2, padx=20, pady=0)
        self.popupFrame.pack(expand = 1, fill = 'both')
        self.popupFrame.focus()

    def popupNoServer(self):
        self.popup_window = tk.Toplevel()
        scr_w = self.master.winfo_screenwidth()
        scr_h = self.master.winfo_screenheight()
        pop_w = 400
        pop_h = 100
        self.popup_window.geometry('%dx%d+%d+%d' % (pop_w, pop_h, (scr_w/2)-(pop_w/2), (scr_h/2)-(pop_h/2)))
        self.popup_window.title("Error")
        self.popupFrame = ttk.Frame(self.popup_window, style = 'TFrame')
        for rows in range (0,3):
            self.popupFrame.rowconfigure(rows, weight = 1)
        for cols in range (0,3):
            self.popupFrame.columnconfigure(cols, weight = 1)
        self.popupLabel = ttk.Label(self.popupFrame, style='E.TLabel', text="You must select a connection to continue calibration")
        self.popupLabel.grid(column=1, row=0, rowspan=1, columnspan=1, ipadx=0, pady=0)

        self.okButton = ttk.Button(self.popupFrame,
                                     text = 'Ok',
                                     style = 'popup2.TButton',
                                     command = self.closePopupNewUser)
        self.okButton.grid(column=0, row=1, rowspan=1, columnspan=2, padx=20, pady=0)
        self.popupFrame.pack(expand = 1, fill = 'both')
        self.popupFrame.focus()

    def popupNewUser(self, error):
        self.popup_window = tk.Toplevel()
        scr_w = self.master.winfo_screenwidth()
        scr_h = self.master.winfo_screenheight()
        pop_w = 400
        pop_h = 100
        self.popup_window.geometry('%dx%d+%d+%d' % (pop_w, pop_h, (scr_w/2)-(pop_w/2), (scr_h/2)-(pop_h/2)))
        self.popup_window.title("New User")
        self.popupFrame = ttk.Frame(self.popup_window, style = 'TFrame')
        for rows in range (0,3):
            self.popupFrame.rowconfigure(rows, weight = 1)
        for cols in range (0,1):
            self.popupFrame.columnconfigure(cols, weight = 1)

        self.popupFrame.focus()

        if error == 0:
            self.popupLabel = ttk.Label(self.popupFrame, style='p.TLabel', text="User:")
            #popupLabel.grid(column=0, row=1, rowspan=1, columnspan=1, padx=0, pady=0)
            self.popupLabel.place(x=50,y=34)
            self.e1 = tk.Entry(self.popupFrame,textvariable=self.t1, bd=0)
            self.e1.place(x=100,y=34)
            self.okButton = ttk.Button(self.popupFrame,
                                         text = 'Ok',
                                         style = 'popup2.TButton',
                                         command = self.userCSV)
            self.okButton.place(x=300,y=24)
            self.popupFrame.pack(expand = 1, fill = 'both')
        else:
            self.popupLabel = ttk.Label(self.popupFrame, style='p.TLabel', text="User:")
            #popupLabel.grid(column=0, row=1, rowspan=1, columnspan=1, padx=0, pady=0)
            self.popupLabel.place(x=50,y=34)
            self.errorLabel = ttk.Label(self.popupFrame, style='E.TLabel', text="Username Taken")
            #popupLabel.grid(column=0, row=1, rowspan=1, columnspan=1, padx=0, pady=0)
            self.errorLabel.place(x=125,y=10)
            self.e1 = tk.Entry(self.popupFrame,textvariable=self.t1, bd=0)
            self.e1.place(x=100,y=34)
            self.okButton = ttk.Button(self.popupFrame,
                                         text = 'Ok',
                                         style = 'popup2.TButton',
                                         command = self.userCSV)
            self.okButton.place(x=300,y=24)
            self.popupFrame.pack(expand = 1, fill = 'both')

    def closePopup(self):
        self.progressBar.stop()
        self.popupFrame.destroy()
        self.popup_window.destroy()
        self.popup_window = None
        return

    def closePopupNewUser(self):
        self.popupFrame.destroy()
        self.popup_window.destroy()
        self.popup_window = None
        self.master.focus()


    def userCSV(self):
        #First obtain any users from previously put added
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        script_dir = os.path.dirname(script_dir)
        rel_path = "/UserData/"
        abs_file_path = script_dir + rel_path
        if os.path.isfile(abs_file_path + "/" + str(self.t1.get())):
            self.closePopupNewUser()
            self.popupNewUser(1)
        else:
            File = os.mkdir(abs_file_path + "/" + str(self.t1.get()))
            self.userFlag = True
            self.closePopupNewUser()
