
#include "Particle.hpp"
#include <iostream>

using namespace std;

Particle::Particle() {
  cout << "Constructed a Particle" << endl;
}

Particle::Particle(Station* station) {
  double x = station -> getX();
  double y = station -> getY();
  double z = 0;

  cout << "x == " << x << endl;
  cout << "y == " << y << endl;
  cout << "z == " << z << endl;
}

Particle::~Particle() {
  cout << "Deleted a Particle" << endl;
}

