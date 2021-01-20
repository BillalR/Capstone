#import base app package
from AppSetup.base_app import *
import pygame
import threading
#import the screens
from mainScreen import *
from calibrationScreen1 import *
from calibrationScreen2 import *
from calibrationScreen3 import *
from calibrationScreen4 import *
from testingScreen import *
from quickScreen import *
from keyboardScreen import *
from knnML import *


class home(base_app):
    def __init__(self, master):

        super().__init__(master)
        self.master = master

        self.SCR_MAIN = -1
        self.SCR_CALIBRATION1 = -1
        self.SCR_CALIBRATION2 = -1
        self.SCR_CALIBRATION3 = -1
        self.SCR_CALIBRATION4 = -1
        self.SCR_TESTING = -1
        self.SCR_QUICK = -1
        self.SCR_KEYBOARD = -1

        ##Define array of screens
        self.screens = []
        self.scrmap = [-1]
        self.numScreens = 0

        #Tk String Variables
        self.screenName = tk.StringVar()
        self.screenName.set("")

        #Array lists of data
        self.channel_data = {}

        #Flags
        self.read = False

        #Main screen Initialize and Configuration
        self.SCR_MAIN = self.numScreens
        self.numScreens += 1
        self.screens.append(mainScreen(self.frame))

        #Calibration Screen 3 Initialize and Configuration
        self.SCR_CALIBRATION3 = self.numScreens
        self.numScreens += 1
        self.screens.append(calibrationScreen3(self.frame))

        #Calibration Screen 2 Initialize and Configuration
        self.SCR_CALIBRATION2 = self.numScreens
        self.numScreens += 1
        self.screens.append(calibrationScreen2(self.frame))
        self.screens[self.SCR_CALIBRATION2].neutralStateReadButton.configure(command= self.combine_funcs(lambda: self.switchScreen(self.SCR_CALIBRATION3, "Calibration"), self.combine_funcs(self.readNeutralData,self.countDown)))

        #Calibration Screen 1 Initialize and Configuration
        self.SCR_CALIBRATION1 = self.numScreens
        self.numScreens += 1
        self.screens.append(calibrationScreen1(self.frame))
        #To forget about a button or label, use -- Grid Forget
        #self.screens[self.SCR_CALIBRATION1].neautralImage.grid_forget()
        self.screens[self.SCR_CALIBRATION1].neutralButtonCalibration.configure(command= lambda: self.switchScreen(self.SCR_CALIBRATION2, "Calibration"))

        #Pack the initial screen
        self.screens[self.SCR_MAIN].pack()
        self.scrmap.append(self.SCR_MAIN)

        #Side Menu configuration
        self.menuSelect.calibrateScreenButton.configure(command=self.combine_funcs(self.headsetCalibration, lambda: self.switchScreen(self.SCR_CALIBRATION1, "Calibration")))
        self.menuSelect.homeButton.configure(command= lambda: self.switchScreen(self.SCR_MAIN, "Home"), style="pressed.TButton")
        self.menuSelect.testButton.configure(command= lambda: self.switchScreen(self.SCR_TESTING, "Testing"),  style="unpressed.TButton")
        self.menuSelect.quickButton.configure(command=lambda: self.switchScreen(self.SCR_QUICK, "Quick Menu"), style="unpressed.TButton")
        self.menuSelect.keyboardButton.configure(command=lambda: self.switchScreen(self.SCR_KEYBOARD, "Keyboard"), style="unpressed.TButton")

        #Trace calls from drop down menus
        self.header.user.trace("w", self.switchUser)
        self.header.CType.trace("w", self.runNetwork)

        #Popup init
        self.messageWindow = pop.popupWindow(self.master)

        #Initalize mixer for sound notifications
        pygame.mixer.init()


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

    '''
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
    '''

    def serverConnect(self):
        if self.header.CType.get() == "UDP                    ":
            self.socket = self.UDPServerInit()
        elif self.header.CType.get() == "LSL                    ":
            self.inlet = self.lslServer()

        #Close popup
        self.messageWindow.closePopup()
        #self.lslTest()

    def readNeutralData(self):
        if self.read == True:
            for i in range(8):
                sample,timestamp = self.inlet.pull_sample()
                if i not in self.channel_data:
                    self.channel_data[i] = sample
                else:
                    self.channel_data[i].append(sample)
        else:
            print(self.channel_data)
            return
        self.master.after(4,self.readNeutralData)

    def generateKNNModel(self):
        pass

    def countDown(self):
        self.read = True
        if self.screens[self.SCR_CALIBRATION3].counter_1.get() > 0:
            self.screens[self.SCR_CALIBRATION3].progressBar.start()
            temp = self.screens[self.SCR_CALIBRATION3].counter_1.get() - 10
            self.screens[self.SCR_CALIBRATION3].counter_1.set(int(temp))
        else:
            self.read = False
            self.screens[self.SCR_CALIBRATION3].counter_1.set(30)
            self.switchScreen(self.SCR_CALIBRATION1, "Calibration")
            #Read in audio file for calibration completion
            script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
            rel_path = "AppSetup/SoundNotifications/ding.mp3"
            abs_file_path = os.path.join(script_dir, rel_path)
            pygame.mixer.music.load(abs_file_path)
            pygame.mixer.music.play(loops=0)
            self.read = False
            return
        self.master.after(1000, self.countDown)

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

    def switchScreen(self, ID, page):
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
        '''
        self.screenName.set(str(page))
        self.header.title.configure(textvariable=self.screenName)
        '''

        if page == "Calibration":
            self.menuSelect.quickButton.configure(style="unpressed.TButton")
            self.menuSelect.homeButton.configure(style="unpressed.TButton")
            self.menuSelect.calibrateScreenButton.configure(style="pressed.TButton")
            self.menuSelect.testButton.configure(style="unpressed.TButton")
            self.menuSelect.keyboardButton.configure(style="unpressed.TButton")
        elif page == "Home":
            self.menuSelect.quickButton.configure(style="unpressed.TButton")
            self.menuSelect.homeButton.configure(style="pressed.TButton")
            self.menuSelect.calibrateScreenButton.configure(style="unpressed.TButton")
            self.menuSelect.testButton.configure(style="unpressed.TButton")
            self.menuSelect.keyboardButton.configure(style="unpressed.TButton")
        elif page == "Testing":
            self.menuSelect.quickButton.configure(style="unpressed.TButton")
            self.menuSelect.calibrateScreenButton.configure(style="unpressed.TButton")
            self.menuSelect.homeButton.configure(style="unpressed.TButton")
            self.menuSelect.testButton.configure(style="pressed.TButton")
            self.menuSelect.keyboardButton.configure(style="unpressed.TButton")
        elif page == "Quick Menu":
            self.menuSelect.testButton.configure(style="unpressed.TButton")
            self.menuSelect.calibrateScreenButton.configure(style="unpressed.TButton")
            self.menuSelect.homeButton.configure(style="unpressed.TButton")
            self.menuSelect.quickButton.configure(style="pressed.TButton")
            self.menuSelect.keyboardButton.configure(style="unpressed.TButton")
        elif page == "Keyboard":
            self.menuSelect.testButton.configure(style="unpressed.TButton")
            self.menuSelect.calibrateScreenButton.configure(style="unpressed.TButton")
            self.menuSelect.homeButton.configure(style="unpressed.TButton")
            self.menuSelect.quickButton.configure(style="unpressed.TButton")
            self.menuSelect.keyboardButton.configure(style="pressed.TButton")

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
