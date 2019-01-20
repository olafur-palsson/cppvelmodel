
#include "VelocityModel.hpp"
#include <iostream>
#include <ATen/ATen.h>

using namespace std;

// Need to set the speed of all 'z' values over 0 to a fixed known value 
// Needs to be in the contsructor

VelocityModel::VelocityModel() {
  VelocityModel::constructModel(200);
}

VelocityModel::VelocityModel(int size) {
  VelocityModel::constructModel(size);
}

VelocityModel::~VelocityModel() {
  cout << "Deleted a VelocityModel" << endl;
}

void VelocityModel::constructModel(int size) {
  this -> model = at::ones({size, size, size}, at::kDouble);
}

