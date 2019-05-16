#include <Eigen/Dense>
#include <vector>
#include <iostream>

using Eigen::MatrixXd;

class NeuralNetwork{
  int _number_of_layers;
  int _neurons;
  int _input_layer, _output_layer;
  int _learning_rate;

  std::vector<float>  _network;
  NeuralNetwork(int number_of_layers, int neurons, int input_layer, int output_layer, float learning_rate);

public:
    void createNetwork(std::vector<MatrixXd> layers, int neurons);

    void show();

    void saveBrain();
    void loadBrain();
    std::vector<float> activation();
    std::vector<float> query();
    std::vector<float> train();

    void backpropagation();
    void feedforward();

};

NeuralNetwork::NeuralNetwork(int number_of_layers, int neurons, int input_layer, int output_layer, float learning_rate){
  int _number_of_layers{number_of_layers};
  int _neurons{neurons};
  int _input_layer{input_layer};
  int _output_layer{output_layer};
  float _learning_rate{learning_rate};

  // Creating all the layers
  std::vector<MatrixXd> layers;
  createNetwork(layers, neurons);

  show();
}

void NeuralNetwork::createNetwork(std::vector<MatrixXd> layers, int neurons){
  for (int i = 0; i < _number_of_layers; ++i){
    // Input Layer
    if (i == 0) layers.push_back(MatrixXd::Random(1, _input_layer));

    // Creating Hidden Layers
    else if (i == 1) layers.push_back(MatrixXd::Random(neurons, neurons));

    // Output Layer
    else if (i - 1 == _number_of_layers) layers.push_back(MatrixXd::Random(1, _output_layer));
  }

}

void NeuralNetwork::show(){
  for (int i = 0; i < _number_of_layers; ++i){
    std::cout << layers[i] << std::endl;
  }
}

void NeuralNetwork::saveBrain(){

}

// std::vector<float> NeuralNetwork::activation(current){

// }

std::vector<float> NeuralNetwork::query(){

}

std::vector<float> NeuralNetwork::train(){

}

void NeuralNetwork::backpropagation(){

}

void NeuralNetwork::feedforward(){

}
