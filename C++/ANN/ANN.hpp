#include <Eigen/Dense>
#include <vector>
#include <iostream>

using Eigen::MatrixXd;

class NeuralNetwork{
  int _number_of_layers;
  int _neurons;
  int _input_layer, _output_layer;
  int _learning_rate;

  double e{2.71828182845904523536};

  std::vector<MatrixXd> _layers;
  NeuralNetwork(int number_of_layers, int neurons, int input_layer, int output_layer, float learning_rate = 0.01);

public:
    std::vector<MatrixXd> createNetwork(int _number_of_layers, int _input_layer, int _neurons,  int _output_layer);

    void show();
    std::vector<MatrixXd> activation(std::vector<MatrixXd> *current);

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
   _layers = NeuralNetwork::createNetwork(_number_of_layers,  _input_layer, _neurons,  _output_layer);

  show();
}

std::vector<MatrixXd> NeuralNetwork::createNetwork(int _number_of_layers, int _input_layer, int _neurons, int _output_layer){
  std::vector<MatrixXd> layers;

  for (int i = 0; i < _number_of_layers; ++i){
    // Input Layer
    if (i == 0) layers.push_back(MatrixXd::Random(_input_layer, 1));

    // Creating Hidden Layers
    else if (i == 1) layers.push_back(MatrixXd::Random(_neurons, _neurons));

    // Output Layer
    else if (i - 1 == _number_of_layers) layers.push_back(MatrixXd::Random(_output_layer, 1));
  }
  return layers;
}

void NeuralNetwork::show(){
  for (int i = 0; i < _number_of_layers; ++i){
    std::cout << layers[i]; << '\n';
  }
}

std::vector<MatrixXd>NeuralNetwork::activation(std::vector<MatrixXd> *current){
  new (&current) Map<MatrixXd>(1. / (1. +  e**(-data)));
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
