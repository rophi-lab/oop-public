CXX      = g++
CXXFLAGS = -Wall -Wextra -Wpedantic -std=c++17

SRCS = main.cpp resource.cpp
OBJS = $(SRCS:.cpp=.o)
TARGET = unique_ptr_lab

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

main.o: resource.hpp
resource.o: resource.hpp

# Optional: build with the address sanitizer. If unique_ptr is doing its job
# this reports no leaks at all.
asan:
	$(CXX) $(CXXFLAGS) -fsanitize=address,undefined -g -o $(TARGET)_asan $(SRCS)

clean:
	rm -f $(OBJS) $(TARGET) $(TARGET)_asan $(TARGET).exe

.PHONY: all clean asan
