import numpy as np
import ANN_Multilayer as ANN
# X = (hours sleeping, hours studying), y = score on test
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)

# scale units
X = X/np.amax(X, axis=0) # maximum of X array
y = y/100 # max test score is 100

NN = ANN.Neural_Network(2, 1, 5, 10)
NN.show()
NN.feedforward(X)


for i in range(10000): # trains the NN 1,000 times
    # print ("Input: \n" + str(X))
    # print ("Actual Output: \n" + str(y))
    # print ("Predicted Output: \n" + str(NN.forward(X)))

    # print ("Loss: " + str(np.mean(np.square(y - NN.feedforward(X))))) # mean sum squared loss
    NN.train(X, y)
