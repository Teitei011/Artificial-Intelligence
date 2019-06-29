import numpy as np
import ANN_Multilayer as ANN
# X = (hours sleeping, hours studying), y = score on test
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)

# scale units
X = X/np.amax(X, axis=0) # maximum of X array
y = y/100 # max test score is 100


inputSize = 2
outputSize = 1
neurons_in_hidden = 3
number_of_layers = 1
training_rate = 0.1

NN = ANN.Neural_Network(inputSize, outputSize, neurons_in_hidden, number_of_layers, training_rate)
# NN.show()
NN.query(X)



for i in range(1): # trains the NN 1,000 times
    # print ("Input: \n" + str(X))
    # print ("Actual Output: \n" + str(y))
    # print ("Predicted Output: \n" + str(NN.forward(X)))
    NN.train(X, y)
