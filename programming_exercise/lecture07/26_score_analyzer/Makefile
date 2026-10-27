CXX      = g++
CXXFLAGS = -Wall -Wextra -Wpedantic -std=c++17
TARGET   = score_analyzer

all: $(TARGET)

$(TARGET): main.cpp
	$(CXX) $(CXXFLAGS) -o $(TARGET) main.cpp

clean:
	rm -f $(TARGET) $(TARGET).exe

.PHONY: all clean
