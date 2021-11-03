#Check!
# Allow resilient population to be played in between infect and intensify step
# check if a player passes hand limit in main so that they can choose cards to discard or use
# in main, don't let players use event cards after the last infection card is drawn, just move to next turn
#   the reason is because one quiet night is reset in the next turn function, also from the players perspective
#   it doesn't make a difference


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
import copy

# GameBoard class
class GameBoard(object):

    # - - - SETUP FUNCTIONS - - -
    
    # Constructor -- initializes components of game board based on number of players, list of usernames, and difficulty level
    def __init__(self, num_players, names_list, difficulty = 4):

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

        self._red_remaining = 24
        self._blue_remaining = 24
        self._black_remaining = 24
        self._yellow_remaining = 24

        #Accounts for the initial station
        self._research_stations_remaining = 5

        self._player_deck = PlayerDeck()
        self._infection_deck = InfectionDeck()

        self._actions_remaining = 4
        self._player_turn = 1

        #discard pile of card objects for each type of card
        self._infection_discard_pile = []
        self._player_discard_pile = []

        #flags for victory or defeat
        self._victory = False
        self._defeat = False

        #flag for use by One Quiet Night event card
        self._skip_infect_cities = False

        # counter for whether or not an epidemic is currently happening
        # used in main to signal whether or not epidemic should be called after drawing cards
        # counter instead of flag for the case that 2 epidemic cards are drawn during a single draw phase
        # reduced by 1 after the intensify step of the epidemic
        self._epidemics_occuring = 0

        #Initilize Cities
        self._city_list = dict()
        self.initialize_cities()

        #Initial Research Station in Atlanta
        self._city_list["Atlanta"].add_station()

        #Initialize Players, gives them a random role, no duplicates
        self._player_list = list()
        self._num_players = num_players
        role_list = random.sample(range(1,8), num_players)
        for x in range(num_players):
            self._player_list.append(Player(role_list[x], "Atlanta"))

        # list of the cities that the quarantine specialist is connected to so they won't be infected
        # initializes as empty so it won't take effect in the setup phase
        self._quarantine_list = list()

        #Infect Cities  
        for x in range(9):
            infect_amount = 3 - (x // 3)
            card = self._infection_deck.top_card()
            self.infect_city(card.city, card.color, infect_amount)
            self._infection_discard_pile.append(card)

        # updates the list of the cities that the quarantine specialist is connected to so they won't be infected
        # if there is no quarantine specialist, the quarantine list will be empty for the rest of the game
        for x in self._player_list:
            if (x.role == 6):
                self._quarantine_list = self._city_list[x.current_city].connected_cities

        # Sets player usernames to names contained in list of strings 
        for x in range(len(names_list)):
            self._player_list[x].username = names_list[x]
            
        # Give Out Cards
        # 2-players = 4, 3-players = 3, 4-players = 2  
        num_cards = -(num_players - 2) + 4
        highest_population = 0
        for x in self._player_list:
            for y in range(num_cards):
                card = self._player_deck.top_card()
                x.acquire_card(card)

                #determines who has the card with the highest population
                if (isinstance(card, CityCard) and card.population > highest_population):
                    highest_population = card.population
                    first_player = x

        # Re-order players based on who has the card with the highest population
        #   moves the last player to the front until the front player is the one with the highest population
        while (self._player_list[0] != first_player):
            self._player_list.insert(0, self._player_list.pop())
        
        #Prepare Deck
        self._player_deck.prepare(difficulty)

        #set up temp_board in case there needs to be a turn reset
        self._temp_board = self

    # - - - (1) ACTION PHASE: EIGHT MAIN ACTIONS - - -
    # All actions, when taken, should decrement the actions counter

    # simple_move()
    # Moves a player to a connected city (Drive / Ferry action)
    def simple_move(self, player, city_name):

        #moves the current player if the city requested is connected to the current city
        if (city_name in self._city_list[player.current_city].connected_cities):
            player.current_city = city_name
            self._actions_remaining -= 1

            # medic passive check
            if (player.role == 3):
                self.medic_passive(city_name)

            return True                    
        else:
            return False


    # direct_flight()
    # Player must discard a City card to move to the city named on the card
    def direct_flight(self, player, city_name):

        #Check!
        #Do I need to use type coercion here?
        #check if the card is in the players hand
        card = CityCard("", "", 0, 0)
        for x in player.playerhand:
            if (isinstance(x, CityCard) and x.city == city_name):
                card = x

        if (card.city != ""):
            self._player_discard_pile.append(card)
            player.discard(card)
            player.current_city = city_name
            self._actions_remaining -= 1

            # medic passive check
            if (player.role == 3):
                self.medic_passive(city_name)

            return True
        else:
            return False

    # charter_flight()
    # Player must discard the City that matches where they are to move anywhere
    def charter_flight(self, player, city_name):

        #check if the card is in the players hand
        card = CityCard("", "", 0, 0)
        for x in player.playerhand:
            if (isinstance(x, CityCard) and x.city == player.current_city):
                card = x

        if (card.city != ""):
            self._player_discard_pile.append(card)
            player.discard(card)
            player.current_city = city_name
            self._actions_remaining -= 1

            # medic passive check
            if (player.role == 3):
                self.medic_passive(city_name)

            return True
        else:
            return False

    # shuttle_flight()
    # Moves a player from a city with a research station to another city with a research station
    def shuttle_flight(self, player, city_name):

        if (city_name in self._city_list and self._city_list[player.current_city].has_station
                and self._citylist[city_name].has_station):
            player.current_city = city_name
            self._actions_remaining -= 1

            # medic passive check
            if (player.role == 3):
                self.medic_passive(city_name)

            return True
        else:
            return False
            
    # build_station()
    # Builds a research station in the city a player is in, if they discard that city
    # Takes into account special role 2
    def build_station(self):

        #return false if no more remaining stations        
        if (self._research_stations_remaining == 0):
                return False

        player = self.get_current_player()

        #check if player is operations expert      
        if (player.role == 2):
            if (self._city_list.add_station() == False):
                return False
            else:
                self._actions_remaining -= 1
                return True

        #check if the player has the current city card
        else:
            #check if the card is in the players hand
            card = CityCard("", "", 0, 0)
            for x in player.playerhand:
                if (isinstance(x, CityCard) and x.city == player.current_city):
                    card = x

            if (card.city != ""):
                if (self._city_list[card.city].add_station() == False):
                    return False
                else:
                    self._player_discard_pile.append(card)
                    player.discard(card)
                    self._actions_remaining -= 1
                    return True
            else:
                return False

    # treat_disease()
    # Removes 1 disease cube of specified color in current city; all cubes if disease is cured
    # Updates cube pools (and possibly, eradicated flags) accordingly
    # Takes into account special role 3
    def treat_disease(self, color):

        player = self.get_current_player()
        city = self._city_list[player.current_city]

        if (color == "red"):
            #return if the selected color can't be treated
            if (city.red == 0):
                return False

            #remove all cubes if the disease is cured or if the player is the medic
            if (self._red_cured or player.role == 3):
                while (city.remove_cube("red") == True):
                    self._red_remaining += 1

                #eradicate if necessary
                if (self._red_cured and self._red_remaining == 24):
                    self._red_eradicated = True

            #remove one cube            
            else:
                city.remove_cube("red")
                self._red_remaining += 1

        elif (color == "blue"):
            if (city.blue == 0):
                return False

            if (self._blue_cured or player.role == 3):
                while (city.remove_cube("blue") == True):
                    self._blue_remaining += 1

                if (self._blue_cured and self._blue_remaining == 24):
                    self._blue_eradicated = True

            else:
                city.remove_cube("blue")
                self._blue_remaining += 1

        elif (color == "black"):
            if (city.black == 0):
                return False

            if (self._black_cured or player.role == 3):
                while (city.remove_cube("black") == True):
                    self._black_remaining += 1

                if (self._black_cured and self._black_remaining == 24):
                    self._black_eradicated = True
            else:
                city.remove_cube("black")
                self._black_remaining += 1

        elif (color == "yellow"):
            if (city.yellow == 0):
                return False

            if (self._yellow_cured or player.role == 3):
                while (city.remove_cube("yellow") == True):
                    self._yellow_remaining += 1

                if (self._yellow_cured and self._yellow_remaining == 24):
                    self._yellow_eradicated = True
            else:
                city.remove_cube("yellow")
                self._yellow_remaining += 1

        else:
            return False

        self.actions_remaining -= 1
        return True

    # share_knowledge()
    # Give or take City card that matches current city
    # The first player in the parameter list is always the one giving the card
    # In main, check to see if hand limit reached so you can discard city cards or use event cards
    # Takes into account special role 4
    def share_knowledge(self, giving_player, taking_player, card_name):

        #check if the card is in the players hand
        card = CityCard("", "", 0, 0)
        for x in giving_player.playerhand:
            if (isinstance(x, CityCard) and x.city == card_name):
                card = x
        
        #return false if the giving player doesn't have the card or players aren't in the same city
        if (card.city == "" or giving_player.current_city != taking_player.current_city):
            return False
        
        #exchange cards if the giving player is the researcher or the card matches current city
        if (giving_player.role == 4 or giving_player.current_city == card_name):
            taking_player.acquire_card(card)
            giving_player.discard(card)
            self._actions_remaining -= 1
            return True

        else:
            return False    

    # discover_cure()
    # Discard 5 City cards of one color at any research station to cure that color
    # pass in the color being discovered, and the list of cards being discarded
    # If no cubes of that color are on board at this time, make disease eradicated also
    # If all diseases are cured, trigger game end (victory)
    # Takes into account special role 7
    def discover_cure(self, color, discard_list):

        player = self.get_current_player()

        if (self._city_list[player.current_city].has_station == False):
            return False

        for x in discard_list:
            if (discard_list[x].color != color or discard_list[x] not in player.playerhand):
                return False

        if (len(discard_list) == 5 or (player.role == 7 and len(discard_list) == 4)):
            if (color == "red"):
                if (self._red_cured):
                    return False
                self._red_cured = True
                if (self._red_remaining == 24):
                    self._red_eradicated = True
            
            elif (color == "blue"):
                if (self._blue_cured):
                    return False
                self._blue_cured = True
                if (self._blue_remaining == 24):
                    self._blue_eradicated = True

            elif (color == "black"):
                if (self._black_cured):
                    return False
                self._black_cured = True
                if (self._black_remaining == 24):
                    self._black_eradicated = True

            elif (color == "yellow"):
                if (self._yellow_cured):
                    return False
                self._yellow_cured = True
                if (self._yellow_remaining == 24):
                    self._yellow_eradicated = True

            else:
                return False
        else:
            return False

        #discard the cards
        for x in discard_list:
            self._player_discard_pile.append(discard_list[x])
            player.discard(discard_list[x])
        
        self.actions_remaining -= 1

        #Check win condition
        if (self._red_cured and self._blue_cured and self._black_cured and self._yellow_cured):
            self.game_end(True)

        return True

    # - - - (2) DRAW CARDS - - -

    # draw_cards()
    # Draws two cards from the Player deck
    # If City/Event card, add to hand (if over the hand limit, handle in main after drawing 2 cards); if Epidemic, conduct Epidemic
    # If there aren't two cards to draw, trigger game end (defeat)
    def draw_cards(self):

        if (self._player_deck.get_size() < 2):
            self.game_end(False)
            return False

        player = self.get_current_player()

        for x in range(2):
            card = self._player_deck.top_card()
            if (isinstance(card, CityCard) or isinstance(card, EventCard)):
                player.acquire_card(card)
            else:
                self._epidemics_occuring += 1
        return True

    # epidemic()
    # Causes an epidemic to take place
    # Does the first two steps: (1) Increase, (2) Infect
    # After calling this function, allow players to play the resilient population card if they have it,
    #  then call intensify()
    def epidemic(self):
        
        # (1) increase
        self._infection_rate = (self._infection_rate_counter // 2) + 2
        self._infection_rate_counter += 1
        
        # (2) infect
        # updates the list of the cities that the quarantine specialist is connected to so they won't be infected
        # skips if there is no quarantine specialist
        if not self._quarantine_list:
            for x in self._player_list:
                if (x.role == 6):
                    self._quarantine_list = self._city_list[x.current_city].connected_cities

        card = self._infection_deck.bottom_card()
        self._infection_discard_pile.append(card)
        self.infect_city(card.city, card.color, 3)
    
    # intensify()
    # Does the third step of an epidemic
    def intensify(self):
        self._infection_deck.intensify(self._infection_discard_pile)
        self._infection_discard_pile.clear()
        self._epidemics_occuring -= 1

    # - - - (3) INFECT CITIES - - -

    # draw_infection_card()
    # Draws an infection card from the top of the deck, putting in discard pile
    # Should then call infect_city() on the city specified by the card
    def draw_infection_card(self):

        #if one quiet night is active, don't draw any cards
        if (self._skip_infect_cities == True):
            return
        
        # updates the list of the cities that the quarantine specialist is connected to so they won't be infected
        # skips if there is no quarantine specialist in the game
        if not self._quarantine_list:
            for x in self._player_list:
                if (x.role == 6):
                    self._quarantine_list = self._city_list[x.current_city].connected_cities

        card = self._infection_deck.top_card()
        self._infection_discard_pile.append(card)
        self.infect_city(card.city, card.color)

        for x in self._city_list:
            self._city_list[x].had_outbreak = False

    # infect_city()
    # Infects a city with the specified number of disease cubes; handles outbreaks appropriately
    # Number of cubes won't be 1 during setup and for 2 - INFECT phases of Epidemics
    # Take into account cured/eradicated diseases, along with special roles (like 3 and 6)
    # If there aren't enough cubes to infect a city, trigger game end (defeat)
    def infect_city(self, city_name, color, num_cubes = 1):
        
        # skip this function if a game over condition has already been met, saves a little time
        if (self._defeat == True):
            return
        
        for x in self.player_list:
            # don't infect if quarantine specialist is in the city or a connected city
            if (x.role == 6 and (x.current_city == city_name or city_name in self._quarantine_list)):
                return

            # don't infect if the medic is in the city and the disease has been cured
            if (x.role == 3 and x.current_city == city_name):
                if (color == "red" and self._red_cured == True):
                    return
                if (color == "blue" and self._blue_cured == True):
                    return
                if (color == "black" and self._black_cured == True):
                    return
                if (color == "yellow" and self._yellow_cured == True):
                    return

        if (color == "red" and self._red_eradicated == False):
            for x in range(int(num_cubes)):

                # only increment red_remaining if a cube was successfully added (i.e. no outbreak happened)               
                flag = self._city_list[city_name].add_cube("red")
                if (flag == True):
                    self._red_remaining -= 1

                # cause outbreak of the disease color that is being increased
                else:
                    self.outbreak_in_city(city_name, color)   

                # check lose condition
                if (self._red_remaining < 0):
                    self.game_end(False)

        elif (color == "blue" and self._blue_eradicated == False):
            for x in range(int(num_cubes)): 

                flag = self._city_list[city_name].add_cube("blue")
                if (flag == True):
                    self._blue_remaining -= 1

                else:
                    self.outbreak_in_city(city_name, color)    

                if (self._blue_remaining < 0):
                   self.game_end(False)

        elif (color == "black" and self._black_eradicated == False):
            for x in range(int(num_cubes)): 

                flag = self._city_list[city_name].add_cube("black")
                if (flag == True):
                    self._black_remaining -= 1

                else:
                    self.outbreak_in_city(city_name, color)  

                if (self._black_remaining < 0):
                   self.game_end(False)

        elif (color == "yellow" and self._yellow_eradicated == False):
            for x in range(int(num_cubes)):   

                flag = self._city_list[city_name].add_cube("yellow")
                if (flag == True):
                    self._yellow_remaining -= 1

                else:
                    self.outbreak_in_city(city_name, color)     

                if (self._yellow_remaining < 0):
                   self.game_end(False)

    # outbreak_in_city()
    # Triggers an outbreak in a given city
    # If additional outbreaks occur, this outbreak should finish first
    # If the outbreak tracker reaches 8, trigger game end (defeat)
    def outbreak_in_city(self, city_name, color):

        # skips the outbreak if the city already had one, or if the game has been lost
        if (self._city_list[city_name].had_outbreak == False and self._defeat == False):
            self._outbreak_counter += 1
            if (self._outbreak_counter >= 8):
                self.game_end(False)
                return

            # prevent future outbreaks from happening to this city
            # resets after each infection card is drawn
            self._city_list[city_name].had_outbreak = True
            
            # recursively go through all the connected cities, if infect_city calls
            #  for an outbreak in a city that already had one, it will skip the outbreak
            #  for that city
            for x in self._city_list[city_name].connected_cities:

                #infect the city with the color of the original disease that started the outbreak
                self.infect_city(x, color)                   

    # - - - SPECIAL ROLES & ACTIONS - - -

    # contingency_planner_take()
    # Takes an Event card from the discard pile, according to Role rules
    def contingency_planner_take(self, card):
        
        player = self.get_current_player()

        if (player.role == 5 and isinstance(card, EventCard) and card in self._player_discard_pile):
            player.contingency_planner_card.value = card.value
            self._player_discard_pile.remove(card)
            self._actions_remaining -= 1
            return True
        else:
            return False     

    # dispatcher_simple_move()
    # Move another player's pawn to city_name as if it were your own
    def dispatcher_simple_move(self, moving_player, city_name):  
        if (self.get_current_player().role == 1):
            return self.simple_move(moving_player, city_name)
        else:
            return False

    # dispatcher_direct_flight()
    # Move another player's pawn to city_name as if it were your own
    def dispatcher_direct_flight(self, moving_player, city_name):
        
        dispatcher = self.get_current_player()
        if (dispatcher.role != 1):
            return False

        #check if the card is in the players hand
        card = CityCard("", "", 0, 0)
        for x in dispatcher.playerhand:
            if (isinstance(x, CityCard) and x.city == city_name):
                card = x

        if (card.city != ""):
            self._player_discard_pile.append(card)
            dispatcher.discard(card)
            moving_player.current_city = city_name
            self._actions_remaining -= 1

            # medic passive check
            if (moving_player.role == 3):
                self.medic_passive(city_name)

            return True
        else:
            return False

    # dispatcher_charter_flight()
    # Move another player's pawn as if it were your own
    def dispatcher_charter_flight(self, moving_player, city_name,):

        dispatcher = self.get_current_player()
        if (dispatcher.role != 1):
            return False

        #check if the card is in the players hand
        card = CityCard("", "", 0, 0)
        for x in dispatcher.playerhand:
            if (isinstance(x, CityCard) and x.city == moving_player.current_city):
                card = x

        if (card.city != ""):
            self._player_discard_pile.append(card)
            dispatcher.discard(card)
            moving_player.current_city = city_name
            self._actions_remaining -= 1

            # medic passive check
            if (moving_player.role == 3):
                self.medic_passive(city_name)

            return True
        else:
            return False

    # dispatcher_shuttle_flight()
    # Move another player's pawn as if it were your own
    def dispatcher_shuttle_flight(self, moving_player, city_name):
        if (self.get_current_player().role == 1):
            return self.shuttle_flight(moving_player, city_name)
        else:
            return False

    # dispatcher_move_p2p()
    # Move one player to another player ("player 2 player")
    # player1 is always the player that is moving
    def dispatcher_move_p2p(self, player1, player2):

        # make sure we are dealing with real people and not frauds
        if (player1 not in self._player_list or player2 in self._player_list):
            return False

        player1.current_city = player2.current_city
        self._actions_remaining -= 1

        # medic passive check
        if (player1.role == 3):
            self.medic_passive(player1.current_city)

        return True

    # operations_expert_move()
    # Move from research station to any city by discarding any Card
    def operations_expert_move(self, card, city_name):

        player = self.get_current_player()

        if (player.role == 2 and card in player.playerhand and city_name in self._city_list 
                and self.city_list[player.current_city].has_station):
            self._player_discard_pile.append(card)
            player.discard(card)
            player.current_city = city_name
            self._actions_remaining -= 1
            return True
        else:
            return False

    # - - - EVENT CARDS - - -

    # one_quiet_night()
    # Does Event card #1 -- One Quiet Night
    def one_quiet_night(self, player):

        if (self.event_card_check(player, 1) == False):
            return False

        self._skip_infect_cities == True   
        return True

    # forecast()
    # Does Event card #2 -- Forecast
    # the last card in the top_six array will be on the top of the deck after the event is done
    def forecast(self, player, top_six):
        
        if (self.event_card_check(player, 2) == False):
            return False

        self._infection_deck.cardlist.extend(top_six)   
        return True

    # government_grant()
    # Does Event card #3 -- Government Grant
    # pass in the player using the card and where they are building the station
    def government_grant(self, player, city_name):

        if (city_name not in self._city_list or self._research_stations_remaining == 0 or self._city_list[city_name].has_station):
            return False

        if (self.event_card_check(player, 3) == False):
            return False

        self._city_list[city_name].add_station()
        self._research_stations_remaining -= 1         
        return True

    # airlift()
    # Does Event card #4 -- Airlift
    def airlift(self, card_player, moving_player, city_name):

        if (city_name not in self._city_list):
            return False

        if (self.event_card_check(card_player, 4) == False):
            return False

        # update the current city of the player that moved
        moving_player.current_city = city_name

        # medic passive check
        if (moving_player.role == 3):
            self.medic_passive(city_name)
     
        return True

    # resilient_population()
    # Does Event card #5 -- Resilient Population
    def resilient_population(self, player, card_to_discard):
        
        if (card_to_discard not in self._infection_discard_pile):
            return False
        
        if (self.event_card_check(player, 5) == False):
            return False

        self._infection_discard_pile.remove(card_to_discard)
        return True

    # - - - MISCELLANEOUS GAMEPLAY FUNCTIONS - - -

    # next_turn()
    # Advances the turn counter and resets number of actions remaining
    # Captures the current state of the board as member data for use with reset()
    def next_turn(self):
        self._actions_remaining = 4

        self._skip_infect_cities == False

        if (self._player_turn == len(self._player_list)):
            self._player_turn = 1
        else:
            self._player_turn += 1

        self._temp_board = self

    # reset()
    # Resets the state of the board to the way it was before a player took actions that turn
    # Only allowed during action phase of turn
    # Check!
    # Should we allow this to work with 0 actions in case they didn't want to make their last move?
    #  we could add a boolean that is updated in the draw card function called in_action_phase
    def reset(self):
        if (self._actions_remaining > 0):
            self = self._temp_board
            return True
        else:
            return False

    # discard()
    # Allows the player to discard when they have gone over the hand limit
    def discard(self, card):
        player = self.get_current_player()
        if (player.over_hand_limit()):
            self._player_discard_pile.append(card)
            player.discard(card)
            return True
        else:
            return False

    # remove_station()
    # removes station if the remaining stations is 0
    def remove_station(self, city_name):
        if (self.research_stations_remaining == 0 and self.city_list[city_name].remove_station()):
            self._research_stations_remaining += 1
            return True
        else:
            return False

    # game_end()
    # ends the game based on if it was a victory or a defeat
    def game_end(self, victory):
        if (victory == True):
            self._victory = True
        else:
            self._defeat = True

    # medic_passive()
    # Checks for the medics passive, removes cubes if a disease is cured
    def medic_passive(self, city_name):
        city = self._city_list[city_name]
        if (self._red_cured):
            while (city.remove_cube("red") == True):
                self._red_remaining += 1
        if (self._blue_cured):
            while (city.remove_cube("blue") == True):
                self._blue_remaining += 1
        if (self._black_cured):
            while (city.remove_cube("black") == True):
                self._black_remaining += 1
        if (self._yellow_cured):
            while (city.remove_cube("yellow") == True):
                self._yellow_remaining += 1
    
    # event_card_check()
    # helper function, checks if the player has an event card and whether or not it is the contingency_planner_card
    def event_card_check(self, player, number):
        has_card = False
        using_contingency_card = False

        if (player.contingency_planner_card.value == number):
            has_card = True
            using_contingency_card = True

        else:
            for x in player.playerhand:
                if (isinstance(x, EventCard) and x.value == number):
                    has_card = True
                    card = x

        # only discard if the card is not the contingency_planner_card           
        if (has_card == True): 
            if (using_contingency_card == False):
                player.discard(card)
                self._player_discard_pile.append(card)
            else:
                player.contingency_planner_card.value = 0

        return has_card

    # initialize_cities()
    # Helper function to initilialize cities
    def initialize_cities(self):
        self._city_list["Bogotá"] = City("Bogotá", "yellow",["Miami", "Mexico City", "Lima", "Buenos Aires", "São Paulo"])
        self._city_list["Johannesburg"] = City("Johannesburg", "yellow",["Kinshasa", "Khartoum"])
        self._city_list["Buenos Aires"] = City("Buenos Aires", "yellow",["São Paulo", "Bogotá"])
        self._city_list["Mexico City"] = City("Mexico City", "yellow",["Los Angeles", "Chicago", "Miami", "Bogotá", "Lima"])
        self._city_list["Lima"] = City("Lima", "yellow",["Mexico City", "Bogotá", "Santiago"])
        self._city_list["Los Angeles"] = City("Los Angeles", "yellow",["Mexico City", "Chicago", "San Francisco", "Sydney"])
        self._city_list["Miami"] = City("Miami", "yellow",["Atlanta", "Washington", "Mexico City", "Bogotá"])
        self._city_list["Kinshasa"] = City("Kinshasa", "yellow",["Lagos", "Khartoum", "Johannesburg"])
        self._city_list["São Paulo"] = City("São Paulo", "yellow",["Bogotá", "Buenos Aires", "Madrid", "Lagos"])
        self._city_list["Santiago"] = City("Santiago", "yellow",["Lima"])
        self._city_list["Khartoum"] = City("Khartoum", "yellow",["Cairo", "Lagos", "Kinshasa", "Johannesburg"])
        self._city_list["Lagos"] = City("Lagos", "yellow",["São Paulo", "Kinshasa", "Khartoum"])

        self._city_list["Istanbul"] = City("Istanbul", "black",["Milan", "St. Petersburg", "Moscow", "Baghdad", "Cairo", "Algiers"])
        self._city_list["Kolkata"] = City("Kolkata", "black",["Delhi", "Chennai", "Bangkok", "Hong Kong"])
        self._city_list["Tehran"] = City("Tehran", "black",["Moscow", "Baghdad", "Karachi", "Delhi"])
        self._city_list["Cairo"] = City("Cairo", "black",["Algiers", "Istanbul", "Baghdad", "Riyadh", "Khartoum"])
        self._city_list["Algiers"] = City("Algiers", "black",["Madrid", "Paris", "Istanbul", "Cairo"])
        self._city_list["Moscow"] = City("Moscow", "black",["St. Petersburg", "Istanbul", "Tehran"])
        self._city_list["Chennai"] = City("Chennai", "black",["Mumbai", "Delhi", "Kolkata", "Bangkok", "Jakarta"])
        self._city_list["Karachi"] = City("Karachi", "black",["Riyadh", "Baghdad", "Tehran", "Delhi", "Mumbai"])
        self._city_list["Delhi"] = City("Delhi", "black",["Tehran", "Karachi", "Mumbai", "Chennai", "Kolkata"])
        self._city_list["Mumbai"] = City("Mumbai", "black",["Karachi", "Delhi", "Chennai"])
        self._city_list["Riyadh"] = City("Riyadh", "black",["Cairo", "Baghdad", "Karachi"])
        self._city_list["Baghdad"] = City("Baghdad", "black",["Istanbul", "Cairo", "Riyadh", "Karachi", "Tehran"])

        self._city_list["San Francisco"] = City("San Francisco", "blue",["Tokyo", "Manila", "Los Angeles", "Chicago"])
        self._city_list["Atlanta"] = City("Atlanta", "blue",["Chicago", "Washington", "Miami"])
        self._city_list["Madrid"] = City("Madrid", "blue",["New York", "London", "Paris", "Algiers", "São Paulo"])
        self._city_list["New York"] = City("New York", "blue",["Montréal", "Washington", "Madrid", "London"])
        self._city_list["Essen"] = City("Essen", "blue",["London", "Paris", "Milan", "St. Petersburg"])
        self._city_list["Chicago"] = City("Chicago", "blue",["San Francisco", "Los Angeles", "Mexico City", "Atlanta", "Montréal"])
        self._city_list["St. Petersburg"] = City("St. Petersburg", "blue",["Essen", "Istanbul", "Moscow"])
        self._city_list["Montréal"] = City("Montréal", "blue",["Chicago", "Washington", "New York"])
        self._city_list["London"] = City("London", "blue",["New York", "Madrid", "Paris", "Essen"])
        self._city_list["Paris"] = City("Paris", "blue",["Madrid", "London", "Essen", "Milan", "Algiers"])
        self._city_list["Milan"] = City("Milan", "blue",["Essen", "Paris", "Istanbul"])
        self._city_list["Washington"] = City("Washington", "blue",["Miami", "Atlanta", "Montréal", "New York"])

        self._city_list["Tokyo"] = City("Tokyo", "red",["Seoul", "Shanghai", "Osaka", "San Francisco"])
        self._city_list["Beijing"] = City("Beijing", "red",["Shanghai", "Seoul"])
        self._city_list["Shanghai"] = City("Shanghai", "red",["Beijing", "Seoul", "Tokyo", "Hong Kong", "Taipei"])
        self._city_list["Bangkok"] = City("Bangkok", "red",["Chennai", "Kolkata", "Hong Kong", "Ho Chi Minh City", "Jakarta"])
        self._city_list["Manila"] = City("Manila", "red",["Ho Chi Minh City", "Hong Kong", "Taipei", "San Francisco", "Sydney"])
        self._city_list["Ho Chi Minh City"] = City("Ho Chi Minh City", "red",["Jakarta", "Bangkok", "Hong Kong", "Manila"])
        self._city_list["Sydney"] = City("Sydney", "red",["Jakarta", "Manila", "Los Angeles"])
        self._city_list["Seoul"] = City("Seoul", "red",["Beijing", "Shanghai", "Tokyo"])
        self._city_list["Taipei"] = City("Taipei", "red",["Manila", "Hong Kong", "Shanghai", "Osaka"])
        self._city_list["Jakarta"] = City("Jakarta", "red",["Chennai", "Bangkok", "Ho Chi Minh City", "Sydney"])
        self._city_list["Osaka"] = City("Osaka", "red",["Taipei", "Tokyo"])
        self._city_list["Hong Kong"] = City("Hong Kong", "red",["Kolkata", "Shanghai", "Taipei", "Manila", "Ho Chi Minh City", "Bangkok"])

    # - - - GETTER FUNCTIONS - - -

    # get_current_player()
    # returns the player that is currently taking their turn
    def get_current_player(self):
        return self._player_list[self._player_turn - 1] 

    @property
    def city_list(self):
        return self._city_list

    @property
    def outbreak_counter (self):
        return self._outbreak_counter

    @property
    def infection_rate_counter(self):
        return self._infection_rate_counter

    @property
    def infection_rate(self):
        return self._infection_rate

    @property
    def red_cured(self):
        return self._red_cured

    @property
    def blue_cured(self):
        return self._blue_cured

    @property
    def black_cured(self):
        return self._black_cured

    @property
    def yellow_cured(self):
        return self._yellow_cured

    @property
    def red_eradicated(self):
        return self._red_eradicated

    @property
    def blue_eradicated(self):
        return self._blue_eradicated

    @property
    def black_eradicated(self):
        return self._black_eradicated

    @property
    def yellow_eradicated(self):
        return self._yellow_eradicated

    @property
    def red_remaining(self):
        return self._red_remaining

    @property
    def blue_remaining(self):
        return self._blue_remaining

    @property
    def black_remaining(self):
        return self._black_remaining

    @property
    def yellow_remaining(self):
        return self._yellow_remaining

    @property
    def research_stations_remaining(self):
        return self._research_stations_remaining

    @property
    def player_list(self):
        return self._player_list

    @property
    def num_players(self):
        return self._num_players

    @property
    def actions_remaining(self):
        return self._actions_remaining

    @property
    def player_turn(self):
        return self._player_turn
    
    @property
    def player_discard_pile(self):
        return self._player_discard_pile

    @property
    def infection_discard_pile(self):
        return self._infection_discard_pile
    
    @property
    def victory(self):
        return self._victory
    
    @property
    def defeat(self):
        return self._defeat

    @property
    def quarantine_list(self):
        return self._quarantine_list
    
    @property
    def skip_infect_cities(self):
        return self._skip_infect_cities

    @property
    def epidemics_occuring(self):
        return self._epidemics_occuring

    @property
    def player_deck(self):
        return self._player_deck

    @property
    def infection_deck(self):
        return self._infection_deck

    @property
    def temp_board(self):
        return self._temp_board