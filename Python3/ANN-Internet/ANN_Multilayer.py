import numpy as np


class Neural_Network(object):
    def __init__(self, _inputSize, _outputSize, neurons_in_hidden, number_of_layers, training_rate):
        #parameters
        self._inputSize = _inputSize
        self._outputSize = _outputSize
        self._hiddenSize = neurons_in_hidden
        self._number_of_layers = number_of_layers
        self._training_rate = training_rate

                    # Creating the layer

        self.layers = []

        # Creating the first hidden layer
        self.layers.append(np.random.randn(self._inputSize, self._hiddenSize))

        # For the hidden layers in the middle
        for i in range(self._number_of_layers):
            self.layers.append(np.random.randn(self._hiddenSize, self._hiddenSize))

        # For the last hidden layer
        self.layers.append(np.random.randn(self._hiddenSize, self._outputSize))

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


    def sigmoid(self, a):
        # activation function
        return 1 / (1 + np.exp(-a))

    def sigmoidPrime(self, a):
        #derivative of sigmoid
        return a * (1 - a)

    def feedforward(self, X):
        #forward propagation through our network
        self.forward_propagation = []

        self.z = np.dot(X, self.layers[0]) # Input Layer
        self.z2 = self.sigmoid(self.z)
        self.forward_propagation.append(self.z2)

        for i in range(self._number_of_layers + 1): # The output layer will be processed here, therefore need a +1
            self.z = np.dot(self.forward_propagation[i], self.layers[i + 1])
            self.z2 = self.sigmoid(self.z)
            self.forward_propagation.append(self.z2)

        return self.z2

    def backpropagation(self, X, y, o):

        self.error_array = []

        self.o_error = y - o # error in output
        self.o_delta = self.o_error * self.sigmoidPrime(o) # applying derivative of sigmoid to error
        self.layers[0] += X.T.dot(self.o_delta)


        for i in range(self._number_of_layers + 1):
            # z error: how much our hidden layer weights contributed to output error
            self.z_error = self.error_array[i].dot(self.layers[i + 1].T)

             # applying derivative of sigmoid to z2 error
            self.error_array.append(self.z_error * self.sigmoidPrime(self.forward_propagation[i + 1]))

            self.layers[i + 1] += self.error_in_the_layers.T.dot(self.error_array[i])

    def loss_function(self, X, Y):
        print ("Loss: " + str(np.mean(np.square(Y - X)))) # mean sum squared loss


    def train (self, X, Y):
        output = self.feedforward(X)
        self.backpropagation(X, Y, output)
        loss_function(output, Y)
