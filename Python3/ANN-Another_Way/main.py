from ANN_Multilayer import NeuralLayer, NeuralNetwork
import numpy as np
import os

def load_mnist(kind='train'):

    """Load MNIST data from `path`"""
    labels_path = os.path.join('%s-labels-idx1-ubyte'% kind)
    images_path = os.path.join('%s-images-idx3-ubyte'% kind)

    with open(labels_path,'rb') as lbpath:
        labels = np.frombuffer(lbpath.read(), dtype=np.uint8,
                               offset=8)

    with open(images_path,'rb') as imgpath:
        images = np.frombuffer(imgpath.read(), dtype=np.uint8,
                               offset=16).reshape(len(labels), 784)

    return images, labels


images = []
labels = []

images, labels = load_mnist()

#Seed the random number generator
np.random.seed(1)
layers = []

# Create layer 1 (40 neurons, each with 3 inputs)
layer1 = NeuralLayer(60, 784)
layers.append(layer1)

# Create layer 1 (40 neurons, each with 3 inputs)

layer2 = NeuralLayer(60, 40)
layers.append(layer1)


# Create layer 2 (40 neurons with 40 inputs)
layer3 = NeuralLayer(10, 60)
layers.append(layer2)


# Combine the layers to create a neural network
neural_network = NeuralNetwork(layers)

# neural_network.show()

# Train the neural network using the training set.
# Do it 60,000 times and make small adjustments each time.
neural_network.train(images, labels, 1000)
neural_network.save()
