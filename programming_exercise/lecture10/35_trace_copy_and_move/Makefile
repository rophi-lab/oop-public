CXX      = g++
CXXFLAGS = -Wall -Wextra -Wpedantic -std=c++17

SRCS = main.cpp tracer.cpp
OBJS = $(SRCS:.cpp=.o)
TARGET = tracer_lab

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

main.o: tracer.hpp
tracer.o: tracer.hpp

# A second build with copy elision switched off, so you can see the
# operations the compiler normally removes for you.
noelide:
	$(CXX) $(CXXFLAGS) -fno-elide-constructors -o $(TARGET)_noelide $(SRCS)

clean:
	rm -f $(OBJS) $(TARGET) $(TARGET)_noelide $(TARGET).exe

.PHONY: all clean noelide
