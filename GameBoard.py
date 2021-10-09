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
import random

# GameBoard class
class GameBoard(object):

    # - - - SETUP FUNCTIONS - - -
    
    # Constructor -- initializes components of game board based on number of players
    def __init__(self, num_players):

        #Initilize Cities
        self._city_list = dict()
        self.initialize_cities()

        #Initial Research Station in Atlanta
        self._city_list["Atlanta"].has_station = True

        #Initialize Member Data
        self._outbreak_counter = 0
        self._infection_rate_counter = 0
        self._infection_rate = 2

        self._red_cured = False
        self._blue_cured = False
        self._black_cured = False
        self._yellow_cured = False

        self._red_eradicated = False
        self._blue_eradicated = False
        self._black_eradicated = False
        self._yellow_eradicated = False

        self._num_research_stations = 5

        self._player_deck = PlayerDeck()
        self._infection_deck = InfectionDeck()

        self._actions_remaining = 4

        #Initialize Players, gives them a random role, no duplicates
        self._player_list = []
        self._num_players = num_players
        role_list = random.sample(range(1,8), num_players)
        for x in range(num_players):
            self._player_list.append(Player(role_list[x], "Atlanta"))

        #CHECK!
        #Make sure this works once Deck class has been made
        #Infect Cities
        for x in range(9):
            infect_amount = 3 - (x % 3)
            card = self._infection_deck.bottom_card()
            if (card._city._color == "red"):
                card._city._red = infect_amount
            if (card._city._color == "blue"):
                card._city._blue = infect_amount
            if (card._city._color == "black"):
                card._city._black = infect_amount
            if (card._city._color == "yellow"):
                card._city._yellow = infect_amount
            
        #Give Out Cards
        # 2-players = 4, 3-players = 3, 4-players = 2
        num_cards = -(num_players - 2) + 4

        #for x in range(num_cards):

        #Prepare Deck
        self._player_deck.prepare()


        #Should usernames be set up in the main program?
        #self.set_usernames()


    # set_usernames()
    # Sets player usernames to names contained in list of strings
    def set_usernames(self, names_list):
        for x in names_list:
            self._player_list[x]._username = names_list[x]


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

    # initialize_cities()
    # Helper function to initilialize cities
    def initialize_cities():
        city_list = dict()
        city_list["Bogotá"] = City("Bogotá", "yellow",["Miami", "Mexico City", "Lima", "Buenos Aires", "São Paulo"])
        city_list["Johannesburg"] = City("Johannesburg", "yellow",["Kinshasa", "Khartoum"])
        city_list["Buenos Aires"] = City("Buenos Aires", "yellow",["São Paulo", "Bogotá"])
        city_list["Mexico City"] = City("Mexico City", "yellow",["Los Angeles", "Chicago", "Miami", "Bogotá", "Lima"])
        city_list["Lima"] = City("Lima", "yellow",["Mexico City", "Bogotá", "Santiago"])
        city_list["Los Angeles"] = City("Los Angeles", "yellow",["Mexico City", "Chicago", "San Francisco", "Sydney"])
        city_list["Miami"] = City("Miami", "yellow",["Atlanta", "Washington", "Mexico City", "Bogotá"])
        city_list["Kinshasa"] = City("Kinshasa", "yellow",["Lagos", "Khartoum", "Johannesburg"])
        city_list["São Paulo"] = City("São Paulo", "yellow",["Bogotá", "Buenos Aires", "Madrid", "Lagos"])
        city_list["Santiago"] = City("Santiago", "yellow",["Lima"])
        city_list["Khartoum"] = City("Khartoum", "yellow",["Cairo", "Lagos", "Kinshasa", "Johannesburg"])
        city_list["Lagos"] = City("Lagos", "yellow",["São Paulo", "Kinshasa", "Khartoum"])

        city_list["Istanbul"] = City("Istanbul", "black",["Milan", "St. Petersburg", "Moscow", "Baghdad", "Cairo", "Algiers"])
        city_list["Kolkata"] = City("Kolkata", "black",["Delhi", "Chennai", "Bangkok", "Hong Kong"])
        city_list["Tehran"] = City("Tehran", "black",["Moscow", "Baghdad", "Karachi", "Delhi"])
        city_list["Cairo"] = City("Cairo", "black",["Algiers", "Istanbul", "Baghdad", "Riyadh", "Khartoum"])
        city_list["Algiers"] = City("Algiers", "black",["Madrid", "Paris", "Istanbul", "Cairo"])
        city_list["Moscow"] = City("Moscow", "black",["St. Petersburg", "Istanbul", "Tehran"])
        city_list["Chennai"] = City("Chennai", "black",["Mumbai", "Delhi", "Kolkata", "Bangkok", "Jakarta"])
        city_list["Karachi"] = City("Karachi", "black",["Riyadh", "Baghdad", "Tehran", "Delhi", "Mumbai"])
        city_list["Delhi"] = City("Delhi", "black",["Tehran", "Karachi", "Mumbai", "Chennai", "Kolkata"])
        city_list["Mumbai"] = City("Mumbai", "black",["Karachi", "Delhi", "Chennai"])
        city_list["Riyadh"] = City("Riyadh", "black",["Cairo", "Baghdad", "Karachi"])
        city_list["Baghdad"] = City("Baghdad", "black",["Istanbul", "Cairo", "Riyadh", "Karachi", "Tehran"])

        city_list["San Francisco"] = City("San Francisco", "blue",["Tokyo", "Manila", "Los Angeles", "Chicago"])
        city_list["Atlanta"] = City("Atlanta", "blue",["Chicago", "Washington", "Miami"])
        city_list["Madrid"] = City("Madrid", "blue",["New York", "London", "Paris", "Algiers", "São Paulo"])
        city_list["New York"] = City("New York", "blue",["Montréal", "Washington", "Madrid", "London"])
        city_list["Essen"] = City("Essen", "blue",["London", "Paris", "Milan", "St. Petersburg"])
        city_list["Chicago"] = City("Chicago", "blue",["San Francisco", "Los Angeles", "Mexico City", "Atlanta", "Montréal"])
        city_list["St. Petersburg"] = City("St. Petersburg", "blue",["Essen", "Istanbul", "Moscow"])
        city_list["Montréal"] = City("Montréal", "blue",["Chicago", "Washington", "New York"])
        city_list["London"] = City("London", "blue",["New York", "Madrid", "Paris", "Essen"])
        city_list["Paris"] = City("Paris", "blue",["Madrid", "London", "Essen", "Milan", "Algiers"])
        city_list["Milan"] = City("Milan", "blue",["Essen", "Paris", "Istanbul"])
        city_list["Washington"] = City("Washington", "blue",["Miami", "Atlanta", "Montréal", "New York"])

        city_list["Tokyo"] = City("Tokyo", "red",["Seoul", "Shanghai", "Osaka", "San Francisco"])
        city_list["Beijing"] = City("Beijing", "red",["Shanghai", "Seoul"])
        city_list["Shanghai"] = City("Shanghai", "red",["Beijing", "Seoul", "Tokyo", "Hong Kong", "Taipei"])
        city_list["Bangkok"] = City("Bangkok", "red",["Chennai", "Kolkata", "Hong Kong", "Ho Chi Minh City", "Jakarta"])
        city_list["Manila"] = City("Manila", "red",["Ho Chi Minh City", "Hong Kong", "Taipei", "San Francisco", "Sydney"])
        city_list["Ho Chi Minh City"] = City("Ho Chi Minh City", "red",["Jakarta", "Bangkok", "Hong Kong", "Manila"])
        city_list["Sydney"] = City("Sydney", "red",["Jakarta", "Manila", "Los Angeles"])
        city_list["Seoul"] = City("Seoul", "red",["Beijing", "Shanghai", "Tokyo"])
        city_list["Taipei"] = City("Taipei", "red",["Manila", "Hong Kong", "Shanghai", "Osaka"])
        city_list["Jakarta"] = City("Jakarta", "red",["Chennai", "Bangkok", "Ho Chi Minh City", "Sydney"])
        city_list["Osaka"] = City("Osaka", "red",["Taipei", "Tokyo"])
        city_list["Hong Kong"] = City("Hong Kong", "red",["Kolkata", "Shanghai", "Taipei", "Manila", "Ho Chi Minh City", "Bangkok"])

    # - - - GETTER FUNCTIONS - - -

    # Any getter functions that might be necessary...
    # ...
