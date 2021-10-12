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
        self._had_outbreak = False
        self._connected_cities = connected_list

    # add_cube()
    # Adds a disease cube of specified color to city ONLY IF city doesn't already have 3
    # Returns True if a cube is added; False if already at 3 (outbreak occurs)
    def add_cube(self, color):
        if color == "black" and self.black < 3:
            self.black += 1
            return True
        elif color == "blue" and self.blue < 3:
            self.blue += 1
            return True
        elif color == "red" and self.red < 3:
            self.red += 1
            return True
        elif color == "yellow" and self.yellow < 3:
            self.yellow += 1
            return True
        else:
            return False

    # remove_cube()
    # Removes a disease cube of specified color
    # Returns True if a cube is removed; False if already at 0
    def remove_cube(self, color):
        if color == "black" and self.black > 0:
            self.black -= 1
            return True
        elif color == "blue" and self.blue > 0:
            self.blue -= 1
            return True
        elif color == "red" and self.red > 0:
            self.red -= 1
            return True
        elif color == "yellow" and self.yellow > 0:
            self.yellow -= 1
            return True
        else:
            return False

    # add_station()
    # Adds a research station to the city ONLY IF it doesn't already have one
    # Returns True if a research station is added; False if it already had one
    def add_station(self):
        if self.has_station == False:
            self.has_station = True
            return True
        else:
            return False

    # remove_station()
    # Removes a research station to the city ONLY IF it already has one
    # Returns True if a research station is removed; False if it didn't have one already
    def remove_station(self):
        if self.has_station == True:
            self.has_station = False
            return True
        else:
            return False

    # Getter functions
    # ...

    @property
    def connected_cities(self):
        return self._connected_cities

    @property
    def has_station(self):
        return self._has_station

    @property
    def had_outbreak(self):
        return self._had_outbreak

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color

    @property
    def black(self):
        return self._black

    @property
    def blue(self):
        return self._blue

    @property
    def red(self):
        return self._red

    @property
    def yellow(self):
        return self._yellow

    # Setter functions
    # ...

    @has_station.setter
    def has_station(self, a):
        self.has_station = a

    @had_outbreak.setter
    def had_outbreak(self, a):
        self._had_outbreak = a

    @black.setter
    def black(self, a):
        self._black = a

    @blue.setter
    def blue(self, a):
        self._blue = a

    @red.setter
    def red(self, a):
        self._red = a

    @yellow.setter
    def yellow(self, a):
        self._yellow = a