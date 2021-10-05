# - - - - - - - - - - - - - - - - - - - -
# COP 4521 -- Term Project
# Daniel Fletcher, Connor Klekamp, Jacob Gregie
# PANDEMIC board game implementation
# - - - - - - - - - - - - - - - - - - - -


# * * * Decks.py * * *
# Card deck inheritance hierarchy
# Base "Deck" class
# Derived "InfectionDeck" and "PlayerDeck" classes
# Separation allows for unique and convenient constructor calls


# Relevant import statements
from Cards import *


# Deck class
# Contains general card deck behavior and attributes
class Deck(object):

    # Default constructor (should only be called by derived class constructors)
    def __init__(self):
        self._cardlist = list()

    # shuffle()
    # Shuffle cards in the deck
    def shuffle(self):
        pass

    # top_card()
    # Returns the top card from the deck, removing it from the deck in the process
    def top_card(self):
        pass

    # get_size()
    # Returns the size of the deck
    def get_size():
        pass

    # is_empty()
    # Returns True if the deck is empty, False otherwise
    def is_empty():
        pass


# InfectionDeck class
# Contains Infection cards and behavior unique to Infection deck
class InfectionDeck(Deck):

    # Default constructor
    # Initializes 48 Infection cards with appropriate city names and colors
    def __init__(self):
        # First, call parent constructor
        super().__init__()

        # ...

        # Shuffle the deck
        super().shuffle()

    # bottom_card()
    # Returns the bottom card from the deck, removing it from the deck in the process
    # Occurs during 2 - INFECT phase of Epidemics
    def bottom_card(self):
        pass

    # intensify()
    # Reshuffles cards from Infection discard, adds them back to TOP of Infection deck
    # Occurs during 3 - INTENSIFY phase of Epidemics
    def intensify(self, discard_pile):
        pass


# PlayerDeck class
# Contains Player cards and behavior unique to Player deck
class PlayerDeck(Deck):

    # Default constructor
    # Initializes 48 City cards (w/ population data), 5 Event cards (NO Epidemic cards yet)
    def __init__(self):
        # First, call parent constructor
        super().__init__()

        # ...

        # Shuffle the deck
        super().shuffle()

    # prepare()
    # Adds 4, 5, or 6 Epidemic cards to the deck (based on parameter)
    # Shuffles deck according to Step 5 of game setup
    def prepare(self, num_epidemics):
        pass
