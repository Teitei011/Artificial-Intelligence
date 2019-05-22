import internet as NN

layers = 1
neurons = 3
input_layer = 2
output_layer = 2
learning_rate = 0.01

input_array = [2, 5]



nn = NN.Network([15,50, 10])
# nn.showBrain()
nn.query(input_array)
