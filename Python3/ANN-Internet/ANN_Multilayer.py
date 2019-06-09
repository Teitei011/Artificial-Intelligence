import numpy as np


class Neural_Network(object):
    def __init__(self, inputSize, outputSize, neurons_in_hidden, number_of_layers):
        #parameters
        self.inputSize = inputSize
        self.outputSize = outputSize
        self.hiddenSize = neurons_in_hidden
        self._number_of_layers = number_of_layers # Cause have the input and hidden

                    # Creating the layer

        self.layers = []

        # Creating the first hidden layer
        self.layers.append(np.random.randn(self.inputSize, self.hiddenSize))

        # For the hidden layers in the middle
        for i in range(self._number_of_layers):
            self.layers.append(np.random.randn(self.hiddenSize, self.hiddenSize))

        # For the last hidden layer
        self.layers.append(np.random.randn(self.hiddenSize, self.outputSize))

    def show(self):
        print("\n----------------------------------\n")
        for i in range(self._number_of_layers + 2):
            temp  = "Layer(" + str(i) + ") --> " + str(self.layers[i]) + "\n\n"
            print(temp)
        print("\n----------------------------------\n")

    def save(self):
        pass

    def load(self):
        pass

    def feedforward(self, X):
        #forward propagation through our network
        self.temp = []

        self.z = np.dot(X, self.layers[0]) # Input Layer
        self.z2 = self.sigmoid(self.z)
        self.temp.append(self.z2)

        for i in range(self._number_of_layers + 1): # The output layer will be processed here, therefore need a +1
            self.z = np.dot(self.temp[i], self.layers[i + 1])
            self.z2 = self.sigmoid(self.z)
            self.temp.append(self.z2)

        return self.z2

    def sigmoid(self, a):
        # activation function
        return 1 / (1 + np.exp(-a))

    def sigmoidPrime(self, a):
        #derivative of sigmoid
        return a * (1 - a)

    def loss_function(self, X, Y):
        print ("Loss: " + str(np.mean(np.square(Y - X)))) # mean sum squared loss

    def backpropagation(self, X, y, o):
        # backward propgate through the network
        self.o_error = y - o # error in output
        self.o_delta = self.o_error*self.sigmoidPrime(o) # applying derivative of sigmoid to error

        self.z2_error = self.o_delta.dot(self.W2.T) # z2 error: how much our hidden layer weights contributed to output error
        self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2) # applying derivative of sigmoid to z2 error

        self.W1 += X.T.dot(self.z2_delta) # adjusting first set (input --> hidden) weights
        self.W2 += self.z2.T.dot(self.o_delta) # adjusting second set (hidden --> output) weights

    def train (self, X, y):
        output = self.feedforward(X)
        self.backpropagation(X, y, output)
        loss_function(output, Y)
