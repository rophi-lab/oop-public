CXX      = g++
CXXFLAGS = -Wall -Wextra -Wpedantic -std=c++17

SRCS = main.cpp int_buffer.cpp
OBJS = $(SRCS:.cpp=.o)
TARGET = memory_lab

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

main.o: int_buffer.hpp
int_buffer.o: int_buffer.hpp

# Optional: build with the address sanitizer to catch leaks, double frees and
# use-after-free at run time. Run ./memory_lab_asan afterwards.
asan:
	$(CXX) $(CXXFLAGS) -fsanitize=address,undefined -g -o $(TARGET)_asan $(SRCS)

clean:
	rm -f $(OBJS) $(TARGET) $(TARGET)_asan $(TARGET).exe

.PHONY: all clean asan
