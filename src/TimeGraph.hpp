

#ifndef TIMEGRAPH_HPP
#define TIMEGRAPH_HPP

#include <iostream>
#include "TimeGraph.hpp"
#include <ATen/ATen.h>

class TimeGraph {
  private:
    at::Tensor timeGraph;
    void constructGraph(int size);

  public:
    TimeGraph();
    TimeGraph(int size);
    ~TimeGraph();
};

#endif
