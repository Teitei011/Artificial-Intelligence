import scipy.special
import numpy as np
import os
from math import exp

def createNeuralLayer(neurons_inputs, neurons):
    weights = []

    if (neurons == 1): # Para o input e o output
        temp = []
        for j in range(neurons_inputs):
            temp.append(np.random.normal(0.0, pow(neurons_inputs, -0.5)))

        weights.append(temp)

    else:
        for i in range(neurons):
            temp = []
            for j in range(neurons_inputs):
                temp.append(np.random.normal(0.0, pow(neurons_inputs, -0.5)))

            weights.append(temp)

    return weights


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
                self.layers.append(createNeuralLayer(self.input_layer, 1))

            # Output Layer
            elif (i + 1 == self.number_of_layers):
                self.layers.append(createNeuralLayer(self.output_layer, 1))

            # Hidden Layers
            else:
                self.layers.append(createNeuralLayer(self.neurons, self.neurons))


    def showBrain(self):
        for i in range(self.number_of_layers):
            if (i == 0):
                print("Input Layer: " + str(self.layers[i]))

            elif (i + 1 == self.number_of_layers):
                print("Ouput Layer: " + str(self.layers[i]))
            else:
                print("Hidden Layer: " + str(self.layers[i]))

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


    def query(self, input_array):
        # Convert input into 2d Array
        inputs = input_array

        # Calculate signals into hidden layer
        for i in range(self.number_of_layers):
            if (i == 0): # First Time
                hidden_inputs = np.dot(self.layers[i], inputs)

                # Calculate signal emerging from hiden layer
                final_inputs = self.activation(hidden_inputs)

                # Calculate the signal emerging from final outputs
                final_outputs = self.activation(final_inputs)

            else:
                hidden_inputs = np.dot(self.layers[i], self.layers[i-1])

                # Calculate signal emerging from hiden layer
                final_inputs = self.activation(hidden_inputs)

                # Calculate the signal emerging from final outputs
                final_outputs = self.activation(final_inputs)

        return final_outputs

    def activation(self, array):
        for i in range(len(array)):
            array[i] = 1 / ( 1 + exp(-array[i]))
        return array

    def train(self, input_array, output_array):
        inputs = input_array

        # Calculate signals into hidden layer
        for i in range(self.number_of_layers):
            if (i == 0): # First Time
                hidden_inputs = np.dot(self.layers[i].matrix(), inputs)

                # Calculate signal emerging from hiden layer
                final_inputs = self.activation(hidden_inputs)

                # Calculate the signal emerging from final outputs
                final_outputs = self.activation(final_inputs)

            else:
                hidden_inputs = np.dot(self.layers[i].matrix(), self.layers[i-1])

                # Calculate signal emerging from hiden layer
                final_inputs = self.activation(hidden_inputs)

                # Calculate the signal emerging from final outputs
                final_outputs = self.activation(final_inputs)

        # Calculating the erros to each layer
        for i in range(self.number_of_layers):
            output_errors, hidden_errors = calculate_error(self, target, final_outputs)
            backpropagation(self, output_errors, final_outputs, hidden_errors, hidden_outputs)

    def calculate_error(self, target, final_outputs):
        output_errors = target - final_outputs
        hidden_errors = np.dot(self.layers[i], output_errors)

        return output_errors, hidden_errors

    def backpropagation(self, output_errors, final_outputs, hidden_errors, hidden_outputs):
        self.weigth_hidden_output += self.learning_rate* np.dot((output_errors * final_outputs * (1.0 - final_outputs)), np.transpose(hidden_errors))
        self.weigth_input_hidden += self.learning_rate * np.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), np.transpose(inputs))
