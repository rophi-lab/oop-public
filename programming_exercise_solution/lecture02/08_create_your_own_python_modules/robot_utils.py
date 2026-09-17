def print_robot_status(name, battery):
    """
    Input: A string name and an integer battery, e.g., "Robot1" and 50
    Output: Print the robot status, e.g., "Robot1 has 50% battery"
    (This function prints; it does not return a value.)
    """
    # TODO: print the robot name and battery percentage
    print(name + " has " + str(battery) + "% battery")


def is_battery_low(battery):
    """
    Input: An integer battery, e.g., 50
    Output: True if the battery is less than 20, False otherwise
    """
    # TODO: return True when battery is less than 20
    return battery < 20
