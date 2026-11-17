CXX      = g++
CXXFLAGS = -Wall -Wextra -Wpedantic -std=c++17

SRCS = main.cpp timer.cpp
OBJS = $(SRCS:.cpp=.o)
TARGET = timer_lab

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

main.o: timer.hpp
timer.o: timer.hpp

clean:
	rm -f $(OBJS) $(TARGET) $(TARGET).exe

.PHONY: all clean
