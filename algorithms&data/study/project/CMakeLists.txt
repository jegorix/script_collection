cmake_minimum_required(VERSION 3.10)
project(AnimalProject)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(include)

add_executable(
    animal_program
    src/Animal.cpp
    main.cpp
)