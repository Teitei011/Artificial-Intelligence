#include <iostream>
#include "ANN.hpp"


int main(){

  int number_of_layers{2};
  int neurons{2};
  int input_layer{5};
  int output_layer{1};
  double learning_rate{0.01};

  NeuralNetwork nn(number_of_layers, neurons, input_layer, output_layer, learning_rate);
  nn.show();
  return 0;
}
