include <vector>;

class NeuralLayer{
  constructor(neurons_inputs, neurons){
    std::vector<float> weights;


};

class NeuralNetwork{
  int _number_of_layers;
  int _neurons;
  int _input_layer, _output_layer;
  int _learning_rate;

  std::vector<float> _layers;

public:
  NeuralNetwork(int number_of_layers, int neurons, int input_layer, int output_layer, int learning_rate)
    : _number_of_layers(number_of_layers), _neurons(neurons), _input_layer(input_layer),
    _output_layer(output_layer), _learning_rate(learning_rate);

    void saveBrain();
    void loadBrain();
    NeuralLayer activation();
    std::vector<float> query();
    std::vector<float> train();

    void backpropagation();
    void feedforward();

};
