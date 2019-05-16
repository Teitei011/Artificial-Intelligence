#include <vector>

class NeuralLayer{
  NeuralLayer(int neurons_inputs, int neurons);
};

class NeuralNetwork{
  int _number_of_layers;
  int _neurons;
  int _input_layer, _output_layer;
  int _learning_rate;

  NeuralLayer _layers;

  NeuralNetwork(int number_of_layers, int neurons, int input_layer, int output_layer, float learning_rate);

public:
    void saveBrain();
    void loadBrain();
    std::vector<float> activation();
    std::vector<float> query();
    std::vector<float> train();

    void backpropagation();
    void feedforward();

};

NeuralLayer::NeuralLayer(int neurons_inputs, int neurons){

}

NeuralNetwork::NeuralNetwork(int number_of_layers, int neurons, int input_layer, int output_layer, float learning_rate){
  int _number_of_layers{number_of_layers};
  int _neurons{neurons};
  int _input_layer{input_layer};
  int _output_layer{output_layer};
  float _learning_rate{learning_rate};

  _layers = NeuralLayer::NeuralLayer( _number_of_layers,  _neurons );

}

void NeuralNetwork::saveBrain(){

}

std::vector<float> NeuralNetwork::activation(NeuralLayer current){

}

std::vector<float> NeuralNetwork::query(){

}

std::vector<float> NeuralNetwork::train(){

}

void NeuralNetwork::backpropagation(){

}

void NeuralNetwork::feedforward(){

}
