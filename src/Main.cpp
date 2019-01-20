
#include <torch/torch.h>
#include "Particle.hpp"
#include "Station.hpp"
#include "Main.hpp"
#include <iostream>

Main::Main() {
  cout << "Constructed a Main" << endl;
}

Main::~Main() {
  cout << "Deleted a Main" << endl;
}

int main() {
  Particle* p = new Particle();
  torch::Tensor tensor = torch::rand({2, 3});
  std::cout << tensor << std::endl;

  Station* station = new Station();
  delete station;

  return 1;
}

