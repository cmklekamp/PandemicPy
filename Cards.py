# - - - - - - - - - - - - - - - - - - - -
# COP 4521 -- Term Project
# Daniel Fletcher, Connor Klekamp, Jacob Gregie
# PANDEMIC board game implementation
# - - - - - - - - - - - - - - - - - - - -


# * * * Cards.py * * *
# Card inheritance hierarchy
# Base "Card" class
# Derived "InfectionCard" class
# Derived "PlayerCard" class with 3 further sub-classes


# Relevant import statements


# Card class
# No data -- purely for polymorphic binding in card decks
class Card(object):
    def __init__(self):
        pass


# InfectionCard class
# Stores city name and color
class InfectionCard(Card):
    
    # Constructor with parameters
    def __init__(self, city, color):
        self._city = city
        self._color = color

    # Getter functions
    def get_city(self):
        return self._city

    def get_color(self):
        return self._color


# PlayerCard class
# No data -- serves as parent for three types of Player cards
class PlayerCard(Card):
    def __init__(self):
        pass


# CityCard class
# Stores city name, color, and population data
class CityCard(PlayerCard):

    # Constructor with parameters
    def __init__(self, city, color, population, density):
        self._city = city
        self._color = color
        self._population = population
        self._density = density

    # Getter functions
    def get_city(self):
        return self._city

    def get_color(self):
        return self._color

    def get_population(self):
        return self._population

    def get_density(self):
        return self._density


# EpidemicCard class
# No data -- class type is the important information
class EpidemicCard(PlayerCard):
    def __init__(self):
        pass


# EventCard class
# Stores type of event as num 1-5
# 1 - ONE QUIET NIGHT
# 2 - FORECAST
# 3 - GOVERNMENT GRANT
# 4 - AIRLIFT
# 5 - RESILIENT POPULATION
class EventCard(PlayerCard):

    # Constructor -- initializes card to specified value (1-5)
    def __init__(self, event_num):
        self._value = event_num

    # Getter functions
    def get_value(self):
        return self._value
