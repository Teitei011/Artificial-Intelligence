#include <Eigen/Dense>
#include <vector>
#include <iostream>

using Eigen::MatrixXd;

int main() {
  std::vector<MatrixXd> array_of_matrix;
  double e{2.71828182845904523536};
  void show(std::vector<MatrixXf> array_of_matrix);


  // Creating the random matrix
  for (int i = 0; i < 5; ++i){
    MatrixXf temp =  MatrixXf::Random(2, 2);
    array_of_matrix.push_back(temp);
  }

  show(array_of_matrix);

  std::cout << "Making the transformation..." << '\n';

  for (int i = 0; i < 5; ++i){
    MatrixXf temp = array_of_matrix[i];
    for (int j = 0; j < 2; ++j){
      for (int k = 0; k < 2; ++k){
        temp(j, k) = 1. / (1. + pow(e, -temp(j ,k)));
      }
    }
  }

  show(array_of_matrix);

  return 0;
}


void show(std::vector<MatrixXd> array_of_matrix){
  for (int i = 0; i < 5; ++i){
    std::cout << "Matrix: " << i << " \n" << array_of_matrix[i] << std::endl;
  }
}
