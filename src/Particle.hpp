

#ifndef PARTICLE_HPP
#define PARTICLE_HPP

#include <iostream>
#include "Particle.hpp"
#include "Station.hpp"
#include <ATen/ATen.h>

class Particle {
  private:
    at::Tensor position;

  public:
    Particle();
    Particle(Station* station);
    ~Particle();
};

#endif
