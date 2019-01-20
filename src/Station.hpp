

#ifndef STATION_HPP
#define STATION_HPP

#include <iostream>
#include <string>
#include <vector>

#include "Station.hpp"

class Station {
  private:
    double radiusOfEarthAtLat(double lat);
    double x;
    double y; 
    std::string name;
    double lat;
    double lon;
    double alt;

  public:
    Station();
    Station(std::string name, double lat, double lon, double alt);
    ~Station();

    void setModelCenter(double modelLat, double modelLon);
    std::string getName();
    double getLat();
    double getLon();
    double getAlt();
    double getX();
    double getY();

    static std::vector<Station*> loadStations();
};

#endif
