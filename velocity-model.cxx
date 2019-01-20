
#include <iostream>
#include <torch/torch.h>
#include "src/Station.hpp"
#include "src/TimeGraph.hpp"
#include "src/VelocityModel.hpp"
#include "src/Particle.hpp"
#include <vector>

int main() {
  std::vector<Station*> stations = Station::loadStations();
  for (Station* station : stations) {
    std::cout << station -> getName() << "\n";
    station -> setModelCenter(64.0980, 21.1197);
  }

  TimeGraph* t = new TimeGraph();
  VelocityModel* m = new VelocityModel();
  Particle* p = new Particle();

}


/**
 * Interesting functions to use:
 *    convultional 3d layer to calculate make rays affect surroundings
 *    sin / cos from torch:
 *      maybe calculate first one layer down, then back up then input
 *      into sin/cos layer
 *    Then just lol something yolo, run things on processor if possible
 *
 * Also, making the timegraphs for each station run of different processes
 * would save a lot of time I think.
 *
 * Then after maybe I could try to make some optimisations to run things faster.
 * 
 * To think about:
 *   Is it possible to program manually the graphics card to simulate the particle
 *   position?
 */
