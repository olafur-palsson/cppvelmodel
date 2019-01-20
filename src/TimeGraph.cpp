
#include "TimeGraph.hpp"
#include <iostream>
#include <ATen/ATen.h>

using namespace std;

TimeGraph::TimeGraph() {
  cout << "Constructed a TimeGraph" << endl;
  TimeGraph::constructGraph(200);
}

TimeGraph::TimeGraph(int size) {
  TimeGraph::constructGraph(size);
}

void TimeGraph::constructGraph(int size) {
  this -> timeGraph = at::ones({size, size, size}, at::kDouble) * 9999;
}

TimeGraph::~TimeGraph() {
  cout << "Deleted a TimeGraph" << endl;
}

