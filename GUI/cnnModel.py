import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import pywt
import os
from PIL import Image
import tensorflow.keras as tf
from tensorflow.keras.layers import Dense, Flatten, Conv2D, Conv1D, MaxPool2D, MaxPool1D, Activation, Dropout, BatchNormalization
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
        self.numChannels = 8*8
        self.numSamples = 8
        self.waveletSamples = 128
        self.nDataSetLength = len(self.dataset)
        self.localCount = 0
        self.dX = {}
        self.scales = np.arange(1,17)
        self.scales_len = np.max(self.scales)
        self.fs = 32

        '''

        #The input shape just needs to be changed back to (8,1,1) and therefore you can work with the typical input data

        '''
        self.X = self.dataset.iloc[:, 0:self.numChannels].values#.reshape(self.dataset.shape[0], 8, 1, 1)
        # self.x_data = np.ndarray((self.nDataSetLength,self.scales_len,self.fs,self.numChannels)) #for wavelet CNN
        self.x_data = np.ndarray((self.nDataSetLength,self.fs,self.numChannels)) #for time CNN
        self.Y = self.dataset.iloc[:, self.numChannels].values
        self.zero = []

        #windowing the time data
        for i in range(self.nDataSetLength - self.fs):
            if all(x==self.Y[i] for x in self.Y[i:(i+self.fs)]):
                for j in range(self.numChannels):
                    self.x_data[i,:,j] = self.X[i:(i+self.fs),j]
            else:
                self.zero.append(i)

        # #remove all x_data wavelets that equal zero & corresponding y data
        self.x_data = np.delete(self.x_data, self.zero, axis=0)
        self.Y = np.delete(self.Y, self.zero, axis=0)
        print(self.x_data.shape)

        self.dY = tf.utils.to_categorical(self.Y, num_classes=3)

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.x_data, self.dY, random_state=0, test_size=0.2)

        # self.shape = (self.scales_len, self.fs, self.numChannels) #for wavelet
        self.shape = (self.fs,self.numChannels) #for time

        #create self.classifier, change between Conv/MaxPool 1 and 2D for time and wavelet respectively
        self.classifier = Sequential()
        self.classifier.add(Conv1D(64, 3, data_format='channels_last', activation='relu', input_shape=self.shape, padding='same'))
        self.classifier.add(MaxPool1D(pool_size=2, strides=2,padding='same'))
        self.classifier.add(BatchNormalization())
        self.classifier.add(Dropout(0.2))

        self.classifier.add(Conv1D(64, 3, data_format='channels_last', activation='relu', input_shape=self.shape, padding='same'))
        self.classifier.add(MaxPool1D(pool_size=2, strides=2,padding='same'))
        self.classifier.add(BatchNormalization())
        self.classifier.add(Dropout(0.2))

        self.classifier.add(Conv1D(64, 3, data_format='channels_last', activation='relu', input_shape=self.shape, padding='same'))
        self.classifier.add(MaxPool1D(pool_size=2, strides=2,padding='same'))
        self.classifier.add(BatchNormalization())

        self.classifier.add(Flatten())
        self.classifier.add(Dense(64))
        self.classifier.add(Dropout(0.5))
        self.classifier.add(Dense(3))
        self.classifier.add(Activation('softmax'))

        # #compile model using accuracy to measure model performance
        self.classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        # #train the model
        self.classifier.fit(self.X_train, self.y_train, validation_data=(self.X_test, self.y_test), epochs=60)

        test_error, test_accuracy = self.classifier.evaluate(self.X_test, self.y_test, verbose=1)
        print(test_accuracy)
        print(self.classifier.summary())
