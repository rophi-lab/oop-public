CXX      = g++
CXXFLAGS = -Wall -Wextra -Wpedantic -std=c++17

SRCS = main.cpp playlist.cpp
OBJS = $(SRCS:.cpp=.o)
TARGET = playlist_lab

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

main.o: playlist.hpp
playlist.o: playlist.hpp

clean:
	rm -f $(OBJS) $(TARGET) $(TARGET).exe

.PHONY: all clean
