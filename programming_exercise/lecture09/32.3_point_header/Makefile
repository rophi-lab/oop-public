CXX      = g++
CXXFLAGS = -Wall -Wextra -Wpedantic -std=c++17

SRCS = main.cpp point.cpp
OBJS = $(SRCS:.cpp=.o)
TARGET = point_lab

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

main.o: point.hpp
point.o: point.hpp

clean:
	rm -f $(OBJS) $(TARGET) $(TARGET).exe

.PHONY: all clean
