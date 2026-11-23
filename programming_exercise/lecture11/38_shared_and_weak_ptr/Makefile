CXX      = g++
CXXFLAGS = -Wall -Wextra -Wpedantic -std=c++17

SRCS = main.cpp node.cpp
OBJS = $(SRCS:.cpp=.o)
TARGET = shared_ptr_lab

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

main.o: node.hpp
node.o: node.hpp

# Part B: the address sanitizer reports the cycle in Part 3 as a real leak.
# That leak is intentional -- it is the point of the exercise.
asan:
	$(CXX) $(CXXFLAGS) -fsanitize=address,undefined -g -o $(TARGET)_asan $(SRCS)

clean:
	rm -f $(OBJS) $(TARGET) $(TARGET)_asan $(TARGET).exe

.PHONY: all clean asan
