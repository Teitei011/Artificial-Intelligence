import scipy.special
import numpy as np
import os

class NeuralLayer:
    def __init__(self, neurons_inputs, neurons):
        self.weights = []

        for i in range(neurons):
            self.temp = []
            for j in range(neurons_inputs):
                self.temp.append(np.random.normal(0.0, pow(neurons_inputs, -0.5)))

            self.weights.append(self.temp)


    def show(self):
        return self.weights

class NeuralNetwork:
    def __init__(self, _layers, _neurons, _input_layer , _output_layer, _learning_rate):
        self.number_of_layers = _layers + 2 # It has + 2 because the input layer and the output layer
        self.neurons = _neurons
        self.input_layer = _input_layer
        self.output_layer = _output_layer
        self.learning_rate = _learning_rate
        self.layers = []

        for i in range(self.number_of_layers):

            # Input Layer
            if (i == 0):
                self.layers.append(NeuralLayer(self.input_layer, 1))

            # Output Layer
            elif (i + 1 == self.number_of_layers):
                self.layers.append(NeuralLayer(self.output_layer, 1))

            # Hidden Layers
            else:
                self.layers.append(NeuralLayer(self.neurons, self.neurons))


    def showBrain(self):
        for i in range(self.number_of_layers):
            if (i == 0):
                print("Input Layer: " + str(self.layers[i].show()))

            elif (i + 1 == self.number_of_layers):
                print("Ouput Layer: " + str(self.layers[i].show()))
            else:
                print("Hidden Layer: " + str(self.layers[i].show()))

    def save(self):
        print("Creating directory...")
        try:
            path = os.mkdir("Weights")
        except:
            print("Directory already created...")

        os.chdir("Weights/")

        # Creating file to know how many arrays it has
        data = open("Number_of_layers.txt", "w")
        data.write(str(self.number_of_layers))
        data.close()

        for i in range(self.number_of_layers):
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

    def activation(array):
        for i in range(len(array)):
            array[i] = scipi.special.expit(array[i])
        return array

    def train(self, input_array, output_array):
        pass

    def feedforward(self):
        pass

    def backpropagation(self):
        pass

    def query(self, input_array):
        pass
