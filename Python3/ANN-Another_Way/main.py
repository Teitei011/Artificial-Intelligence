from ANN_Multilayer import NeuralLayer, NeuralNetwork
import numpy as np
#Seed the random number generator
np.random.seed(1)
layers = []
# Create layer 1 (40 neurons, each with 3 inputs)
layer1 = NeuralLayer(4, 3)
layers.append(layer1)


# Create layer 2 (40 neurons with 40 inputs)
layer2 = NeuralLayer(1, 4)
layers.append(layer2)

# # Create layer 2 (a single neuron with 4 inputs)
# layer3 = NeuralLayer(1, 40)
# layers.append(layer3)


# Combine the layers to create a neural network
neural_network = NeuralNetwork(layers)

neural_network.show()

# The training set. We have 7 examples, each consisting of 3 input values
# and 1 output value.
training_set_inputs = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1], [0, 0, 0]])
training_set_outputs = np.array([[0, 1, 1, 1, 1, 0, 0]]).T

# Train the neural network using the training set.
# Do it 60,000 times and make small adjustments each time.
neural_network.train(training_set_inputs, training_set_outputs, 1)

print("\n\nStage 2) New synaptic weights after training: ")
neural_network.show()

# Test the neural network with a new situation.
print("\n\nStage 3) Considering a new situation [1, 1, 0] -> ?: ")
output = neural_network.think(np.array([1, 1, 0]))
print(output[-1])
