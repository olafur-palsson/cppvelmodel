cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(velocity-model)

set (SOURCE_FOLDER "src")

find_package(Torch REQUIRED)

include_directories(.)
add_executable(velocity-model 
  velocity-model.cxx 
  src/Station.cpp
  src/TimeGraph.cpp
  src/VelocityModel.cpp
  src/Particle.cpp
  )

target_link_libraries(velocity-model "${TORCH_LIBRARIES}")
set_property(TARGET velocity-model PROPERTY CXX_STANDARD 11)
