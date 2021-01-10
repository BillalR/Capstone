#import base app package
from AppSetup.base_app import *
#import the screens
from mainScreen import *



class home(base_app):
    def __init__(self, master):

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
        self.screens[self.SCR_MAIN].calibrateButton.configure(command=self.headsetCalibration)


        #Load initial screen
        self.screens[self.SCR_MAIN].pack()
        self.scrmap.append(self.SCR_MAIN)

        #Footer information button
        self.footer.logoButton.configure(command=self.infoLogo)

        #Trace calls from drop down menus
        self.header.user.trace("w", self.switchUser)
        self.header.CType.trace("w", self.runNetwork)

        #Popup init
        self.messageWindow = pop.popupWindow(self.master)

    def switchUser(self, *args):
        if self.header.user.get() == "New User...":
            self.messageWindow.t1.set("")
            self.messageWindow.popupNewUser(0)
            self.updateUserSelection()
        else:
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
        self.master.after(50, self.lslTest)

    def serverConnect(self):
        if self.header.CType.get() == "UDP                    ":
            self.socket = self.UDPServerInit()
        elif self.header.CType.get() == "LSL                    ":
            self.inlet = self.lslServer()

        #Close popup
        self.messageWindow.closePopup()

    def runNetwork(self, *args):
        #Initalize popup window class
        self.messageWindow.popupConnection()
        #Popup needs to be forced refresh to display
        self.master.update()
        self.serverConnect()

    def infoLogo(self):
        self.master.focus()
        self.messageWindow.popupInfo()
        #Popup needs to be forced refresh to display
        self.master.update()

    def headsetCalibration(self):
        if self.header.user.get() == "User":
            self.master.focus()
            self.messageWindow.popupNoUser()
        else:
            pass

    def updateUserSelection(self):
        if self.messageWindow.userFlag == True:
            self.messageWindow.userFlag = False
            self.header.UserOPTIONS.append(self.messageWindow.t1.get())
            self.header.user.set(self.messageWindow.t1.get())
            self.header.dropDown.children['menu'].add_command(label=self.messageWindow.t1.get(), command=lambda usr=self.messageWindow.t1.get(): self.header.user.set(usr))
            return
        else:
            pass
        self.master.after(50, self.updateUserSelection)




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
