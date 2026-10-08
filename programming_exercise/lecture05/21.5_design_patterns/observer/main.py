"""
Exercise 21.5e: Observer

Goal:
    WeatherStation keeps a list of observers and notifies them when the
    temperature changes.
    Do not edit the Observer base class or WeatherStation.__init__.
    __init__ already creates self.observers as an empty list and sets
    self.temperature to None.

--------------------------------------------------------------------------------
1. TemperatureDisplay.update(self, temperature)
    Print one line. Use this text, including the space before C:
        Temperature: <temperature> C
    An f-string does that:
        print(f"Temperature: {temperature} C")
    Example: temperature 32 prints
        Temperature: 32 C

2. HeatWarning.update(self, temperature)
    Print only when the day is hot.
        if temperature >= 30:
            print("Hot day: drink water!")
    If temperature is below 30, print nothing.
    Still let the method run. Do not raise an error for a cool day.
    32 prints the warning. 20 prints nothing.

3. WeatherStation.subscribe(self, observer)
    Add that observer to the end of self.observers.
        self.observers.append(observer)

4. WeatherStation.unsubscribe(self, observer)
    Remove that observer only when it is already in the list.
        if observer in self.observers:
            self.observers.remove(observer)
    If it is not registered, do nothing. Do not raise an error.
    remove() deletes the first matching object. The demo unsubscribes the
    same HeatWarning object that was subscribed, so this is the right object.

5. WeatherStation.set_temperature(self, temperature)
    Do these two things, in this order:
        a. Save the reading:
               self.temperature = temperature
        b. Notify whoever is still subscribed, from first to last:
               for observer in self.observers:
                   observer.update(temperature)
    Call update() even when the new temperature equals the old one.

How the demo uses your code:
    subscribe a display, then subscribe a warning.
    set_temperature(32) notifies both, in that order:
        Temperature: 32 C
        Hot day: drink water!
    unsubscribe the warning.
    set_temperature(20) notifies only the display:
        Temperature: 20 C
    The warning is gone, and 20 would have been silent anyway.

How to run:
    python main.py
"""


class Observer:
    def update(self, temperature: float) -> None:
        raise NotImplementedError


class TemperatureDisplay(Observer):
    def update(self, temperature: float) -> None:
        # TODO: print(f"Temperature: {temperature} C")
        pass


class HeatWarning(Observer):
    def update(self, temperature: float) -> None:
        # TODO: if temperature >= 30, print("Hot day: drink water!")
        #       Below 30, print nothing.
        pass


class WeatherStation:
    def __init__(self) -> None:
        self.observers: list[Observer] = []
        self.temperature: float | None = None

    def subscribe(self, observer: Observer) -> None:
        # TODO: self.observers.append(observer)
        pass

    def unsubscribe(self, observer: Observer) -> None:
        # TODO: if observer is in self.observers, remove it.
        #       If it is not in the list, do nothing.
        pass

    def set_temperature(self, temperature: float) -> None:
        # TODO: self.temperature = temperature
        # TODO: for each observer still in self.observers, call
        #       observer.update(temperature)
        pass


# ------------------------------- DO NOT EDIT -------------------------------- #

if __name__ == "__main__":
    station = WeatherStation()
    warning = HeatWarning()
    station.subscribe(TemperatureDisplay())
    station.subscribe(warning)
    station.set_temperature(32)
    station.unsubscribe(warning)
    station.set_temperature(20)


# Expected Output:
# Temperature: 32 C
# Hot day: drink water!
# Temperature: 20 C
