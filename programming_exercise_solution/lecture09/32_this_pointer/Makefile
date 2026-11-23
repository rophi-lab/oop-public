CXX      = g++
CXXFLAGS = -Wall -Wextra -Wpedantic -std=c++17

SRCS = main.cpp counter.cpp
OBJS = $(SRCS:.cpp=.o)
TARGET = this_lab

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

main.o: counter.hpp
counter.o: counter.hpp

clean:
	rm -f $(OBJS) $(TARGET) $(TARGET).exe

.PHONY: all clean
