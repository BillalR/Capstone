#import base app package
from AppSetup.base_app import *
#import the screens
from mainScreen import *
from calibrationScreen import *



class home(base_app):
    def __init__(self, master):

        super().__init__(master)
        self.master = master

        self.SCR_MAIN = -1
        self.SCR_CALIBRATION = -1

        ##Define array of screens
        self.screens = []
        self.scrmap = [-1]
        self.numScreens = 0

        #Tk String Variables
        self.screenName = tk.StringVar()
        self.screenName.set("")


        #Main screen Initialize and Configuration
        self.SCR_MAIN = self.numScreens
        self.numScreens += 1
        self.screens.append(mainScreen(self.frame))

        #Calibration Screen Initialize and Configuration
        self.SCR_CALIBRATION = self.numScreens
        self.numScreens += 1
        self.screens.append(calibrationScreen(self.frame))

        #Load initial screen
        self.screens[self.SCR_MAIN].pack()
        self.scrmap.append(self.SCR_MAIN)

        #Footer information button
        #self.leftSide.logoButton.configure(command=self.infoLogo)
        self.leftSide.calibrateScreenButton.configure(command=self.combine_funcs(self.headsetCalibration, lambda: self.switchScreen(self.SCR_CALIBRATION, "Calibration")))
        self.leftSide.homeButton.configure(command= lambda: self.switchScreen(self.SCR_MAIN, "Home"), style="pressed.TButton")

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
        print(channel_data)
        self.master.after(4, self.lslTest)

    def serverConnect(self):
        if self.header.CType.get() == "UDP                    ":
            self.socket = self.UDPServerInit()
        elif self.header.CType.get() == "LSL                    ":
            self.inlet = self.lslServer()

        #Close popup
        self.messageWindow.closePopup()
        self.lslTest()

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
            #self.messageWindow.popupNoUser()
            pass
        else:
            pass

    def updateUserSelection(self):
        if self.messageWindow.userFlag == True:
            self.messageWindow.userFlag = False
            self.header.UserOPTIONS.insert(0, self.messageWindow.t1.get())
            self.header.user.set(self.messageWindow.t1.get())
            self.header.dropDown.children['menu'].add_command(label=self.messageWindow.t1.get(), command=lambda usr=self.messageWindow.t1.get(): self.header.user.set(usr))
            return
        else:
            pass
        self.master.after(50, self.updateUserSelection)

    def switchScreen(self, ID, pagename):
        if ID < 0:
            pass
        elif ID >= self.numScreens:
            return
        elif ID == self.scrmap[-1]:
            return
        if self.header.user.get() == "User" or self.header.user.get() == "New User...":
            self.messageWindow.popupNoUser()
            return

        #Change title of page and select the right button background
        self.screenName.set(str(pagename))
        self.header.title.configure(textvariable=self.screenName)
        if pagename == "Calibration":
            self.leftSide.homeButton.configure(style="unpressed.TButton")
            self.leftSide.calibrateScreenButton.configure(style="pressed.TButton")
        elif pagename == "Home":
            self.leftSide.homeButton.configure(style="pressed.TButton")
            self.leftSide.calibrateScreenButton.configure(style="unpressed.TButton")
        self.master.focus()
        self.screens[self.scrmap[-1]].pack_forget()
        self.scrmap.append(ID)
        self.screens[self.scrmap[-1]].pack()

    def switchBack(self):
        if self.scrmap[-2] < 0:
            return
        self.screens[self.scrmap[-1].pop()].pack_forget()
        self.screens[self.scrmap[-1]].pack()

    def switchHome(self):
        if self.scrmap[-1] == self.SCR_MAIN:
            pass
        else:
            self.screens[self.scrmap.pop()].pack_forget()
            self.scrmap = [-1, self.SCR_MAIN]
            self.screenName.set("Home")
            self.header.title.configure(textvariable=self.screenName)
            self.screens[self.SCR_MAIN].pack()


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
