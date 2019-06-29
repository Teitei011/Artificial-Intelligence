import numpy as np

class NeuralLayer():
    def __init__(self, number_of_neurons, number_of_inputs_per_neuron):
        self._weights = 2 * np.random.random((number_of_inputs_per_neuron, number_of_neurons)) - 1

class NeuralNetwork():
    def __init__(self, layers):
        self._layers = layers

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def think(self, inputs):
        '''
            Forward propagation
        '''
        output_from_layers = np.dot(inputs, self._layers[0]._weights)

        for i in range(1, len(self._layers)  - 2):
            output_from_layers = np.dot(output_from_layers[i], self._layers[i + 1]._weights)

        return output_from_layers

    def show(self):
        for i in range(len(self._layers)):
            print("Layer {}".format(i + 1))
            print(self._layers[i]._weights)

    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):

        for iteration in range(number_of_training_iterations):
            output_from_layers = self.think(training_set_inputs)

            layers_errors = training_set_outputs - output_from_layers[-1]
            layers_deltas = layers_errors * self.sigmoid_derivative(output_from_layers[-1])

            layers_adjustment = training_set_inputs.T.dot(layers_deltas)
            self._layers[0]._weights += layers_adjustment

            for i in range(len(self._layers) - 1, 1, -1):
                layers_errors = layers_deltas.dot(self._layers[i]._weights.T)
                layers_delta = layers_errors * self.sigmoid_derivative(output_from_layers[i - 1])

                layers_adjustments = output_from_layers[i].T.dot(layers_delta)

                self._layers[i]._weights += layers_adjustments
