# - - - - - - - - - - - - - - - - - - - -
# COP 4521 -- Term Project
# Daniel Fletcher, Connor Klekamp, Jacob Gregie
# PANDEMIC board game implementation
# - - - - - - - - - - - - - - - - - - - -


# * * * Player.py * * *
# Player class
# Encapsulates Player data and behavior
# To be used on game board


# Relevant import statements
from Cards import *
from City import *


# Key for Role numbers
# 1 - DISPATCHER
# 2 - OPERATIONS EXPERT
# 3 - MEDIC
# 4 - RESEARCHER
# 5 - CONTINGENCY PLANNER
# 6 - QUARANTINE SPECIALIST
# 7 - SCIENTIST


# Player class
class Player(object):
    
    # Constructor with parameters
    # Initializes player role number (1-7), corresponding color, and current city
    def __init__(self, role_num, starting_city):
        self._role = role_num
        self._current_city = starting_city
        self._username = ""

    # - - - GETTER FUNCTIONS - - -
    # get_username() 
    @property
    def username(self):
        return self._username

    # - - - SETTER FUNCTIONS - - -
    # set_username()
    # Sets the player's username to the given parameter
    @username.setter
    def set_username(self, username):
        self._username = username

    # acquire_card()
    # Adds a card to the player's hand
    def acquire_card(self):
        pass

    # over_hand_limit()
    # Returns True if the player has more than 7 cards in hand; False otherwise
    def over_hand_limit(self):
        pass

    # can_turn_in()
    # Returns True if the player can turn in a set; False otherwise
    # Takes special case of Role #7 (Scientist) into consideration
    def can_turn_in(self):
        pass