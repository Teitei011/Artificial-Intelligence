import ANN as NN

layers = 1
neurons = 5
input_layer = 2
output_layer = 2
learning_rate = 0.01

nn = NN.NeuralNetwork(layers, neurons, input_layer, output_layer, learning_rate)
nn.showBrain()
# nn.save()
