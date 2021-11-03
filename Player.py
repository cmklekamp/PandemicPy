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
        self._playerhand = list()
        self._role = role_num
        self._current_city = starting_city
        self._username = ""
        self._contingency_planner_card = EventCard(0)

        # Setting player color based on role number.
        # This should make later GUI syntax a little more readable.
        if role_num == 1:
            self._player_color = "pink"
        elif role_num == 2:
            self._player_color = "light green"
        elif role_num == 3:
            self._player_color = "orange"
        elif role_num == 4:
            self._player_color = "brown"
        elif role_num == 5:
            self._player_color = "light blue"
        elif role_num == 6:
            self._player_color = "dark green"
        elif role_num == 7:
            self._player_color = "white"
       

    # - - - GETTER FUNCTIONS - - -
    # get_username() 
    @property
    def username(self):
        return self._username

    @property
    def playerhand(self):
        return self._playerhand

    @property
    def role(self):
        return self._role

    @property
    def current_city(self):
        return self._current_city

    @property
    def contingency_planner_card(self):
        return self._contingency_planner_card

    # - - - SETTER FUNCTIONS - - -
    # set_username()
    # Sets the player's username to the given parameter
    @username.setter
    def username(self, username):
        self._username = username

    @contingency_planner_card.setter
    def contingency_planner_card(self, card):
        self._contingency_planner_card = card
    
    @current_city.setter
    def current_city(self, city):
        self._current_city = city

    # acquire_card()
    # Adds a card to the player's hand
    def acquire_card(self, card):
        self._playerhand.append(card)

    # discard()
    # Takes in a card and discards it from the player's hand
    # Returns true if the card was able to be found and discarded, otherwise false
    def discard(self, card):
        for x in self._playerhand:
            if x == card:
                self._playerhand.remove(card)
                return True
        return False

    # over_hand_limit()
    # Returns True if the player has more than 7 cards in hand; False otherwise
    def over_hand_limit(self):
        if len(self._playerhand) > 7:
            return True
        else:
            return False

    # can_turn_in()
    # Returns True if the player can turn in a set; False otherwise
    # Takes special case of Role #7 (Scientist) into consideration
    def can_turn_in(self):
        if self._current_city.has_station():
            # Counters that will be used to count the number of cards of each color the player holds.
            yellowCounter = 0
            blackCounter = 0
            blueCounter = 0
            redCounter = 0
            # Counter that holds the number a player needs to successfully turn in the set.
            goal = 5

            # Increments the counters as the hand is checked.
            for x in self._playerhand:
                if x.color == "yellow":
                    yellowCounter += 1
                elif x.color == "black":
                    blackCounter += 1
                elif x.color == "blue":
                    blueCounter += 1
                else:
                    redCounter += 1
            
            # Goal decreases by one if the player is the Scientist.
            if self._role == 7:
                goal -= 1

            # Final check.
            if yellowCounter >= goal or blackCounter >= goal or blueCounter >= goal or redCounter >= goal:
                return True
            else:
                return False
        else:
            return False