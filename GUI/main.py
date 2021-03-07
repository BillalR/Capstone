#import base app package
from AppSetup.base_app import *
import pygame
import threading
import csv
import numpy as np
import pandas as pd
import statistics as st
from scipy import signal
from sklearn.preprocessing import StandardScaler

#import the screens or models
from mainScreen import *
from calibrationScreen1 import *
from calibrationScreen2 import *
from calibrationScreen3 import *
from calibrationScreen4 import *
from calibrationScreen5 import *
from calibrationScreen6 import *
from calibrationScreen7 import *
from calibrationScreen8 import *
from calibrationScreen9 import *
from calibrationScreen10 import *
from testingScreen import *
from testingScreenPlot import *
from quickScreen import *
from keyboardScreen import *
from knnML import *
from svmModel import *

'''
Just some comments on the perception, in case you forget...

0: Neutral State
1: On thought
2: Off thought

'''


class home(base_app):
    def __init__(self, master):

        super().__init__(master)
        self.master = master



        self.SCR_MAIN = -1
        self.SCR_CALIBRATION1 = -1
        self.SCR_CALIBRATION2 = -1
        self.SCR_CALIBRATION3 = -1 #<-- Neutral State processing
        self.SCR_CALIBRATION4 = -1
        self.SCR_CALIBRATION5 = -1
        self.SCR_CALIBRATION6 = -1
        self.SCR_CALIBRATION7 = -1
        self.SCR_CALIBRATION8 = -1 #<-- On LED state processing
        self.SCR_CALIBRATION9 = -1 #<-- Off LED state processing
        self.SCR_CALIBRATION10 = -1
        self.SCR_TESTING = -1
        self.SCR_TESTINGPLOT = -1
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
        self.channelNames = ["FP1","CZ","FZ","C3","C4","F3","O1","O2","Perception"]
        #self.channelNames = ["FP1","CZ","FZ","C3","C4","Perception"]
        self.channel_data = {}
        self.dataInput = []

        #Machine Learning Model Selection
        self.model = None

        #Flags
        self.read = False
        self.startOnce = True

        #Main screen Initialize and Configuration
        self.SCR_MAIN = self.numScreens
        self.numScreens += 1
        self.screens.append(mainScreen(self.frame))

        #Testing Screen Plot Initialize and Configuration
        self.SCR_TESTINGPLOT = self.numScreens
        self.numScreens += 1
        self.screens.append(testingScreenPlot(self.frame))
        #self.screens[self.SCR_TESTING].testingButton.configure(command= lambda: threading.Thread(target=self.readGeneralBrainData).start())
        #self.screens[self.SCR_TESTING].testingButton.configure(command= lambda: self.testData)

        #Testing Screen Initialize and Configuration
        self.SCR_TESTING = self.numScreens
        self.numScreens += 1
        self.screens.append(testingScreen(self.frame))
        self.screens[self.SCR_TESTING].testingButton.configure(command= lambda: threading.Thread(target=self.readGeneralBrainData).start())
        #self.screens[self.SCR_TESTING].testingButton.configure(command= self.combine_funcs(lambda: self.testData, lambda: self.switchScreen(self.SCR_TESTINGPLOT, "Testing")))
        #self.screens[self.SCR_TESTING].testingButton.configure(command= lambda: threading.Thread(target=self.testData))

        #Calibration Screen 3 Initialize and Configuration
        self.SCR_QUICK = self.numScreens
        self.numScreens += 1
        self.screens.append(quickScreen(self.frame))

        #Calibration Screen 3 Initialize and Configuration
        self.SCR_KEYBOARD = self.numScreens
        self.numScreens += 1
        self.screens.append(keyboardScreen(self.frame))

        #Calibration Screen 10 Initialize and Configuration
        self.SCR_CALIBRATION10 = self.numScreens
        self.numScreens += 1
        self.screens.append(calibrationScreen10(self.frame))

        #Calibration Screen 9 Initialize and Configuration
        self.SCR_CALIBRATION9 = self.numScreens
        self.numScreens += 1
        self.screens.append(calibrationScreen9(self.frame))

        #Calibration Screen 7 Initialize and Configuration
        self.SCR_CALIBRATION8 = self.numScreens
        self.numScreens += 1
        self.screens.append(calibrationScreen8(self.frame))

        #Calibration Screen 7 Initialize and Configuration
        self.SCR_CALIBRATION7 = self.numScreens
        self.numScreens += 1
        self.screens.append(calibrationScreen7(self.frame))
        self.screens[self.SCR_CALIBRATION7].offStateReadButton.configure(command= self.combine_funcs(lambda: self.switchScreen(self.SCR_CALIBRATION9, "Calibration"), self.offStateTimer))

        #Calibration Screen 6 Initialize and Configuration
        self.SCR_CALIBRATION6 = self.numScreens
        self.numScreens += 1
        self.screens.append(calibrationScreen6(self.frame))
        self.screens[self.SCR_CALIBRATION6].calibrationRedoButton.configure(command= lambda: self.switchScreen(self.SCR_CALIBRATION5, "Calibration"))
        self.screens[self.SCR_CALIBRATION6].calibrationContinueButton.configure(command= lambda: self.switchScreen(self.SCR_CALIBRATION7, "Calibration"))

        #Calibration Screen 5 Initialize and Configuration
        self.SCR_CALIBRATION5 = self.numScreens
        self.numScreens += 1
        self.screens.append(calibrationScreen5(self.frame))
        self.screens[self.SCR_CALIBRATION5].onStateReadButton.configure(command= self.combine_funcs(lambda: self.switchScreen(self.SCR_CALIBRATION8, "Calibration"), self.onStateTimer))

        #Calibration Screen 4 Initialize and Configuration
        self.SCR_CALIBRATION4 = self.numScreens
        self.numScreens += 1
        self.screens.append(calibrationScreen4(self.frame))
        self.screens[self.SCR_CALIBRATION4].calibrationRedoButton.configure(command= lambda: self.switchScreen(self.SCR_CALIBRATION2, "Calibration"))
        self.screens[self.SCR_CALIBRATION4].calibrationContinueButton.configure(command= lambda: self.switchScreen(self.SCR_CALIBRATION5, "Calibration"))

        #Calibration Screen 3 Initialize and Configuration
        self.SCR_CALIBRATION3 = self.numScreens
        self.numScreens += 1
        self.screens.append(calibrationScreen3(self.frame))

        #Calibration Screen 2 Initialize and Configuration
        self.SCR_CALIBRATION2 = self.numScreens
        self.numScreens += 1
        self.screens.append(calibrationScreen2(self.frame))
        self.screens[self.SCR_CALIBRATION2].neutralStateReadButton.configure(command= self.combine_funcs(lambda: self.switchScreen(self.SCR_CALIBRATION3, "Calibration"), self.neutralStateTimer))

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
        self.menuSelect.calibrateScreenButton.configure(command= lambda: self.switchScreen(self.SCR_CALIBRATION1, "Calibration"))
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

        #Initalize your model if the user already has calibration data



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

    def redoBool(self):
        self.redo = True
        return

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

    def generateKNNModel(self):
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        script_dir = os.path.dirname(script_dir)
        rel_path = "/GUI/UserData/"
        abs_file_path = os.path.join(script_dir, rel_path)
        self.model = KNN(script_dir + rel_path + self.header.user.get() + "/Data.csv")
        return

    '''
    All of the functions contained below will correspond to the
    accumulation of data from various states
    '''

    def readNeutralState(self):
        count = 0
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        script_dir = os.path.dirname(script_dir)
        rel_path = "/GUI/UserData/"
        abs_file_path = os.path.join(script_dir, rel_path)
        fs = 250/2
        if os.path.exists(script_dir + rel_path + self.header.user.get() + "/Data.csv"):
            os.remove(script_dir + rel_path + self.header.user.get() + "/Data.csv")
            print("Data has been overridden")

        while self.read == True:
            for i in range(9):
                if i == 8:
                    perception = 0
                    self.channel_data[i] = perception
                else:
                    sample,timestamp = self.inlet.pull_sample()
                    if i not in self.channel_data:
                        F, PSD = signal.welch(sample, fs, nperseg=len(sample))
                        self.channel_data[i] = st.mean(PSD)

            if count == 0:
                df = pd.DataFrame.from_dict(self.channel_data, orient="index")
                df = df.T
                df.to_csv(script_dir + rel_path + self.header.user.get() + "/Data.csv", mode="a", header=self.channelNames)
                self.channel_data = {}
                count = count + 1
            else:
                df = pd.DataFrame.from_dict(self.channel_data, orient="index")
                df = df.T
                df.to_csv(script_dir + rel_path + self.header.user.get() + "/Data.csv", mode="a", header=False)
                self.channel_data = {}
        return

    def readOnState(self):
        count = 0
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        script_dir = os.path.dirname(script_dir)
        rel_path = "/GUI/UserData/"
        abs_file_path = os.path.join(script_dir, rel_path)
        fs = 250/2
        '''
        if os.path.exists(script_dir + rel_path + self.header.user.get() + "/Data.csv"):
            os.remove(script_dir + rel_path + self.header.user.get() + "/Data.csv")
            print("On Off State data has been overridden")
        '''
        while self.read == True:
            for i in range(9):
                if i == 8:
                    perception = 1
                    self.channel_data[i] = perception
                else:
                    sample,timestamp = self.inlet.pull_sample()
                    if i not in self.channel_data:
                        F, PSD = signal.welch(sample, fs, nperseg=len(sample))
                        self.channel_data[i] = st.mean(PSD)

            df = pd.DataFrame.from_dict(self.channel_data, orient="index")
            df = df.T
            df.to_csv(script_dir + rel_path + self.header.user.get() + "/Data.csv", mode="a", header=False)
            self.channel_data = {}
            '''
            if count == 0:
                df = pd.DataFrame.from_dict(self.channel_data, orient="index")
                df = df.T
                df.to_csv(script_dir + rel_path + self.header.user.get() + "/Data.csv", mode="a", header=self.channelNames)
                self.channel_data = {}
                count = count + 1
            else:
                df = pd.DataFrame.from_dict(self.channel_data, orient="index")
                df = df.T
                df.to_csv(script_dir + rel_path + self.header.user.get() + "/Data.csv", mode="a", header=False)
                self.channel_data = {}
            '''

        return

    def readOffState(self):
        #count = 0
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        script_dir = os.path.dirname(script_dir)
        rel_path = "/GUI/UserData/"
        abs_file_path = os.path.join(script_dir, rel_path)
        fs = 250/2
        '''
        if os.path.exists(script_dir + rel_path + self.header.user.get() + "/Data.csv"):
            os.remove(script_dir + rel_path + self.header.user.get() + "/Data.csv")
            print("On Off State data has been overridden")
        '''

        while self.read == True:
            for i in range(9):
                if i == 8:
                    perception = 2
                    self.channel_data[i] = perception
                else:
                    sample,timestamp = self.inlet.pull_sample()
                    if i not in self.channel_data:
                        F, PSD = signal.welch(sample, fs, nperseg=len(sample))
                        self.channel_data[i] = st.mean(PSD)

            df = pd.DataFrame.from_dict(self.channel_data, orient="index")
            df = df.T
            df.to_csv(script_dir + rel_path + self.header.user.get() + "/Data.csv", mode="a", header=False)
            self.channel_data = {}
        return

    def neutralStateTimer(self):
        self.read = True
        if self.startOnce == True:
            threading.Thread(target=self.readNeutralState).start()
            self.startOnce = False
        if self.screens[self.SCR_CALIBRATION3].counter_1.get() > 0:
            self.screens[self.SCR_CALIBRATION3].progressBar.start()
            temp = self.screens[self.SCR_CALIBRATION3].counter_1.get() - 1
            self.screens[self.SCR_CALIBRATION3].counter_1.set(int(temp))
        else:
            self.read = False
            self.startOnce = True
            self.screens[self.SCR_CALIBRATION3].counter_1.set(30)
            self.switchScreen(self.SCR_CALIBRATION4, "Calibration") #Move onto the next calibration screen for on and off
            #Read in audio file for calibration completion
            script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
            rel_path = "AppSetup/SoundNotifications/ding.mp3"
            abs_file_path = os.path.join(script_dir, rel_path)
            #pygame.mixer.music.load(abs_file_path)
            #pygame.mixer.music.play(loops=0)
            return
        self.master.after(1000, self.neutralStateTimer)

    def onStateTimer(self):
        self.read = True
        if self.startOnce == True:
            threading.Thread(target=self.readOnState).start()
            self.startOnce = False
        if self.screens[self.SCR_CALIBRATION8].counter_1.get() > 0:
            self.screens[self.SCR_CALIBRATION8].progressBar.start()
            temp = self.screens[self.SCR_CALIBRATION8].counter_1.get() - 1
            self.screens[self.SCR_CALIBRATION8].counter_1.set(int(temp))
        else:
            self.read = False
            self.startOnce = True
            self.screens[self.SCR_CALIBRATION8].counter_1.set(30)
            self.switchScreen(self.SCR_CALIBRATION6, "Calibration") #Move onto the next calibration screen for on and off
            #Read in audio file for calibration completion
            script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
            rel_path = "AppSetup/SoundNotifications/ding.mp3"
            abs_file_path = os.path.join(script_dir, rel_path)
            #pygame.mixer.music.load(abs_file_path)
            #pygame.mixer.music.play(loops=0)
            return
        self.master.after(1000, self.onStateTimer)

    def offStateTimer(self):
        self.read = True
        if self.startOnce == True:
            threading.Thread(target=self.readOffState).start()
            self.startOnce = False
        if self.screens[self.SCR_CALIBRATION9].counter_1.get() > 0:
            self.screens[self.SCR_CALIBRATION9].progressBar.start()
            temp = self.screens[self.SCR_CALIBRATION9].counter_1.get() - 1
            self.screens[self.SCR_CALIBRATION9].counter_1.set(int(temp))
        else:
            self.read = False
            self.startOnce = True
            self.screens[self.SCR_CALIBRATION9].counter_1.set(30)
            self.switchScreen(self.SCR_CALIBRATION10, "Calibration") #Move onto the next calibration screen for on and off
            #Read in audio file for calibration completion
            script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
            rel_path = "AppSetup/SoundNotifications/ding.mp3"
            abs_file_path = os.path.join(script_dir, rel_path)
            #pygame.mixer.music.load(abs_file_path)
            #pygame.mixer.music.play(loops=0)
            threading.Thread(target=self.generateKNNModel).start()
            return
        self.master.after(1000, self.offStateTimer)

    '''
    End of state accumulation functions

    '''


    '''

    Start of running tests on brain wave data and ml model

    '''

    #def testOutput(self):
    #    pass

    def readGeneralBrainData(self):
        fs = 250/2
        while self.model != None:
            for i in range(8):
                sample,timestamp = self.inlet.pull_sample()
                if i not in self.channel_data:
                    F, PSD = signal.welch(sample, fs, nperseg=len(sample))
                    #self.channel_data[i] = st.mean(PSD)
                    self.dataInput.append(st.mean(PSD))

            #df = pd.DataFrame.from_dict(self.channel_data, orient="index")
            #df = df.T
            #self.channel_data = {}
            #df = df.drop(df.columns[[0]], axis=1)
            #data = df.iloc[:, 0:self.model.numChannels]

            #sc_X = StandardScaler()
            #data = sc_X.fit_transform(data)
            #print(data)
            #print(self.dataInput)
            temp = [self.dataInput]
            #temp = np.array(self.dataInput)
            #temp = self.dataInput.iloc[:, 0:self.model.numChannels]
            modelOutput = self.model.classifier.predict(temp)
            self.dataInput = []
            #print(modelOutput)

            if modelOutput == 1:
                #self.arduinoBoard.board.digitalWrite(13, "HIGH")
                print("On")
                #time.sleep(1)
            elif modelOutput == 2:
                #self.arduinoBoard.board.digitalWrite(13,"LOW")
                print("Off")
                #time.sleep(1)
            elif modelOutput == 0:
                print("Neutral")
            time.sleep(0.01)



    def runNetwork(self, *args):
        self.messageWindow.popupConnection()
        #Popup needs to be forced refresh to display
        self.master.update()
        self.serverConnect()

    def infoLogo(self):
        self.master.focus()
        self.messageWindow.popupInfo()
        #Popup needs to be forced refresh to display
        self.master.update()


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
        elif self.header.CType.get() == "Connection Type":
            self.messageWindow.popupNoServer()
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

if __name__ == '__main__':
    main()
