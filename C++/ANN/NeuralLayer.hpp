#include <Eigen/Dense>
#include <vector>
#include <iostream>

using Eigen::MatrixXd;

class NeuralLayer{
  MatrixXd _layer;

  NeuralLayer(int neurons_inputs, int neuronios){
    _layer = MatrixXd::Random(neurons_inputs, neuronios);
}

  public:
};
