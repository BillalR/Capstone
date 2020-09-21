import numpy as np
import pandas as pd

class Neuron:
    #Constructor does nothing
    def __init__(self):
        np.random.seed(1)

        self.synaptic_weights = 2 * np.random.random((3,1)) - 1


    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

    #Derivative is in the form simplified to (sigmoid)(1-sigmoid)
    def sigmoidDer(self,x):
        return x*(1-x)

    def train(self, training_inputs, training_outputs, trianing_iterations):

        for iteration in range(training_iterations):
            #error is used for back propogation
            output = self.think(training_inputs)
            error = training_outputs - output

            adjustments = np.dot(training_inputs.T, error*self.sigmoidDer(output))
            self.synaptic_weights += adjustments

    def think(self,inputs):

        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))

        return output

if __name__ == "__main__":

    neural_network = Neuron()

    print("Random synaptic weights: ")
    print(neural_network.synaptic_weights)

    #training_inputs = np.array(data.values)
    training_inputs = np.array([[0,0,1],
                                [1,1,1],
                                [1,0,1],
                                [0,1,1]])

    #training_outputs = np.random.randint(0,3,(len(training_inputs),1))
    training_outputs = np.array([[0,1,1,0]]).T

    neural_network.train(training_inputs, training_outputs, 10000)

    print("Synaptic weights after training: ")
    print(neural_network.synaptic_weights)
