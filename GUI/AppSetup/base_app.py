import os
import platform
import tkinter as tk
from tkinter import ttk
import time
import serial
import socket
from pylsl import StreamInlet, resolve_stream

#Import window components
from AppSetup import window_setup as winSet
from AppSetup import header_bar, footer_bar
from AppSetup import popup as pop



class base_app:
    def __init__(self, master, removable_frame=None):

        #the removable frame option is for when you want to use screens without the header/footer (screen_Splash)
        self.master = master
        if removable_frame == None:
            self.removable_frame = master
        else:
            self.removable_frame = removable_frame
        self.master.configure(bg = 'white')

        #Master Styles
        self.style = ttk.Style()
        winSet.init_default_window(self.master, self.style)

        #init the header bar
        self.master.title("Gencephalon")

        self.header = header_bar.header(self.removable_frame)
        self.footer = footer_bar.footer(self.removable_frame)
        #init the center screen (screens need to be placed on this frame)
        self.frame = ttk.Frame(self.removable_frame, style='TFrame')
        self.frame.pack(expand = 1, fill = 'both')

        #define variables for the hidden quit button
        self._countdown_to_quit = 5
        self._countdown_time = time.time()



    def quitApp(self):
        os._exit(0)


    #UDP Server Connection
    def UDPServerInit(self):
        localIP = "127.0.0.1"
        localPort = 20001
        bufferSize = 2000

        UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        UDPServerSocket.bind((localIP, localPort))

        print("UDP server up and listening")

        return UDPServerSocket

    def lslServer(self):
        # first resolve an EEG stream on the lab network
        print("looking for an EEG stream...")
        self.streams = resolve_stream('type', 'EEG')
        # create a new inlet to read from the stream
        self.inlet = StreamInlet(self.streams[0])

        return self.inlet

    def combine_funcs(self, *funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combined_func

#Launcher
#######################################
def main():
    root = tk.Tk()
    app = base_app(root)
    root.mainloop()

#stops code from executing unless it is the main,
#aka avoids executing code if just importing a class
if __name__ == '__main__':
    main()
