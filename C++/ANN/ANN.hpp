#include "Eigen/Dense"
#include <vector>
#include <iostream>

using Eigen::MatrixXd;
using WeigthsVector = std::vector<MatrixXd>;


class NeuralNetwork{
  int _number_of_layers;
  int _neurons;
  int _input_layer, _output_layer;
  int _learning_rate;

  double e{2.71828182845904523536};

  WeigthsVector _layers;

public:

    NeuralNetwork(int number_of_layers, int neurons, int input_layer, int output_layer, float learning_rate = 0.01);

    void createNetwork(int _number_of_layers, int _input_layer, int _neurons,  int _output_layer);

    void show();
    void activation(std::vector<MatrixXd> *current);

    void saveBrain();
    void loadBrain();
    std::vector<float> query();
    std::vector<float> train();

    void backpropagation();
    void feedforward();

};

NeuralNetwork::NeuralNetwork(int number_of_layers, int neurons, int input_layer, int output_layer, float learning_rate){
   _number_of_layers = number_of_layers + 2; //It has a plus 2 because it has the input layer and the output layer
   _neurons = neurons;
   _input_layer = input_layer;
   _output_layer = output_layer ;
   _learning_rate = learning_rate;

  // Creating all the layers
   NeuralNetwork::createNetwork(_number_of_layers,  _input_layer, _neurons,  _output_layer);

  show();
}

void NeuralNetwork::createNetwork(int _number_of_layers, int _input_layer, int _neurons, int _output_layer){

  for (int i = 0; i < _number_of_layers; ++i){
    // Input Layer
    if (i == 0) _layers.push_back(MatrixXd::Random(_input_layer, 1));

    // Creating Hidden Layers
    else if (i != 1 && i -1 != _number_of_layers) _layers.push_back(MatrixXd::Random(_neurons, _neurons));

    // Output Layer
    else if (i - 1 == _number_of_layers) _layers.push_back(MatrixXd::Random(_output_layer, 1));
  }
}

void NeuralNetwork::show(){
  for (int i = 0; i < _number_of_layers; ++i){
    if (i == 0) std::cout << "Input Layer: ";
    if (i < _number_of_layers) std::cout << "Output Layer: ";
    std::cout << _layers[i] << std::endl;
  }
}

void NeuralNetwork::activation(std::vector<MatrixXd> *current){

}


void NeuralNetwork::saveBrain(){

}

void loadBrain(){

}

std::vector<float> NeuralNetwork::query(){

}

std::vector<float> NeuralNetwork::train(){

}

void NeuralNetwork::backpropagation(){

}

void NeuralNetwork::feedforward(){

}
