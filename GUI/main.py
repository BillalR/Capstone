#import base app package
from AppSetup.base_app import *
import pygame
import threading
import csv
import numpy as np
import pandas as pd
import statistics as st
from scipy import signal
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import time
import pywt
import pathlib
from skimage.restoration import denoise_wavelet

#import the screens or models
from mainScreen import *
from calibrationScreen1 import *
from calibrationScreen2 import *
from calibrationScreen3 import *
from calibrationScreen3b import *
from calibrationScreen4 import *
from calibrationScreen5 import *
from calibrationScreen6 import *
from calibrationScreen7 import *
from calibrationScreen8 import *
from calibrationScreen9 import *
from calibrationScreen10 import *
from calibrationScreen11 import *
from calibrationScreen12 import *
from calibrationScreen13 import *
from testingScreen import *
from testingScreen2 import *
from testingScreen3 import *
from testingScreenPlot import *
from quickScreen import *
from keyboardScreen import *
from knnML import *
from testkey import *
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
        self.SCR_CALIBRATION3 = -1 #<-- State processing screen
        self.SCR_CALIBRATION3b = -1 #<-- State processing screen
        self.SCR_CALIBRATION4 = -1
        self.SCR_CALIBRATION5 = -1
        self.SCR_CALIBRATION6 = -1
        self.SCR_CALIBRATION7 = -1
        self.SCR_CALIBRATION8 = -1 #<-- On LED state processing
        self.SCR_CALIBRATION9 = -1 #<-- Off LED state processing
        self.SCR_CALIBRATION10 = -1
        self.SCR_CALIBRATION11 = -1
        self.SCR_CALIBRATION12 = -1
        self.SCR_CALIBRATION13 = -1
        self.SCR_TESTING = -1
        self.SCR_TESTING2 = -1
        self.SCR_TESTING3 = -1
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
        self.channel_data = {}
        self.time_data = {}
        self.dataInput = []

        #Machine Learning Model Selection
        self.model = None

        #Flags
        self.read = False
        self.startOnce = True
        self.headerOnce = False
        self.FFT = False
        self.Time = False
        self.startUp = True

        #Counters
        self.loops = 0
        self.count = 0
        self.stateCount = 1
        self.processCount = 0

        #General Variables for Simplicity
        self.calCycles = 6

        #Main screen Initialize and Configuration
        self.SCR_MAIN = self.numScreens
        self.numScreens += 1
        self.screens.append(mainScreen(self.frame))

        #Testing Screen Plot Initialize and Configuration
        self.SCR_TESTINGPLOT = self.numScreens
        self.numScreens += 1
        self.screens.append(testingScreenPlot(self.frame))

        #Testing Screen Initialize and Configuration
        self.SCR_TESTING = self.numScreens
        self.numScreens += 1
        self.screens.append(testingScreen(self.frame))
        self.screens[self.SCR_TESTING].testingButton.configure(command= lambda: threading.Thread(target=self.readGeneralBrainData).start())
        self.screens[self.SCR_TESTING].CNNButton.configure(command= self.combine_funcs(lambda: threading.Thread(target=self.generateCNNModel).start(), self.domainTimeInit))
        self.screens[self.SCR_TESTING].KNNButton.configure(command= self.combine_funcs(lambda: threading.Thread(target=self.generateKNNModel).start(),self.domainFFTInit))

        #Testing Screen TWO
        self.SCR_TESTING2 = self.numScreens
        self.numScreens += 1
        self.screens.append(testingScreen2(self.frame))

        #Testing Screen THREE
        self.SCR_TESTING3 = self.numScreens
        self.numScreens += 1
        self.screens.append(testingScreen3(self.frame))

        #Quick Menu Initialize and Configuration
        self.SCR_QUICK = self.numScreens
        self.numScreens += 1
        self.screens.append(quickScreen(self.frame))

        #Keyboard Screen Initialize and Configuration
        self.SCR_KEYBOARD = self.numScreens
        self.numScreens += 1
        self.screens.append(keyboardScreen(self.frame))

        #Calibration Screen 13 Initialize and Configuration
        self.SCR_CALIBRATION13 = self.numScreens
        self.numScreens += 1
        self.screens.append(calibrationScreen13(self.frame))
        self.screens[self.SCR_CALIBRATION13].fifthStateReadButton.configure(command= self.combine_funcs(lambda: self.switchScreen(self.SCR_CALIBRATION3, "Calibration"), self.StateTimer))

        #Calibration Screen 12 Initialize and Configuration
        self.SCR_CALIBRATION12 = self.numScreens
        self.numScreens += 1
        self.screens.append(calibrationScreen12(self.frame))
        self.screens[self.SCR_CALIBRATION12].fourthStateReadButton.configure(command= self.combine_funcs(lambda: self.switchScreen(self.SCR_CALIBRATION3, "Calibration"), self.StateTimer))

        #Calibration Screen 11 Initialize and Configuration
        self.SCR_CALIBRATION11 = self.numScreens
        self.numScreens += 1
        self.screens.append(calibrationScreen11(self.frame))
        self.screens[self.SCR_CALIBRATION11].thirdStateReadButton.configure(command= self.combine_funcs(lambda: self.switchScreen(self.SCR_CALIBRATION3, "Calibration"), self.StateTimer))

        #Calibration Screen 10 Initialize and Configuration
        self.SCR_CALIBRATION10 = self.numScreens
        self.numScreens += 1
        self.screens.append(calibrationScreen10(self.frame))

        #Calibration Screen 9 Initialize and Configuration
        self.SCR_CALIBRATION9 = self.numScreens
        self.numScreens += 1
        self.screens.append(calibrationScreen9(self.frame))

        #Calibration Screen 8 Initialize and Configuration
        self.SCR_CALIBRATION8 = self.numScreens
        self.numScreens += 1
        self.screens.append(calibrationScreen8(self.frame))

        #Calibration Screen 7 Initialize and Configuration
        self.SCR_CALIBRATION7 = self.numScreens
        self.numScreens += 1
        self.screens.append(calibrationScreen7(self.frame))
        self.screens[self.SCR_CALIBRATION7].secondStateReadButton.configure(command= self.combine_funcs(lambda: self.switchScreen(self.SCR_CALIBRATION3, "Calibration"), self.StateTimer))

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
        self.screens[self.SCR_CALIBRATION5].firstStateReadButton.configure(command= self.combine_funcs(lambda: self.switchScreen(self.SCR_CALIBRATION3, "Calibration"), self.StateTimer))

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
        self.screens[self.SCR_CALIBRATION2].neutralStateReadButtonFFT.configure(command= self.combine_funcs(lambda: self.switchScreen(self.SCR_CALIBRATION3, "Calibration"), self.domainFFT))
        self.screens[self.SCR_CALIBRATION2].neutralStateReadButtonTime.configure(command= self.combine_funcs(lambda: self.switchScreen(self.SCR_CALIBRATION3, "Calibration"), self.domainTime))
        #self.screens[self.SCR_CALIBRATION2].neutralStateReadButtonFFT.configure(command= self.combine_funcs(lambda: self.switchScreen(self.SCR_CALIBRATION3, "Calibration"), self.testTimer))

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
        self.menuSelect.keyboardButton.configure(command=self.combine_funcs(lambda: self.switchScreen(self.SCR_KEYBOARD, "Keyboard"),lambda: threading.Thread(target=self.keyboardGeneralBrainData).start()), style="unpressed.TButton")

        #Trace calls from drop down menus
        self.header.user.trace("w", self.switchUser)
        self.header.CType.trace("w", self.runNetwork)

        #Popup init
        self.messageWindow = pop.popupWindow(self.master)

        #Initalize mixer for sound notifications
        pygame.mixer.init()

        #Initialize data storage folder
        self.dataFolder()

    '''
    Functions
    '''

    def dataFolder(self):
        script_dir = pathlib.Path(__file__).parent.absolute() #<-- absolute dir the script is in
        script_dir = str(script_dir) + "/UserData"
        if os.path.isdir(script_dir):
            pass
        else:
            os.mkdir(script_dir)

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
        5-10 second neutral intervals
        3 seconds on - 10 times
        3 seconds off - 10 times
    '''

    def serverConnect(self):
        if self.header.CType.get() == "UDP                    ":
            self.socket = self.UDPServerInit()
        elif self.header.CType.get() == "LSL                    ":
            self.inlet = self.lslServer()
        #Close popup
        self.messageWindow.closePopup()
        return

    def generateKNNModel(self):
        script_dir = pathlib.Path(__file__).parent.absolute() #<-- absolute dir the script is in
        script_dir = str(script_dir) + "/UserData"
        if self.FFT == True:
            self.model = KNN(str(script_dir) + "/" + self.header.user.get() + "/DataFFT.csv")
        else:
            self.model = KNN(str(script_dir) + "/" + self.header.user.get() + "/DataTime.csv")
        return

    def generateCNNModel(self):
        script_dir = pathlib.Path(__file__).parent.absolute() #<-- absolute dir the script is in
        script_dir = str(script_dir) + "/UserData"
        if self.FFT == True:
            self.model = CNN(str(script_dir) + "/" + self.header.user.get() + "/DataTime.csv")
        else:
            self.model = CNN(str(script_dir) + "/" + self.header.user.get() + "/DataTime.csv")
        return
    '''
    All of the functions contained below will correspond to the
    accumulation of data from various states
    '''

    '''
    Read FFT data in
    '''

    def readNeutralStateFFT(self):

        script_dir = pathlib.Path(__file__).parent.absolute() #<-- absolute dir the script is in
        script_dir = str(script_dir) + "/UserData"
        fs = 250/2
        localCount = 0
        perception = 0

        if os.path.exists(str(script_dir) + "/" + self.header.user.get() + "/DataFFT.csv") and self.count == 0:
            os.remove(str(script_dir) + "/" + self.header.user.get() + "/DataFFT.csv")
            print("Data has been overridden")

        while self.read == True:
            for i in range(9):
                if i == 8:
                    perception = 0
                    self.channel_data[i] = perception
                else:
                    sample,timestamp = self.inlet.pull_sample()
                    if i not in self.channel_data:
                        PSD = (np.square(sample))/(2*0.9765625)
                        self.channel_data[i] = st.mean(PSD)
            print(self.channel_data)

            if self.count == 0:
                df = pd.DataFrame.from_dict(self.channel_data, orient="index")
                df = df.T
                df.to_csv(str(script_dir) + "/" + self.header.user.get() + "/DataFFT.csv", mode="w", header=self.channelNames)
                self.channel_data = {}
                self.count = self.count + 1
            else:
                df = pd.DataFrame.from_dict(self.channel_data, orient="index")
                df = df.T
                df.to_csv(str(script_dir) + "/" + self.header.user.get() + "/DataFFT.csv", mode="a", header=False)
                self.channel_data = {}
        return

    def readStateFFT(self, perception):
        script_dir = pathlib.Path(__file__).parent.absolute() #<-- absolute dir the script is in
        script_dir = str(script_dir) + "/UserData"
        fs = 250/2
        localCount = 0

        while self.read == True:
            for i in range(9):
                if i == 8:
                    self.channel_data[i] = perception
                else:
                    sample,timestamp = self.inlet.pull_sample()
                    if i not in self.channel_data:
                        #F, PSD = signal.welch(sample, fs, nperseg=len(sample))
                        PSD = (np.square(sample))/(2*0.9765625)
                        self.channel_data[i] = st.mean(PSD)

            print(self.channel_data)
            df = pd.DataFrame.from_dict(self.channel_data, orient="index")
            df = df.T
            df.to_csv(str(script_dir) + "/" + self.header.user.get() + "/DataFFT.csv", mode="a", header=False)
            self.channel_data = {}
        return


    '''
    Read Time Domain Data
    '''

    def readNeutralStateTime(self):

        fs = 250
        localCount = 0
        perception = 0
        scales = np.arange(1,129)
        data = {}
        temp = []


        script_dir = pathlib.Path(__file__).parent.absolute() #<-- absolute dir the script is in
        script_dir = str(script_dir) + "/UserData"

        if os.path.exists(str(script_dir) + "/" + self.header.user.get() + "/DataTime.csv") and self.count == 0:
            os.remove(str(script_dir) + "/" + self.header.user.get() + "/DataTime.csv")
            print("Data has been overridden")

        if os.path.exists(str(script_dir) + "/" + self.header.user.get() + "/DataTimeStep.csv") and self.count == 0:
            os.remove(str(script_dir) + "/" + self.header.user.get() + "/DataTimeStep.csv")
            print("Data has been overridden")

        while self.read == True:
            for i in range(32):
                sample, timestamp = self.inlet.pull_sample()
                print("neutral")
                for value in sample:
                    self.channel_data[localCount] = value
                    localCount = localCount + 1
            self.channel_data[localCount] = perception
            localCount = 0
            if self.count == 0:
                df = pd.DataFrame.from_dict(self.channel_data, orient="index")
                df = df.T
                df.to_csv(str(script_dir) + "/" + self.header.user.get() + "/DataTime.csv", mode="a", header=False)
                self.channel_data = {}
                self.count = self.count + 1
            else:
                df = pd.DataFrame.from_dict(self.channel_data, orient="index")
                df = df.T
                df.to_csv(str(script_dir) + "/" + self.header.user.get() + "/DataTime.csv", mode="a", header=False)
                self.channel_data = {}
        return

    def readStateTime(self, perception):
        fs = 250
        localCount = 0
        scales = np.arange(1,129)
        data = {}
        temp = []
        script_dir = pathlib.Path(__file__).parent.absolute() #<-- absolute dir the script is in
        script_dir = str(script_dir) + "/UserData"

        while self.read == True:
            for i in range(32):
                sample, timestamp = self.inlet.pull_sample()
                print("Active")
                for value in sample:
                    self.channel_data[localCount] = value
                    localCount = localCount + 1

            self.channel_data[localCount] = perception
            localCount = 0
            print(sample)

            df = pd.DataFrame.from_dict(self.channel_data, orient="index")
            df = df.T
            df.to_csv(str(script_dir) + "/" + self.header.user.get() + "/DataTime.csv", mode="a", header=False)
            self.channel_data = {}
        return

    def neutralStateTimer(self):
        self.read = True
        if self.startOnce == True and self.FFT == True:
            #self.inlet = self.lslServer()
            threading.Thread(target=self.readNeutralStateFFT).start()
            self.startOnce = False
        elif self.startOnce == True and self.Time == True:
            #self.inlet = self.lslServer()
            threading.Thread(target=self.readNeutralStateTime).start()
            self.startOnce = False
        if self.screens[self.SCR_CALIBRATION3].counter_1.get() > 0:
            self.screens[self.SCR_CALIBRATION3].progressBar.start()
            temp = self.screens[self.SCR_CALIBRATION3].counter_1.get() - 1
            self.screens[self.SCR_CALIBRATION3].counter_1.set(int(temp))
        else:
            self.read = False
            self.startOnce = True
            self.screens[self.SCR_CALIBRATION3].counter_1.set(2)
            #self.switchScreen(self.SCR_CALIBRATION4, "Calibration") #Redo Button
            self.switchScreen(self.SCR_CALIBRATION5, "Calibration") #Move onto next screen
            return
        self.master.after(1000, self.neutralStateTimer)

    def StateTimer(self):
        self.read = True
        if self.startOnce == True and self.FFT == True:
            #self.inlet = self.lslServer()
            print("Function start")
            threading.Thread(target=self.readStateFFT, args=(self.stateCount,)).start()
            self.startOnce = False
        elif self.startOnce == True and self.Time == True:
            #self.inlet = self.lslServer()
            threading.Thread(target=self.readStateTime, args=(self.stateCount,)).start()
            self.startOnce = False
        if self.screens[self.SCR_CALIBRATION3].counter_1.get() > 0:
            self.screens[self.SCR_CALIBRATION3].progressBar.start()
            temp = self.screens[self.SCR_CALIBRATION3].counter_1.get() - 1
            self.screens[self.SCR_CALIBRATION3].counter_1.set(int(temp))
        else:
            print("StateCount:{}".format(self.stateCount))
            print("Process Count:{}".format(self.processCount))
            self.read = False
            self.startOnce = True
            if self.processCount == 4:
                self.processCount = 0
            else:
                self.processCount += 1
            self.screens[self.SCR_CALIBRATION3].counter_1.set(2)
            if self.loops > self.calCycles and self.Time == True:
                self.switchScreen(self.SCR_CALIBRATION10, "Calibration") #Move onto the next calibration screen for on and off
                threading.Thread(target=self.generateCNNModel).start()
                return
            elif self.loops > self.calCycles and self.FFT == True:
                self.switchScreen(self.SCR_CALIBRATION10, "Calibration") #Move onto the next calibration screen for on and off
                threading.Thread(target=self.generateKNNModel).start()
                return
            elif self.stateCount == 5:
                self.stateCount = 1
                self.switchScreen(self.SCR_CALIBRATION5, "Calibration") #Go back to the other commands and not Neutral
            elif self.processCount == 1:
                self.stateCount += 1
                self.switchScreen(self.SCR_CALIBRATION7, "Calibration") #Go back to the other commands and not Neutral
                return
            elif self.processCount == 2:
                self.stateCount += 1
                self.switchScreen(self.SCR_CALIBRATION11, "Calibration") #Go back to the other commands and not Neutral
                return
            elif self.processCount == 3:
                self.stateCount += 1
                self.switchScreen(self.SCR_CALIBRATION12, "Calibration") #Go back to the other commands and not Neutral
                return
            elif self.processCount == 4:
                self.stateCount += 1
                self.loops += 1
                self.switchScreen(self.SCR_CALIBRATION13, "Calibration") #Go back to the other commands and not Neutral
                return
        self.master.after(1000, self.StateTimer)

    '''
    def firstStateTimer(self):
        self.read = True
        if self.startOnce == True and self.FFT == True:
            self.inlet = self.lslServer()
            t1 = threading.Thread(target=self.readStateFFT(1))
            t1.start()
            self.startOnce = False
        elif self.startOnce == True and self.Time == True:
            self.inlet = self.lslServer()
            t1 = threading.Thread(target=self.readStateTime(1))
            t1.start()
            self.startOnce = False
        if self.screens[self.SCR_CALIBRATION3].counter_1.get() > 0:
            self.screens[self.SCR_CALIBRATION3].progressBar.start()
            temp = self.screens[self.SCR_CALIBRATION3].counter_1.get() - 1
            self.screens[self.SCR_CALIBRATION3].counter_1.set(int(temp))
        else:
            t1.join()
            self.read = False
            self.startOnce = True
            self.screens[self.SCR_CALIBRATION3].counter_1.set(2)
            #self.switchScreen(self.SCR_CALIBRATION6, "Calibration") #Redo Button
            self.switchScreen(self.SCR_CALIBRATION7, "Calibration") #Move onto next screen
            return
        self.master.after(1000, self.firstStateTimer)

    def secondStateTimer(self):
        self.read = True
        if self.startOnce == True and self.FFT == True:
            self.inlet = self.lslServer()
            t2 = threading.Thread(target=self.readStateFFT(2))
            t2.start()
            self.startOnce = False
        elif self.startOnce == True and self.Time == True:
            self.inlet = self.lslServer()
            t2 = threading.Thread(target=self.readStateTime(2))
            t2.start()
            self.startOnce = False
        if self.screens[self.SCR_CALIBRATION3].counter_1.get() > 0:
            self.screens[self.SCR_CALIBRATION3].progressBar.start()
            temp = self.screens[self.SCR_CALIBRATION3].counter_1.get() - 1
            self.screens[self.SCR_CALIBRATION3].counter_1.set(int(temp))
        else:
            t2.join()
            self.read = False
            self.startOnce = True
            self.screens[self.SCR_CALIBRATION3].counter_1.set(2)
            self.switchScreen(self.SCR_CALIBRATION11, "Calibration") #Move onto the next calibration screen for on and off
            return
        self.master.after(1000, self.secondStateTimer)

    def thirdStateTimer(self):
        self.read = True
        if self.startOnce == True and self.FFT == True:
            self.inlet = self.lslServer()
            threading.Thread(target=self.readStateFFT(3)).start()
            self.startOnce = False
        elif self.startOnce == True and self.Time == True:
            self.inlet = self.lslServer()
            threading.Thread(target=self.readStateTime(3)).start()
            self.startOnce = False
        if self.screens[self.SCR_CALIBRATION3].counter_1.get() > 0:
            self.screens[self.SCR_CALIBRATION3].progressBar.start()
            temp = self.screens[self.SCR_CALIBRATION3].counter_1.get() - 1
            self.screens[self.SCR_CALIBRATION3].counter_1.set(int(temp))
        else:
            self.read = False
            self.startOnce = True
            self.screens[self.SCR_CALIBRATION3].counter_1.set(2)
            self.switchScreen(self.SCR_CALIBRATION12, "Calibration") #Move onto the next calibration screen for on and off
            return
        self.master.after(1000, self.secondStateTimer)

    def fourthStateTimer(self):
        self.read = True
        if self.startOnce == True and self.FFT == True:
            self.inlet = self.lslServer()
            threading.Thread(target=self.readStateFFT(4)).start()
            self.startOnce = False
        elif self.startOnce == True and self.Time == True:
            self.inlet = self.lslServer()
            threading.Thread(target=self.readStateTime(4)).start()
            self.startOnce = False
        if self.screens[self.SCR_CALIBRATION3].counter_1.get() > 0:
            self.screens[self.SCR_CALIBRATION3].progressBar.start()
            temp = self.screens[self.SCR_CALIBRATION3].counter_1.get() - 1
            self.screens[self.SCR_CALIBRATION3].counter_1.set(int(temp))
        else:
            self.read = False
            self.startOnce = True
            self.screens[self.SCR_CALIBRATION3].counter_1.set(2)
            self.switchScreen(self.SCR_CALIBRATION13, "Calibration") #Move onto the next calibration screen for on and off
            return
        self.master.after(1000, self.secondStateTimer)

    def fifthStateTimer(self):
        self.read = True
        if self.startOnce == True and self.FFT == True:
            self.inlet = self.lslServer()
            threading.Thread(target=self.readStateFFT(5)).start()
            self.startOnce = False
        elif self.startOnce == True and self.Time == True:
            self.inlet = self.lslServer()
            threading.Thread(target=self.readStateTime(5)).start()
            self.startOnce = False
        if self.screens[self.SCR_CALIBRATION3].counter_1.get() > 0:
            self.screens[self.SCR_CALIBRATION3].progressBar.start()
            temp = self.screens[self.SCR_CALIBRATION3].counter_1.get() - 1
            self.screens[self.SCR_CALIBRATION3].counter_1.set(int(temp))
        else:
            self.read = False
            self.startOnce = True
            self.screens[self.SCR_CALIBRATION3].counter_1.set(2)
            self.loops = self.loops + 1
            if self.loops > self.calCycles and self.Time == True:
                self.switchScreen(self.SCR_CALIBRATION10, "Calibration") #Move onto the next calibration screen for on and off
                threading.Thread(target=self.generateCNNModel).start()
                return
            elif self.loops > self.calCycles and self.FFT == True:
                self.switchScreen(self.SCR_CALIBRATION10, "Calibration") #Move onto the next calibration screen for on and off
                threading.Thread(target=self.generateKNNModel).start()
                return
            else:
                self.switchScreen(self.SCR_CALIBRATION5, "Calibration") #Go back to the other commands and not Neutral
                return
        self.master.after(1000, self.secondStateTimer)
        '''
    '''
    End of state accumulation functions
    '''

    '''
    State functions
    '''

    def domainFFT(self):
        self.FFT = True
        self.Time = False
        self.neutralStateTimer()
        return

    def domainTime(self):
        self.FFT = False
        self.Time = True
        self.neutralStateTimer()
        return

    def domainTimeInit(self):
        self.FFT = False
        self.Time = True

    def domainFFTInit(self):
        self.FFT = True
        self.Time = False

    '''

    Start of running tests on brain wave data and ml model

    '''

    def keyboardGeneralBrainData(self):
        while self.screens[self.SCR_KEYBOARD].read == True:
            '''
            Output functionality with the use of FFT calibration
            '''
            if self.FFT == True:
                fs = 250/2
                countUp = 0
                countDown = 0
                countLeft = 0
                countRight = 0
                countSelect = 0
                while self.model != None and self.screens[self.SCR_KEYBOARD].read == True:
                    self.inlet = self.lslServer()
                    for i in range(8):
                        sample,timestamp = self.inlet.pull_sample()
                        if i not in self.channel_data:
                            PSD = (np.square(sample))/(2*0.9765625)
                            self.dataInput.append(st.mean(PSD))
                    temp = [self.dataInput]

                    modelOutput = self.model.classifier.predict(temp)
                    self.dataInput = []

                    if modelOutput == 1:
                        countUp+= 1
                        if countUp == 2:
                            print("Up")
                            self.screens[self.SCR_KEYBOARD].upKey()
                            countUp = 0
                            countDown = 0
                            countLeft = 0
                            countRight = 0
                            countSelect = 0
                    elif modelOutput == 2:
                        countDown += 1
                        if countDown == 2:
                            print("Down")
                            self.screens[self.SCR_KEYBOARD].downKey()
                            countUp = 0
                            countDown = 0
                            countLeft = 0
                            countRight = 0
                            countSelect = 0
                    elif modelOutput == 3:
                        countLeft += 1
                        if countLeft == 2:
                            print("Left")
                            self.screens[self.SCR_KEYBOARD].leftKey()
                            ccountUp = 0
                            countDown = 0
                            countLeft = 0
                            countRight = 0
                            countSelect = 0
                    elif modelOutput == 4:
                        countRight += 1
                        if countRight == 2:
                            print("Right")
                            self.screens[self.SCR_KEYBOARD].rightKey()
                            countUp = 0
                            countDown = 0
                            countLeft = 0
                            countRight = 0
                            countSelect = 0
                    elif modelOutput == 5:
                        countSelect += 1
                        if countSelect == 2:
                            print("Select")
                            self.screens[self.SCR_KEYBOARD].brainSelect()
                            countUp = 0
                            countDown = 0
                            countLeft = 0
                            countRight = 0
                            countSelect = 0
                    elif modelOutput == 0:
                        print("Neutral")
                        countUp = 0
                        countDown = 0
                        countLeft = 0
                        countRight = 0
                        countSelect = 0
        else:
            return





    def readGeneralBrainData(self):
        #self.switchScreen(self.SCR_CALIBRATION10, "Calibration") #Switch to the draw screen
        '''
        Output functionality with the use of FFT calibration
        '''
        if self.FFT == True:
            fs = 250/2
            countOn = 0
            countOff = 0
            while self.model != None:
                self.inlet = self.lslServer()
                for i in range(8):
                    sample,timestamp = self.inlet.pull_sample()
                    if i not in self.channel_data:
                        PSD = (np.square(sample))/(2*0.9765625)
                        self.dataInput.append(st.mean(PSD))

                temp = [self.dataInput]

                modelOutput = self.model.classifier.predict(temp)
                self.dataInput = []

                if modelOutput == 1:
                    #print("On")

                    countOn += 1
                    if countOn == 2:
                        print("On")
                        countOn = 0
                        countOff = 0

                elif modelOutput == 2:
                    #print("Off")

                    countOff += 1
                    if countOff == 2:
                        print("Off")
                        countOff = 0
                        countOn = 0

                elif modelOutput == 0:
                    print("Neutral")
                    countOn = 0
                    countOff = 0

        '''
        Output functionality with the use of Time calibration
        '''
        if self.Time == True:
            class_names = ['Neutral','On','Off']
            fs = 32
            scales = np.arange(1,129)
            count = 0
            self.inlet = self.lslServer()
            numSamples = 256
            while self.model != None:
                self.inlet = self.lslServer()
                temp = np.ndarray((1,fs,numSamples))
                for j in range(32):
                    count = 0
                    for i in range(32):
                        sample, timestamp = self.inlet.pull_sample()
                        for val in sample:
                            temp[:,j,count] = val
                            cout = count + 1

                data = temp.reshape(1, fs, numSamples)
                out = class_names[np.argmax(self.model.classifier.predict(temp))]

                if out == "On":
                    print("ON")
                elif out == "Off":
                    print("OFF")
                elif out == "Neutral":
                    print("NEUTRAL")

                count = count + 1



    def runNetwork(self, *args):
        self.messageWindow.popupConnection()
        self.master.update() #Popup needs to be forced refresh to display
        self.serverConnect()

    def infoLogo(self):
        self.master.focus()
        self.messageWindow.popupInfo()
        self.master.update() #Popup needs to be forced refresh to display


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
        return

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
