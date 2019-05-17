all: main.o NeuralLayer.o NeuralNetwork.o
	clang++ -std=c++17 -Wall -Wpedantic -Wextra -O2 *.o -o Brain.exe

main.o: main.cpp
	g++  -o main.cpp NeuralLayer.hpp NeuralNetWork.hpp

NeuralLayer.o: NeuralLayer.hpp
	g++ -o NeuralLayer.hpp

NeuralNetwork.o: NeuralNetwork.hpp
	g++ -o NeuralNetwork.hpp
