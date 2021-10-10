# - - - - - - - - - - - - - - - - - - - -
# COP 4521 -- Term Project
# Daniel Fletcher, Connor Klekamp, Jacob Gregie
# PANDEMIC board game implementation
# - - - - - - - - - - - - - - - - - - - -


# * * * City.py * * *
# City class
# Encapsulates data and behavior of "City spaces"
# To be used on game board


# City class
class City(object):
    
    # Constructor with parameters
    # "connected_list" should be a list of city names that connect to this city
    def __init__(self, name, color, connected_list):
        self._name = name
        self._color = color
        self._black = 0
        self._blue = 0
        self._red = 0
        self._yellow = 0
        self._has_station = False
        self._connected_cities = connected_list

    # add_cube()
    # Adds a disease cube of specified color to city ONLY IF city doesn't already have 3
    # Returns True if a cube is added; False if already at 3 (outbreak occurs)
    def add_cube(self, color):
        pass

    # remove_cube()
    # Removes a disease cube of specified color
    # Returns True if a cube is added; False if already at 0
    def remove_cube(self, color):
        pass

    # add_station()
    # Adds a research station to the city ONLY IF it doesn't already have one
    # Returns True if a research station is added; False if it already had one
    def add_station(self):
        pass

    # remove_station()
    # Removes a research station to the city ONLY IF it already has one
    # Returns True if a research station is removed; False if it didn't have one already
    def remove_station(self):
        pass

    # Getter functions
    # ...

    @property
    def connected_cities(self):
        return self._connected_cities

    @property
    def has_station(self):
        return self._has_station