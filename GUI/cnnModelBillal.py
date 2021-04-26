import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import pywt
import os
from PIL import Image
import tensorflow.keras as tf
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPool2D, Activation, Dropout, BatchNormalization
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import History
history = History()
import sys
import pywt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score



'''
PATH="~/.pyenv/versions/3.8.0/bin:${PATH}"
eval "$(pyenv init -)"
'''

class CNN:

    def __init__(self, data):

        print("Generating Model")
        self.dataset = pd.read_csv(data)
        self.dataset = self.dataset.drop(self.dataset.columns[[0]], axis=1)
        self.numChannels = 8
        #self.numSamples = 8
        self.numSamples = 8*8
        self.waveletSamples = 128
        self.nDataSetLength = len(self.dataset)
        self.dX = {}
        self.localCount = 0
        self.scales = np.arange(1,129)

        '''
        self.X = self.dataset.iloc[:, 0:self.numSamples].values.reshape(self.dataset.shape[0], self.numSamples, 1, 1)
        self.Y = self.dataset.iloc[:, self.numSamples].values


        self.dY = tf.utils.to_categorical(self.Y, num_classes=3)

        self.dX = np.array(self.X)
        self.dY = np.array(self.dY)

        #The input shape just needs to be changed back to (8,1,1) and therefore you can work with the typical input data

        '''


        self.X = self.dataset.iloc[:, 0:self.numSamples].values#.reshape(self.dataset.shape[0], 8, 1, 1)
        self.Y = self.dataset.iloc[:, self.numSamples].values

        #Below for Wavelet
        print("Looping through your bigass dataset")
        for i, array in enumerate(self.X):
            n = 1
            self.temp = {new_list: [] for new_list in range(self.numSamples//self.numChannels)}
            for j, value in enumerate(array, start=1):
                if j%self.numChannels != 0:
                    self.temp[j-n].append(value)
                else:
                    self.temp[j-n].append(value)
                    n = n + self.numChannels
            for key, value in self.temp.items():
                coeffs,freq = pywt.cwt(value,self.scales,'morl', 1/250)
                self.dX[self.localCount] = coeffs
                self.localCount = self.localCount + 1


        self.dX = np.array(list(self.dX.values()))
        self.dX = self.dX.reshape(self.dataset.shape[0], 128, self.numSamples)


        self.dY = tf.utils.to_categorical(self.Y, num_classes=3)

        self.ddX = np.array(self.dX)
        self.dY = np.array(self.dY)




        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.ddX, self.dY, random_state=0, test_size=0.2)


        #create self.classifier

        self.classifier = Sequential()
        self.classifier.add(Conv1D(64, 3, data_format='channels_last', activation='relu', input_shape=(128,self.numSamples), padding='same'))
        self.classifier.add(MaxPool1D(pool_size=2, strides=2,padding='same'))
        self.classifier.add(BatchNormalization())
        self.classifier.add(Dropout(0.2))

        self.classifier.add(Conv1D(64, 3, data_format='channels_last', activation='relu', input_shape=(128,self.numSamples), padding='same'))
        self.classifier.add(MaxPool1D(pool_size=2, strides=2,padding='same'))
        self.classifier.add(BatchNormalization())
        self.classifier.add(Dropout(0.2))

        self.classifier.add(Conv1D(64, 3, data_format='channels_last', activation='relu', input_shape=(128,self.numSamples), padding='same'))
        self.classifier.add(MaxPool1D(pool_size=2, strides=2,padding='same'))
        self.classifier.add(BatchNormalization())

        self.classifier.add(Flatten())
        self.classifier.add(Dense(64))
        self.classifier.add(Dropout(0.5))
        self.classifier.add(Dense(3))
        self.classifier.add(Activation('softmax'))


        self.classifier.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        self.classifier.fit(self.X_train, self.y_train, batch_size=16, epochs=60, verbose=1, validation_data=(self.X_test, self.y_test), callbacks=[history])

        test_error, test_accuracy = self.classifier.evaluate(self.X_test, self.y_test, verbose=1)
        print(test_accuracy)
        print(self.classifier.summary())
