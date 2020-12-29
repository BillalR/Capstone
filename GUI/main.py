#import base app package
from AppSetup.base_app import *
#import the screens
from mainScreen import *

class home(base_app):
    def __init__(self, master):
        #call the base app initializer (called super)
        #refer to base_app.py for documentation on what gets inherited
        super().__init__(master)
        self.master = master


        self.SCR_MAIN = -1

        ##Define array of screens
        self.screens = []
        self.scrmap = [-1]
        self.numScreens = 0

        #Main screen
        self.SCR_MAIN = self.numScreens
        self.numScreens += 1
        self.screens.append(mainScreen(self.frame))
        self.screens[self.SCR_MAIN].serialData.configure(command=self.lslTest)
        self.screens[self.SCR_MAIN].serialData


        #Load initial screen
        self.screens[self.SCR_MAIN].pack()
        self.scrmap.append(self.SCR_MAIN)

        #self.socket = self.UDPServerInit()
        #self.inlet = self.lslServer()

        #Trace calls from drop down menus
        self.header.individualName.trace("w", self.newUser)
        self.header.CType.trace("w", self.serverConnect)

    def newUser(self, *args):
        pass

    def UDPTest(self):
        data, addr = self.socket.recvfrom(2000)
        print(data)
        self.master.after(1000, self.comTest)

    def lslTest(self):
        channel_data = {}
        for i in range(4): # each of the 4 channels here
            sample, timestamp = self.inlet.pull_sample()
            if i not in channel_data:
                channel_data[i] = sample
            else:
                channel_data[i].append(sample)
        #print(channel_data)
        self.master.after(50, self.lslTest)

    def serverConnect(self, *args):
        if self.header.CType.get() == "UDP":
            self.socket = self.UDPServerInit()
        elif self.header.CType.get() == "LSL":
            self.inlet = self.lslServer()

#Launcher
#######################################
def main():

    root = tk.Tk()
    app = home(root)
    root.mainloop()

#stops code from executing unless it is the main,
#aka avoids executing code if just importing a class
if __name__ == '__main__':
    main()
