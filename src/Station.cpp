
#include "Station.hpp"
#include <iostream>
#include <math.h>
#include <vector>
#include <fstream>
#include <torch/torch.h>

#define PI 3.14159265
#define EARTH_RADIUS 6373

using namespace std;

Station::Station() {
}

Station::Station(std::string name, double lat, double lon, double alt) {
  this -> name = name;
  this -> lat = lat;
  this -> lon = lon;
  this -> alt = alt;
}

Station::~Station() {

}

double Station::radiusOfEarthAtLat(double latitude) {
  double diameterAtLatitude = cos(latitude * PI / 180.0) * 6373;
  vector<double> v;
  return diameterAtLatitude;
}

void Station::setModelCenter(double modelLat, double modelLon) {
  y = (lat - modelLat) * EARTH_RADIUS * 2 * PI / 360;
  x = (lon - modelLon) * radiusOfEarthAtLat(modelLat) * 2 * PI / 360;
}

string Station::getName() {
  return this -> name;
}

double Station::getLat() {
  return this -> lat;
}

double Station::getLon() {
  return this -> lon;
}

double Station::getAlt() {
  return this -> alt;
}

double Station::getX() {
  return this -> x;
}

double Station::getY() {
  return this -> y;
}

vector<Station*> Station::loadStations() {
  vector<Station*> stations;
  std::ifstream stationFile("./data/Hengill.sta");
  cout << "Did something \n";
  if (stationFile.is_open()) {
    std::string line;
    while (getline(stationFile, line)) {
      std::cout << line << "\n";
      string name = line.substr(0, 4);
      string latString = line.substr( 4, 11);
      string lonString = line.substr(13, 21);
      string altString = line.substr(23, 27);
      double lat = stod(latString);
      double lon = stod(lonString);
      double alt = stod(altString);
      Station* station = new Station(name, lat, lon, alt);
      stations.push_back(station);
    }
  }
  return stations;
}
