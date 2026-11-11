CXX      = g++
CXXFLAGS = -Wall -Wextra -Wpedantic -std=c++17

SRCS = main.cpp bank_account.cpp savings_account.cpp
OBJS = $(SRCS:.cpp=.o)
TARGET = bank_lab

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

main.o: bank_account.hpp savings_account.hpp
bank_account.o: bank_account.hpp
savings_account.o: savings_account.hpp bank_account.hpp

clean:
	rm -f $(OBJS) $(TARGET) $(TARGET).exe

.PHONY: all clean
