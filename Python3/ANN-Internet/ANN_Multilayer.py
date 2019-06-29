import numpy as np
from time import time

class Neural_Network(object):
    def __init__(self, inputSize, outputSize, neurons_in_hidden, number_of_layers, training_rate):
        #parameters
        self._inputSize = inputSize
        self._outputSize = outputSize
        self._hiddenSize = neurons_in_hidden
        self._number_of_layers = number_of_layers
        self._training_rate = training_rate

                    # Creating the layer

        self.layers = []
        # self.bias = []

        # Creating the first hidden layer
        self.layers.append(np.random.randn( self._inputSize, self._hiddenSize))
        # self.bias.append(np.random.randn(self._hiddenSize, self._hiddenSize))

        # self.layers.append(np.random.randn(self._hiddenSize, self._inputSize))


        # For the hidden layers in the middle
        for i in range(self._number_of_layers):
            self.layers.append(np.random.randn(self._hiddenSize, self._hiddenSize))
            # self.bias.append(np.random.randn(self._hiddenSize, self._hiddenSize))

        # For the last hidden layer
        self.layers.append(np.random.randn(self._hiddenSize, self._outputSize))
        # self.bias.append(np.random.randn(self._hiddenSize, self._outputSize))

        for i in range(self._number_of_layers + 2):
            print(self.layers[i].shape)

    def show(self):
        print("\n----------------------------------\n")
        for i in range(self._number_of_layers + 2):
            temp  = "Layer(" + str(i) + ") --> " + str(self.layers[i]) + "\n\n"
            print(temp)
        print("\n----------------------------------\n")

    def save(self):
            print("Creating directory...")
            try:
                path = os.mkdir("Weights")
            except:
                print("Directory already created...")

            os.chdir("Weights/")

            # Creating file to know how many arrays it has
            data = open("Number_of_layers.txt", "w")
            data.write(str(self._number_of_layers + 2))
            data.close()

            for i in range(self._number_of_layers + 2):
                np.save("weights[" + str(i) + "].npy", self.layers[i])

            os.chdir("..")

    def load(self):
        try:
            os.chdir("Weights/")
        except:
            print("No data has been saved")
            return

        data = open("Number_of_layers.txt", "r")
        number_of_layers = data.readline()
        data.close()

        # Loading all the weights
        for i in range(int(number_of_layers)):
            self.layers[i] = np.load("weights[" + str(i) + "].npy") # TODO: See why this isn´t working


    def sigmoid(self, a):
        # activation function
        return 1 / (1 + np.exp(-a))

    def sigmoidPrime(self, a):
        #derivative of sigmoid
        return a * (1 - a)

    def query(self, X):
        #forward propagation through our network
        self.forward_propagation = []
        self.z = np.dot(X, self.layers[0]) #+ self.bias[0] # Input Layer
        self.z2 = self.sigmoid(self.z)
        self.forward_propagation.append(self.z2)

        for i in range(self._number_of_layers + 1): # The output layer will be processed here, therefore need a +1
            self.z = np.dot(self.forward_propagation[i], self.layers[i + 1])# + self.bias[i + 1]
            self.z2 = self.sigmoid(self.z)
            self.forward_propagation.append(self.z2)

        return self.z2

    def backpropagation(self, X, y):
        print("Backpropagation")
    #forward propagation through our network
        self.forward_propagation = []
        self.z2 = []
        self.z = np.dot(X, self.layers[0])# + self.bias[0] # Input Layer
        self.z2 = self.sigmoid(self.z)

        self.forward_propagation.append(self.z2)

        for i in range(self._number_of_layers + 1): # The output layer will be processed here, therefore need a +1
            self.z = np.dot(self.forward_propagation[i], self.layers[i + 1])# + self.bias[i + 1]
            self.z2 = self.sigmoid(self.z)
            self.forward_propagation.append(self.z2)


            #  backpropagation itself

        self.o_error = y - self.forward_propagation[-1] # error in output
        print("self.o_error")
        print(self.o_error.shape)

        self.o_delta = self.o_error * self.sigmoidPrime(self.forward_propagation[-1]) # applying derivative of sigmoid to error
        print("self.o_deltar")
        print(self.o_delta.shape)

        for i in range(self._number_of_layers + 1):
            print("self.layers[-(1 + 2)]")
            print(self.layers[-(i + 2)].shape)
            self.z2_error = self.o_delta.dot(self.layers[-(i + 2)]) # z2 error: how much our hidden layer weights contributed to output error
            print("self.z2_error")
            print(self.z2_error.shape)
            self.o_delta = self.z2_error * self.sigmoidPrime(self.forward_propagation[-(i + 2)]) # applying derivative of sigmoid to z2 error

            # Updating the weights
            self.layers[-(i + 2)] += self.forward_propagation[-(i + 2)].dot(self.o_delta)

    def loss_function(self, X, Y):
        return "Loss: " + str(np.mean(np.square(Y - X))) # mean sum squared loss


    def train (self, X, Y):
        self.backpropagation(X, Y)

        print(loss_function(X, Y))
