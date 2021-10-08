# - - - - - - - - - - - - - - - - - - - -
# COP 4521 -- Term Project
# Daniel Fletcher, Connor Klekamp, Jacob Gregie

# PANDEMIC board game implementation
# - - - - - - - - - - - - - - - - - - - -


# * * * GameBoard.py * * *
# GameBoard class
# Encapsulates all data and behavior of the gameplay and board


# Relevant import statements
from Cards import *
from Decks import *
from City import *
from Player import *


# GameBoard class
class GameBoard(object):

    # - - - SETUP FUNCTIONS - - -
    
    # Constructor -- initializes components of game board based on number of players
    def __init__(self, num_players):
        pass

    # set_usernames()
    # Sets player usernames to names contained in list of strings
    def set_usernames(self, names_list):
        pass



    # - - - (1) ACTION PHASE: EIGHT MAIN ACTIONS - - -
    # All actions, when taken, should decrement the actions counter

    # simple_move()
    # Moves a player to a connected city (Drive / Ferry action)
    def simple_move(self):
        pass

    # direct_flight()
    # Player must discard a City card to move to the city named on the card
    def direct_flight(self):
        pass

    # charter_flight()
    # Player must discard the City that matches where they are to move anywhere
    def charter_flight(self):
        pass

    # shuttle_flight()
    # Moves a player from a city with a research station to another city with a research station
    def shuttle_flight(self):
        pass

    # build_station()
    # Builds a research station in the city a player is in, if they discard that city
    # Takes into account special role 2
    def build_station(self):
        pass

    # treat_disease()
    # Removes 1 disease cube of specified color in current city; all cubes if disease is cured
    # Updates cube pools (and possibly, eradicated flags) accordingly
    # Takes into account special role 3
    def treat_disease(self):
        pass

    # share_knowledge()
    # Give or take City card that matches current city
    # Checks for hand limit and responds appropriately, when necessary
    # Takes into account special role 4
    def share_knowledge(self):
        pass

    # discover_cure()
    # Discard 5 City cards of one color at any research station to cure that color
    # If no cubes of that color are on board at this time, make disease eradicated also
    # If all diseases are cured, trigger game end (victory)
    # Takes into account special role 7
    def discover_cure(self):
        pass



    # - - - (2) DRAW CARDS - - -

    # draw_cards()
    # Draws two cards from the Player deck
    # If City/Event card, add to hand (handling hand limit appropriately); if Epidemic, conduct Epidemic
    # If there aren't two cards to draw, trigger game end (defeat)
    def draw_card(self):
        pass

    # epidemic()
    # Causes an epidemic to take place
    # Does all three steps: (1) Increase, (2) Infect, (3) Intensify
    def epidemic(self):
        pass



    # - - - (3) INFECT CITIES - - -

    # draw_infection_card()
    # Draws an infection card from the top of the deck, putting in discard pile
    # Should then call infect_city() on the city specified by the card
    def draw_infection_card(self):
        pass

    # infect_city()
    # Infects a city with the specified number of disease cubes; handles outbreaks appropriately
    # Number of cubes won't be 1 during setup and for 2 - INFECT phases of Epidemics
    # Take into account cured/eradicated diseases, along with special roles (like 3 and 6)
    # If there aren't enough cubes to infect a city, trigger game end (defeat)
    def infect_city(self, city_name, num_cubes = 1):
        pass

    # outbreak_in_city()
    # Triggers an outbreak in a given city
    # If additional outbreaks occur, this outbreak should finish first
    # If the outbreak tracker reaches 8, trigger game end (defeat)
    def outbreak_in_city(self, city_name):
        pass



    # - - - SPECIAL ROLES & ACTIONS - - -

    # contingency_planner_take()
    # Takes an Event card from the discard pile, according to Role rules
    def contingency_planner_take(self):
        pass 

    # dispatcher_move_other()
    # Move another player's pawn
    def dispatcher_move_other(self):
        pass 

    # dispatcher_move_p2p()
    # Move one player to another player ("player 2 player")
    def dispatcher_move_p2p(self):
        pass 

    # operations_expert_move()
    # Move from research station to any city by discarding any Card
    def operations_expert_move(self):
        pass 



    # - - - EVENT CARDS - - -

    # one_quiet_night()
    # Does Event card #1 -- One Quiet Night
    def one_quiet_night(self):
        pass

    # forecast()
    # Does Event card #2 -- Forecast
    def forecast(self):
        pass

    # government_grant()
    # Does Event card #3 -- Government Grant
    def government_grant(self):
        pass

    # airlift()
    # Does Event card #4 -- Airlift
    def airlift(self):
        pass

    # resilient_population()
    # Does Event card #5 -- One Quiet Night
    def resilient_population(self):
        pass



    # - - - MISCELLANEOUS GAMEPLAY FUNCTIONS - - -

    # next_turn()
    # Advances the turn counter and resets number of actions remaining
    # Captures the current state of the board as member data for use with reset()
    def next_turn(self):
        pass

    # reset()
    # Resets the state of the board to the way it was before a player took actions that turn
    # Only allowed during action phase of turn
    def reset(self):
        pass

    # discard()
    # Allows the player to discard when they have gone over the hand limit
    def discard(self):
        pass



    # - - - GETTER FUNCTIONS - - -

    # Any getter functions that might be necessary...
    # ...
