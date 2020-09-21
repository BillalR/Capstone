#This program will be prototyping data handling RAW EEG datasets
#This will be using the perceptron NN aglorithm -- No Hidden layers, typically one neuron and multiple synapes
import numpy as np
import pandas as pd
import random
from Data import *
from Network import *

#Main definition program
if __name__ == '__main__':

    #Identify the column sensor names
    S1 = 'Fp1'
    S2 = 'Fp2'
    S3 = 'F7'
    S4 = 'F3'
    S5 = 'Fz'
    S6 = 'F4'

    #dh refers to handling the data in question
    #Data will be used to utilize the data
    dh = Data('data_series.csv')
    data = dh.readFile()

    #Define Neural Network
    Neuron = Neuron()

    #training_inputs = np.array(data.values)
    training_inputs = np.array([[0,0,1],
                                [1,1,1],
                                [1,0,1],
                                [0,1,1]])

    #training_outputs = np.random.randint(0,3,(len(training_inputs),1))
    training_outputs = np.array([[0,1,1,0]]).T

    #Assigning random values to weights
    np.random.seed(1)

    #We are going to create a inputs x outputs -- 6 inputs and 1 outputs -- 6 x 1
    #Values will range between -1 and 1
    synaptic_weights = 2 * np.random.random((3,1)) - 1

    print('Random starting synaptic weights: {}'.format(synaptic_weights))

    #Main loop
    for iteration in range(20000):
        input_layer = training_inputs
        #Since the dot product gives us the similarity between two vectors, we are comparing training inputs to the weights
        #and identifying whether they work or not
        outputs = Neuron.sigmoid(np.dot(input_layer,synaptic_weights))

        error = training_outputs - outputs

        adjustments = error * Neuron.sigmoidDer(outputs)

        synaptic_weights += np.dot(input_layer.T,adjustments)

    print('Synaptic Weights After Training: {}'.format(synaptic_weights))

    print('Outputs after training: {}'.format(outputs))
