import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import pywt 
import os 
from PIL import Image
import tensorflow.keras as tf
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPool2D, Activation
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import History
history = History()
import sys

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

class CNN:

    def __init__(self, data):

        print("Generating Model")
        self.dataset = pd.read_csv(data + "Data.csv")
        self.dataset = self.dataset.drop(self.dataset.columns[[0]], axis=1)
        self.numChannels = 8
        self.nDataSetLength = len(self.dataset)
        #print(self.dataset)

        self.X = np.array(self.dataset.iloc[:, 0:self.numChannels].values)
        self.Y = np.array(self.dataset.iloc[:, self.numChannels].values)

        neutrals = []
        ons = []
        offs = []
        neutral_state = np.empty(8)
        on_state = np.empty(8)
        off_state = np.empty(8)
        count_neutral = 0
        count_on = 0
        count_off = 0
        sample_neutral = 0
        sample_on = 0
        sample_off = 0
        fs = 250/2
        scales = np.arange(1,129)
        scale_len = np.max(scales)

        #split time data into arrays of arrays of perception data
        for i in range(len(self.Y)):
            if self.Y[i] == 0: #if overall index is more than one away from previous, make new array
                if (i - count_neutral) > 1 or sample_neutral == fs:
                    if neutral_state.shape[0] > fs:
                        neutrals.append(neutral_state[1:,:]) #add array to list except first row
                    neutral_state = np.empty(8) #clear array
                    sample_neutral = 0
                neutral_state = np.vstack((neutral_state,self.X[i,:])) #add to neutral_state[i]
                count_neutral = i #set count to idx
                sample_neutral += 1
            if self.Y[i] == 1:
                if len(on_state) == 8:
                    count_on = i
                if (i - count_on) > 1 or sample_on == fs:
                    if on_state.shape[0] > fs:
                        ons.append(on_state[1:,:])
                    on_state = np.empty(8)
                    sample_on = 0
                on_state = np.vstack((on_state,self.X[i,:]))
                count_on = i
                sample_on += 1
            if self.Y[i] == 2:
                if len(off_state) == 8:
                    count_off = i
                if (i - count_off) > 1 or sample_off == fs:
                    if off_state.shape[0] > fs:
                        offs.append(off_state[1:,:])
                    off_state = np.empty(8)
                    sample_off = 0
                off_state = np.vstack((off_state,self.X[i,:]))
                count_off = i
                sample_off += 1

        #add data in arrays to main lists
        if neutral_state.shape[0] > fs:
            neutrals.append(neutral_state[1:,:])
        if on_state.shape[0] > fs:
            ons.append(on_state[1:,:])
        if off_state.shape[0] > fs:
            offs.append(off_state[1:,:])

        x_data = np.ndarray((len(neutrals)+len(ons)+len(offs),scale_len,int(fs),8))
        y_data = []
        count = 0
        train_test = 1
        for inst in neutrals:
            for i in range(self.numChannels):
                coeffs,freq = pywt.cwt(inst[:,i], scales, 'morl', 1/fs)
                coeff_norm = 255*(coeffs - np.min(coeffs))/np.ptp(coeffs)  
                x_data[count,:,:,i] = coeffs
                im = Image.fromarray(coeff_norm)
                im = im.convert('RGB')
                filename = "0_%s_%s.jpg" %(str(count), str(i))
                im.save(data + filename)
            count += 1
            y_data.append(0)    


        for inst in ons:
            for i in range(self.numChannels):
                coeffs,freq = pywt.cwt(inst[:,i], scales, 'morl', 1/fs)
                coeff_norm = 255*(coeffs - np.min(coeffs))/np.ptp(coeffs)
                x_data[count,:,:,i] = coeffs
                im = Image.fromarray(coeff_norm)
                im = im.convert('RGB')
                filename = "1_%s_%s.jpg" %(str(count), str(i))
                im.save(data + filename)
            count += 1
            y_data.append(1)  

        for inst in offs:
            for i in range(self.numChannels):
                coeffs,freq = pywt.cwt(inst[:,i], scales, 'morl', 1/fs)
                coeff_norm = 255*(coeffs - np.min(coeffs))/np.ptp(coeffs)
                x_data[count,:,:,i] = coeffs
                im = Image.fromarray(coeff_norm)
                im = im.convert('RGB')
                filename = "2_%s_%s.jpg" %(str(count), str(i))
                im.save(data + filename)
            count += 1
            y_data.append(2)  

        y_data = np.array(y_data).T
        print(x_data.shape)
        print(y_data.shape)
        x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, random_state=0, test_size=0.2)

        y_train = list(map(lambda x: int(x) - 1, y_train))
        y_test = list(map(lambda x: int(x) - 1, y_test))

        x_train = x_train.astype('float32')
        x_test = x_test.astype('float32')

        img_x = scale_len
        img_y = int(fs)
        img_z = self.numChannels
        input_shape = (img_x, img_y, img_z)

        num_classes = 3
        batch_size = 16
        epochs = 20

        y_train = tf.utils.to_categorical(y_train, num_classes)
        y_test = tf.utils.to_categorical(y_test, num_classes)

        model = Sequential()
        #~70% w/ garbage data, 20 epochs using coeff_norm, less w/ coeffs
        # model.add(Conv2D(32, kernel_size=(5, 5), strides=(1, 1), activation='relu', input_shape=input_shape))
        # model.add(MaxPool2D(pool_size=(2, 2), strides=(2, 2)))
        # model.add(Conv2D(64, (5, 5), activation='relu'))
        # model.add(MaxPool2D(pool_size=(2, 2)))
        # model.add(Flatten())
        # model.add(Dense(1000, activation='relu'))
        # model.add(Dense(num_classes, activation='softmax'))

        #peak 75% w/ garbage data, 20 epochs using coeff_norm, peak 81.25% w/ coeffs <-- using fs = 125, scales = 128
        #peak 100% w/ garbage data, 20 epochs using coeffs <-- using fs = 250, scales = 256
        model.add(Conv2D(32, 5, activation = 'relu', padding = 'same', input_shape = input_shape))
        model.add(MaxPool2D())
        model.add(Conv2D(64, 5, activation = 'relu', padding = 'same', kernel_initializer = "he_normal"))
        model.add(MaxPool2D())  
        model.add(Flatten())
        model.add(Dense(128, activation = 'relu', kernel_initializer = "he_normal"))
        model.add(Dense(54, activation = 'relu', kernel_initializer = "he_normal"))
        model.add(Dense(num_classes, activation = 'softmax'))
    
        model.compile(loss=tf.losses.categorical_crossentropy, optimizer=tf.optimizers.Adam(), metrics=['accuracy'])
        model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_data=(x_test, y_test), callbacks=[history])

        train_score = model.evaluate(x_train, y_train, verbose = 0)
        print('Train loss: {}, Train Acc: {}'.format(train_score[0], train_score[1]))
        test_score = model.evaluate(x_test, y_test, verbose = 0)
        print('Test loss: {}, Test Acc: {}'.format(test_score[0], test_score[1]))

    #in above loops (make function) pushback train/test arrays for x & y

    #Don't have to put in folders? Could just run cnn directly???
    #set folders for train/test data (sets of 8)
    #pull from folders, stack channels into 3D array, normalize to [0-1] (depending on CNN specs)
    #work on getting real-time wavelet data, comparison to model (buffer 125 samples, calculate wavelet, stack channels, check, repeat)  
