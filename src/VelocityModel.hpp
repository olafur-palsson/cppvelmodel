

#ifndef VELOCITYMODEL_HPP
#define VELOCITYMODEL_HPP

#include <iostream>
#include "VelocityModel.hpp"
#include <ATen/ATen.h>

class VelocityModel {
  private:
    void constructModel(int size);
    at::Tensor model;

  public:
    VelocityModel();
    VelocityModel(int size);
    ~VelocityModel();
};

#endif
