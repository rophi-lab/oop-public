# Exercise 22: Makefile
#
# The C++ sources are already finished. Fill in this file, then run:
#     make
#     ./geometry              (geometry.exe on Windows)
#     make clean
#
# IMPORTANT: every command line under a target must start with a TAB, not spaces.

CXX      = g++
CXXFLAGS = -Wall -Wextra -Wpedantic -std=c++17
TARGET   = geometry
OBJECTS  = main.o geometry.o

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJECTS)

%.o: %.cpp geometry.hpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(OBJECTS) $(TARGET) $(TARGET).exe

.PHONY: all clean
