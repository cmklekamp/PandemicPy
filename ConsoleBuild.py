# Check!
# printing outbreaks

# - - - - - - - - - - - - - - - - - - - -
# COP 4521 -- Term Project
# Daniel Fletcher, Connor Klekamp, Jacob Gregie
# PANDEMIC board game implementation
# - - - - - - - - - - - - - - - - - - - -


# * * * ConsoleBuild.py * * *
# Main program for testing game functionality on the console
# Will serve as foundational implementation for GUI

# Relevant import statements
from Cards import *
from Decks import *
from City import *
from Player import *
from GameBoard import *
from unidecode import unidecode


# - - - HELPER FUNCTIONS - - -

# print_title()
# Prints the "Pandemic" title ASCII art to the screen
def print_title():
    print("\n=====================================================")
    print("______  ___   _   _______ ________  ________ _____ ")
    print("| ___ \/ _ \ | \ | |  _  \  ___|  \/  |_   _/  __ \\")
    print("| |_/ / /_\ \|  \| | | | | |__ | .  . | | | | /  \/")
    print("|  __/|  _  || . ` | | | |  __|| |\/| | | | | |  ")
    print("| |   | | | || |\  | |/ /| |___| |  | |_| |_| \__/\\")
    print("\_|   \_| |_/\_| \_/___/ \____/\_|  |_/\___/ \____/")
    print("=====================================================\n")


# start_game_data()
# Prompts input for number of players, player names, and desired difficulty
# Returns data as a tuple to be unpacked
def start_game_data():
    # Player count
    player_count = int(input("How many players? (2-4)\n> "))
    while(player_count < 2 or player_count > 4):
        player_count = int(input("\nInvalid input.\nHow many players? (2-4)\n> "))
    print()

    # Player names
    player_names = list()
    for i in range(player_count):
        player_names.append(input("Player " + str(i + 1) + "'s username: "))

    # Desired difficulty
    difficulty = int(input("\nWhat difficulty?\n[4 - Introductory]\n[5 - Standard]\n[6 - Heroic]\n> "))
    while(difficulty < 4 or difficulty > 6):
        print("Invalid input.")
        difficulty = int(input("What difficulty?\n[4 - Introductory]\n[5 - Standard]\n[6 - Heroic]\n> "))
    print()

    # Pack data into tuple and return
    data_package = (player_count, player_names, difficulty)
    return data_package


# role_title()
# Returns role title as a string based on numeric identifier
def role_title(value):
    if(value == 1):
        return "DISPATCHER"
    elif(value == 2):
        return "OPERATIONS EXPERT"
    elif(value == 3):
        return "MEDIC"
    elif(value == 4):
        return "RESEARCHER"
    elif(value == 5):
        return "CONTINGENCY PLANNER"
    elif(value == 6):
        return "QUARANTINE SPECIALIST"
    else:
        return "SCIENTIST"


# show_roles()
# Shows roles of all players in the game
def show_roles(board):
    print("\nShowing all player roles...\n")
    for player in board.player_list:
        print(player.username.upper() + " -- " + role_title(player.role))
    print()


# print_menu()
# Prints menu of options to the screen and prompts user input
def print_menu(board):
    # Heading for current player's turn
    print("==========================")
    print("PLAYER " + str(board.player_turn) + " -- " + role_title(board.get_current_player().role))
    print(board.get_current_player().username + "'s turn")
    print("==========================")
    print()

    # Viewing actions
    print("- - - VIEWING ACTIONS - - -")
    print("(A) Show All Gameplay Elements")
    print("(B) Show Current City and Surrounding City")
    print("(C) Show Cities with Research Stations")
    print("(D) Show Infected Cities")
    print("(E) Show All Cities")
    print("(F) Show Misc Board Data")
    print("(G) View Hand")
    print("(H) View All Player Hands")
    print("(M) Re-print Menu")
    print()

    # Gameplay actions
    print("- - - EIGHT MAIN ACTIONS - - -")
    print("(1) Drive / Ferry")
    print("(2) Direct Flight")
    print("(3) Charter Flight")
    print("(4) Shuttle Flight")
    print("(5) Build a Research Station")
    print("(6) Treat Disease")
    print("(7) Share Knowledge")
    print("(8) Discover a Cure")
    print()

    # Additional actions
    print("- - - ADDITIONAL ACTIONS - - -")
    print("(\"role\") Special Role Action")
    print("(\"event\") Play Event Card")
    print("(\"reset\") Reset This Turn")
    print()


# parse_input()
# Interprets the user's menu choice and calls the appropriate functions
def parse_input(choice, board):
    if(choice == "A" or choice == "a"):
        # Show all gameplay elements
        show_current_city(board)
        show_all_cities(board)
        show_misc_data(board)
        for x in board.player_list:
            show_player_hand(x)

    elif(choice == "B" or choice == "b"):
        # Show current city and surrounding city
        show_current_city(board)

    elif(choice == "C" or choice == "c"):
        # Show cities with research stations
        show_research_cities(board)

    elif(choice == "D" or choice == "d"):
        # Show infected cities
        show_infected_cities(board)

    elif(choice == "E" or choice == "e"):
        # Show all cities
        show_all_cities(board)

    elif(choice == "F" or choice == "f"):
        # Show misc board data
        show_misc_data(board)

    elif(choice == "G" or choice == "g"):
        # View hand
        show_player_hand(board.get_current_player())

    elif(choice == "H" or choice == "h"):
        # View all player hands
        for x in board.player_list:
            show_player_hand(x)

    elif(choice == "1"):
        # Drive / ferry
        drive_ferry(board)

    elif(choice == "2"):
        # Direct flight
        take_direct_flight(board)

    elif(choice == "3"):
        # Charter flight
        take_charter_flight(board)

    elif(choice == "4"):
        # Shuttle flight
        take_shuttle_flight(board)

    elif(choice == "5"):
        # Build a research station
        build_research_station(board)

    elif(choice == "6"):
        # Treat disease
        treat_disease_action(board)

    elif(choice == "7"):
        # Share knowledge
        share_knowledge_action(board)

    elif(choice == "8"):
        # Discover a cure
        discover_cure_action(board)

    elif(choice == "role"):
        player = board.get_current_player()

        # Dispatcher Action
        if (player.role == 1):
           dispatcher_action(board, player)

        # Operations Expert Action
        elif (player.role == 2):
            operations_expert_action(board, player)
            
        # Contingency Planner Action
        elif (player.role == 5):
            contingency_planner_action(board, player)
        
        else:
            print("The current player's role does not have an special action they can take.\n")
            
    elif(choice == "event"):
        play_event_card(board)

    elif(choice == "reset"):
        resetting = True
        print("The turn has been reset.\n")
        return resetting

    else:
        print("\nInvalid option.\n")


# show_current_city()
# Shows the details of the city of the current player and the surrounding cities
def show_current_city(board):
    # Heading and current city
    print("\nShowing current city and surrounding cities...")
    show_city_heading()
    show_city_details(board.city_list[board.get_current_player().current_city])

    # Surrounding cities
    for x in (board.city_list[board.get_current_player().current_city].connected_cities):
        show_city_details(board.city_list[x])
    print()


# show_research_cities()
# Shows the details of all cities with research stations
def show_research_cities(board):
    # Heading and message
    print("\nShowing all cities with research stations...")
    show_city_heading()

    # Show details for all cities with research stations
    for x in (board.city_list):
        if board.city_list[x].has_station:
            show_city_details(board.city_list[x])
    print()


# show_infected_cities
# Shows the details of all cities with disease cubes on the board
def show_infected_cities(board):
    # Heading and message
    print("\nShowing all infected cities...")
    show_city_heading()

    # Show details for all INFECTED cities
    for x in (board.city_list):
        if(board.city_list[x].blue > 0 or board.city_list[x].red > 0 or board.city_list[x].black > 0 or board.city_list[x].yellow > 0):
            show_city_details(board.city_list[x])
    print()


# show_all_cities()
# Shows the details of all cities on the board
def show_all_cities(board):
    # Heading and message
    print("\nShowing ALL cities on the board...")
    show_city_heading()

    # Show details for all cities
    for x in (board.city_list):
        show_city_details(board.city_list[x])
    print()


# show_city_heading()
# Shows the heading for printing a city's details, in the same format as show_city_details()
def show_city_heading():
    heading_info = ("CITY NAME", "COLOR", "STATION", "BLUE", "RED", "BLACK", "YELLOW")
    city_name, color, station, blue, red, black, yellow = heading_info
    heading_string = "{0:30} {1:10} {2:10} {3:10} {4:10} {5:10} {6:10}".format(city_name, color, station, blue, red, black, yellow)
    print("\n===============================================================================================================")
    print(heading_string)
    print("===============================================================================================================")


# show_city_details()
# Helper function for showing the details of a single city
def show_city_details(city):
    # Helper string for has_station property
    if(city.has_station):
        station_string = "X"
    else:
        station_string = ""

    # Creating and printing the city details as a string
    city_string = "{0:30} {1:10} {2:10} {3:10} {4:10} {5:10} {6:10}".format(city.name, city.color, station_string, str(city.blue), str(city.red), str(city.black), str(city.yellow))
    print(city_string)


# show_misc_data()
# Show the outbreak tracker, infection rate, cures, and cubes remaining
def show_misc_data(board):
    # Print message
    print("\n Showing miscellaneous board data...\n")

    # Outbreak tracker
    print("<-- OUTBREAK TRACKER -->")
    print("0\t1\t2\t3\t4\t5\t6\t7\t8")
    if(board.outbreak_counter == 0):
        print("^")
    elif(board.outbreak_counter == 1):
        print(" \t^")
    elif(board.outbreak_counter == 2):
        print(" \t \t^")
    elif(board.outbreak_counter == 3):
        print(" \t \t \t^")
    elif(board.outbreak_counter == 4):
        print(" \t \t \t \t^")
    elif(board.outbreak_counter == 5):
        print(" \t \t \t \t \t^")
    elif(board.outbreak_counter == 6):
        print(" \t \t \t \t \t \t^")
    elif(board.outbreak_counter == 7):
        print(" \t \t \t \t \t \t \t^")
    else:
        print(" \t \t \t \t \t \t \t \t^")
    print()

    # Infection rate
    print("<-- INFECTION RATE -->")
    print("2\t2\t2\t3\t3\t4\t4")
    if(board.infection_rate_counter == 0):
        print("^")
    elif(board.infection_rate_counter == 1):
        print(" \t^")
    elif(board.infection_rate_counter == 2):
        print(" \t \t^")
    elif(board.infection_rate_counter == 3):
        print(" \t \t \t^")
    elif(board.infection_rate_counter == 4):
        print(" \t \t \t \t^")
    elif(board.infection_rate_counter == 5):
        print(" \t \t \t \t \t^")
    else:
        print(" \t \t \t \t \t \t^")
    print()

    # Cured diseases / eradicated diseases, I -- helper strings
    if(board.blue_cured and board.blue_eradicated):
        blue_string = "  X   /     X"
    elif(board.blue_cured and board.blue_eradicated == False):
        blue_string = "  X   /"
    else:
        blue_string = "      /"
    if(board.red_cured and board.red_eradicated):
        red_string = "  X   /     X"
    elif(board.red_cured and board.red_eradicated == False):
        red_string = "  X   /"
    else:
        red_string = "      /"
    if(board.black_cured and board.black_eradicated):
        black_string = "  X   /     X"
    elif(board.black_cured and board.black_eradicated == False):
        black_string = "  X   /"
    else:
        black_string = "      /"
    if(board.yellow_cured and board.yellow_eradicated):
        yellow_string = "  X   /     X"
    elif(board.yellow_cured and board.yellow_eradicated == False):
        yellow_string = "  X   /"
    else:
        yellow_string = "      /"

    # Cured diseases / eradicated diseases, II -- printing
    print("<-- CURED AND ERADICATED DISEASES -->")
    print("{0:10} {1:30}".format("DISEASE", "CURED / ERADICATED"))
    print("{0:10} {1:30}".format("blue", blue_string))
    print("{0:10} {1:30}".format("red", red_string))
    print("{0:10} {1:30}".format("black", black_string))
    print("{0:10} {1:30}".format("yellow", yellow_string))
    print()

    # Remaining disease cubes
    print("<-- REMAINING DISEASE CUBES -->")
    print("{0:10} {1:10}".format("blue", str(board.blue_remaining)))
    print("{0:10} {1:10}".format("red", str(board.red_remaining)))
    print("{0:10} {1:10}".format("black", str(board.black_remaining)))
    print("{0:10} {1:10}".format("yellow", str(board.yellow_remaining)))
    print()


# show_player_hand()
# Show all cards in a player's hand
def show_player_hand(player):
    print("\nShowing " + player.username + "'s hand...")
    print("(" + player.username + " is the " + role_title(player.role) + ".)\n")
    counter = 1
    
    # Show the contingency planner's card if they have one
    if (player.role == 5 and player.contingency_planner_card.value != 0):
        print("CONTIGENCY PLANNER CARD: EVENT -- " + event_card_string(player.contingency_planner_card.value))

    for x in player.playerhand:
        if(isinstance(x, CityCard)):
            print("CARD " + str(counter) + ": " + x.city + " / " + x.color)
        else:
            print("CARD " + str(counter) + ": EVENT -- " + event_card_string(x.value))
        counter += 1
    print()


# MAIN ACTIONS 1-8 FUNCTIONS

# 1: Drive/ferry movement action
def drive_ferry(board):
    show_current_city(board)
    city_name = input("Move to which city? ")
    if board.simple_move(board.get_current_player(), city_name):
        print("Success! " + board.get_current_player().username + " moved to " + city_name + ".")
    else:
        print(city_name + " is not connected to your current city. Please try again, or select a new action.")

# 2: Direct flight movement action
def take_direct_flight(board):
    show_player_hand(board.get_current_player())
    city_name = input("Please choose one of your currently held cities to move to: ")
    if board.direct_flight(board.get_current_player(), city_name):
        print("Success! " + board.get_current_player().username + " took a direct flight to " + city_name + ".")
    else:
        print(board.get_current_player().username + " did not have the required card to take a flight here. Please try again, or select a new action.")

# 3: Charter flight movement action
def take_charter_flight(board):
    show_all_cities(board)
    city_name = input("Please choose a city to move to: ")
    city_is_valid = False
    for x in board.city_list:
        if unidecode(x) == city_name:
            city_is_valid = True
            if board.charter_flight(board.get_current_player(), x):
                print("Success! " + board.get_current_player().username + " chartered a flight to " + x + ".")
            else:
                print(board.get_current_player().username + " did not have the required card to charter a flight. Please try again, or select a new action.")
            break
    if city_is_valid == False:
        print("City not found. Action could not be taken.")

# 4: Shuttle flight movement action
def take_shuttle_flight(board):
    show_research_cities(board)
    city_name = input("Move to which city? ")
    if board.shuttle_flight(board.get_current_player(), city_name):
        print("Success! " + board.get_current_player().username + " was shuttled to " + city_name + ".")
    else:
        print(city_name + " or the current city does not have the required research station. Please try again, or select a new action.")

# 5: Build research station
def build_research_station(board):
    print("Building a research station in current city...")
    if board.build_station():
        print("Success! A research station has been built in this city, and its card discarded from your hand.")
    elif board.research_stations_remaining == 0:
        print("You are out of research stations to build. Remove an old one to build a new one here, or select a new action?")
        choice = input("To remove an old one, enter \"R\", to skip and select a new action, enter \"S\": ")
        while choice != 'r' and choice != 'R' and choice != 's' and choice != 'S':
            choice = input("Please enter a valid choice.")
        if choice == 'r' or choice == 'R':
            show_research_cities(board)
            city_name = input("Choose city to remove a research station from, or type \"cancel\" to cancel action: ")
            if board.remove_station(city_name):
                print("Station removed. You can now build a station.")
            else:
                print("You chose \"cancel\" or typed an invalid city. Cancelling action...")
        else:
            print("Skipping this action. Please choose a new action.")
    else:
        print("You do not have the required city card to build a station here! Please try again, or select a new action.")

# 6: Treat disease
def treat_disease_action(board):
    show_city_heading()
    show_city_details(board.city_list[board.get_current_player().current_city])
    print("\nPlease enter color disease to treat...")
    color = input("red, blue, black, or yellow: ")
    if board.treat_disease(color):
        print("Success! Disease cube(s) removed from your current city!")
    else:
        print("There were no disease cubes of color \"" + color + "\" to remove from this city. Please try again, or select a new action.")

# 7: Share knowledge
def share_knowledge_action(board):
    print("Note that if the taking player goes over the hand limit, they must discard a card...")
    giving_player_name = input("Which player is giving the card? ")
    taking_player_name = input("Which player is taking the card? ")
    giving_player_valid = False
    taking_player_valid = False
    if giving_player_name != taking_player_name:
        for x in board.player_list:
            if x.username == giving_player_name:
                giving_player_valid = True
                giving_player = x
            elif x.username == taking_player_name:
                taking_player_valid = True
                taking_player = x
        if giving_player_valid and taking_player_valid:
            if board.share_knowledge(giving_player, taking_player, board.get_current_player().current_city):
                print("Success! The " + board.get_current_player().current_city + " card was given to " + taking_player_name + ".")
                if taking_player.over_hand_limit():
                    print("Taking player is now over the hand limit. Please discard a card.")
                    show_player_hand(taking_player)
                    discarded = False
                    while discarded == False:
                        discard_card = input("Discard which card?")
                        if taking_player.discard(discard_card):
                            print("Discard successful.")
                            discarded = True
            else:
                print("Invalid card. Knowledge could not be shared.")
                print("This may be because the card is not in the player's hand, or the card does not match the current city of both players.")
        else:
            print("One or both players could not be found. Please try again, or select a new action.")
    else:
        print("Player can not share knowledge to themselves. Please try again, or select a new action.")

# 8: Discover cure
def discover_cure_action(board):
    if board.get_current_player().can_turn_in():
        print("Please input all five cards of one color to turn in, or type \"cancel\": ")
        card_num = 0
        card_name = ""
        discard_list = []
        while card_num > 5 and card_name != "cancel":
            show_player_hand(board.get_current_player())
            card_name = input("Card name (or \"cancel\"): ")
            for x in board.get_current_player().playerhand:
                if x.city == card_name:
                    card_num = card_num + 1
                    discard_list.append(x)
        color = input("What disease color would you like to cure (red, blue, black, or yellow)? ")
        if card_num == 5 and (color == "red" or color == "blue" or color == "black" or color == "yellow"):
            if board.discover_cure(color, discard_list):
                print("Success! This desease has been eradicated!")
            else:
                print("This disease was unable to be eradicated. This could be because you did not have the proper cards, or are not positioned on a research station.")
        else:
            print("Invalid color. Please try again, or select a new action.")
    else:
        print(board.get_current_player().username + " does not have enough cards to turn in. Please try again, or select a new action.")

# Dispatcher Special Action
def dispatcher_action(board, dispatcher):
    print("- - - VIEWING ACTIONS - - -")
    print("(1) Drive / Ferry")
    print("(2) Direct Flight")
    print("(3) Charter Flight")
    print("(4) Shuttle Flight")
    print("(5) Player to Player")
    choice = input("\nWhat kind of move would you like to make? (Enter the number): ")
    choice = int(choice)

    if (choice < 1 or choice > 5):
        print("Why did you try to pick an action that wasn't listed. Don't do that.\n")
        return

    print("\nShowing Player List...\n")
    counter = 1
    for x in board.player_list:
        print("Player " + str(counter) + ": " + x.username + ", " + x.current_city)
        counter += 1       
    
    # Dispatcher Simple Move
    if (choice == 1):              
        choice = input("\nWho is gonna move? (Enter the number): ")
        choice = int(choice) - 1
        player = board.player_list[choice]

        print("Showing cities surrounding " + player.username + "'s current city...")
        for x in (board.city_list[player.current_city].connected_cities):
            show_city_details(board.city_list[x])

        city_name = input("\nMove to which city? (Enter the name) ")
        if board.dispatcher_simple_move(player, city_name):
            print("Success! " + player.username + " moved to " + city_name + ".\n")
        else:
            print(city_name + " is not connected to " + player.username + "'s  current city.\n")

    # Dispatcher Direct Flight
    elif (choice == 2):
        choice = input("\nWho is gonna move? (Enter the number): ")
        choice = int(choice) - 1
        moving_player = board.player_list[choice]

        show_player_hand(dispatcher)
        city_name = input("Please choose one of your currently held cities to move to (Enter the name): ")
        if board.dispatcher_direct_flight(moving_player, city_name):
            print("\nSuccess! " + moving_player.username + " took a direct flight to " + city_name + ".\n")
        else:
            print("\n" + moving_player.username + " could not take a flight to " + city_name + ".\n")

    # Dispatcher Charter Flight
    elif (choice == 3):
        choice = input("\nWho is gonna move? (Enter the number): ")
        choice = int(choice) - 1
        moving_player = board.player_list[choice]

        city_name = input("\nPlease choose a city to move to. (Enter the name): ")
        city_is_valid = False
        for x in board.city_list:
            if unidecode(x) == city_name:
                city_is_valid = True
                if board.dispatcher_charter_flight(moving_player, city_name):
                    print("\nSuccess! " + moving_player.username + " chartered a flight to " + city_name + ".\n")
                else:
                    print("\n" + moving_player.username + " could not take a flight to " + city_name + ".\n")
                break
        if city_is_valid == False:
            print("\nCity not found. Action could not be taken.\n")

    # Dispatcher Shuttle Flight
    elif (choice == 4):
        choice = input("\nWho is gonna move? (Enter the number): ")
        choice = int(choice) - 1
        moving_player = board.player_list[choice]

        print("Printing cities with research stations...")
        show_research_cities(board)

        city_name = input("Move to which city? (Enter the name): ")
        if board.dispatcher_shuttle_flight(moving_player, city_name):
            print("\nSuccess! " + moving_player.username + " was shuttled to " + city_name + ".\n")
        else:
            print("\n" + moving_player.username + " could not take a flight to " + city_name + ".\n")

    # Dispatcher Move Player to Player
    elif (choice == 5):
        choice = input("\nWho is gonna move? (Enter the number): ")
        choice = int(choice) - 1
        moving_player = board.player_list[choice]

        choice2 = input("\nWho are they moving to? (Enter the number): ")
        choice2 = int(choice2) - 1
        destination_player = board.player_list[choice2]

        if (moving_player == destination_player):
            print("\nCongratulations, you just tried to move a player to themselves. Next time, don't do that.\n")
        
        else:
            if (board.dispatcher_move_p2p(moving_player, destination_player) == True):
                print("\n" + moving_player.username + " successfully moved to " + destination_player.username + ". Now kiss.\n")
            else:
                print("\nSomebody involved in this equation is not a real person, find the imposter.\n")

# Operations Expert Action
def operations_expert_action(board,player):
    if (board.operations_expert_action_complete == True):
        print ("\nYou tried to pull a fast one on me huh. You already did that this turn. If you could do that more than once in a turn, that would be BROKEN.\n")
        return
    
    if (board.city_list[player.current_city].has_station == False):
        print("\nBro, you aren't even in a city with a research station.\n")
        return

    has_city_card = False
    for x in player.playerhand:
        if isinstance (x, CityCard):
            has_city_card = True

    if (has_city_card == False):
        print ("You seem to be lacking a critical piece of cardboard to complete this action, a city card.\n")
        return

    print ("Now showing " + player.username + "'s hand...\n")
    show_player_hand(player)

    choice = input("What card would you like to discard? (Enter the number): ")
    choice = int(choice) - 1

    card = player.playerhand[choice]
    if (isinstance(card, CityCard) == False):
        print("\nYou just picked an invalid card, shame on you.\n")
        return

    city = input("\nWhere would you like to go? (Enter the name of the city): ")

    success = board.operations_expert_move(card, city)
    if (success == True):
        print("\nPack your bags, " + player.username + ". You are going to " + city + ".\n")
    else:
        print("\n" + player.username + " ,I hate to tell you this, but you aren't going anywhere.\n")    

# Contingency Planner Action   
def contingency_planner_action(board,player):
    if (player.contingency_planner_card.value != 0):
        print("You already have an event card, silly.\n")

    empty = True
    counter = 1
    event_list = []          
    print ("Showing event cards in discard pile...\n")
    for x in board.player_discard_pile:
        if (isinstance(x, EventCard)):
            print("CARD " + str(counter) + ": " + event_card_string(x.value))
            counter+= 1
            empty = False
            event_list.append(x)

    if (empty == True):
        print ("There are no event cards in the discard pile.\n")

    else:
        choice = input("\nWhat card would you like to take? (Enter the number): ")
        choice = int(choice) - 1
        card = event_list[choice]
        board.contingency_planner_take(card)
        print(player.username + " has acquired: " + event_card_string(card.value) + "\n")

# event_card_string()
# Returns the title of the event card based on the numeric value
def event_card_string(value):
    if(value == 1):
        return "One Quiet Night"
    elif(value == 2):
        return "Forecast"
    elif(value == 3):
        return "Government Grant"
    elif(value == 4):
        return "Airlift"
    else:
        return "Resilient Population"

# play_event_card()
# Function for playing an event card
def play_event_card(board):
    counter = 1
    print()
    for x in board.player_list:
        print ("Player " + str(counter) + ": " + x.username)
        counter += 1

    choice = input("\nWho is using an event card? (Enter Player Number): ")
    choice = int(choice) - 1
    player = board.player_list[choice]

    print("\nShowing event cards in " + player.username + "'s hand...")
    counter = 1
    has_event_card = False
    event_card_list = list()

    for x in player.playerhand:
        if(isinstance(x, EventCard)):
            print("CARD " + str(counter) + ": EVENT -- " + event_card_string(x.value))
            has_event_card = True
            event_card_list.append(x)
            counter += 1

    # Show the contingency planner's card if they have one
    if (player.role == 5 and player.contingency_planner_card.value != 0):
        print("CARD " + str(counter) + ": CONTIGENCY PLANNER CARD: EVENT -- " + event_card_string(player.contingency_planner_card.value))
        has_event_card = True
        event_card_list.append(player.contingency_planner_card)
    print()

    if (has_event_card == False):
        print("There are no event cards in " + player.username + "'s hand\n")
        return
    
    choice = input("Select the card that you want to use (\"0\" to cancel): ")
    choice = int(choice) - 1

    if choice == -1:
        print("\nNo event card was used.\n")
        return

    card = event_card_list[choice]

    if (card.value == 1):
        play_one_quiet_night(board, player)
    elif (card.value == 2):    
        play_forecast(board, player)     
    elif (card.value == 3):
        play_government_grant(board, player)
    elif (card.value == 4):
        play_airlift(board, player)
    elif (card.value == 5):
        play_resilient_population(board, player)
    else:
        print("Card does not exist.\n")


# play_one_quiet_night()
# plays the One Quiet Night Event Card
def play_one_quiet_night(board, player):
    board.one_quiet_night(player)
    print ("\nThe next Infect Cities step will be skipped.\n")


# play_forcast()
# plays the Forcast Event Card
def play_forecast(board,player):
    infection_list = []
    print ("\nShowing the top 6 cards of the Infection Deck...\n")
    for x in range(6):
        y = board.infection_deck.top_card()
        print("CARD " + str(x+1) + ": " + y.city + " / " + y.color)
        infection_list.append(y)

    print ("\nSelect each card in the order that you want them placed on the deck. The last card you choose will be on the top of the deck.\n")

    rearranged_list = []
    for x in range(6):  
        choice = input("Enter card number " + str(x+1) + ": ")
        choice = int(choice) - 1

        while infection_list[choice] in rearranged_list:
            choice = input("Card already chosen. Try Again: ")
            choice = int(choice) - 1

        rearranged_list.append(infection_list[choice])

    board.forecast(player, rearranged_list)
    print("\nThe top 6 cards of the infection deck have been rearranged.\n")


# play_government_grant()
# plays the Government Grant Event Card
def play_government_grant(board, player):

    if (board.research_stations_remaining == 0):
        choice = input("\nYou have reached the research station limit. Would you like to remove a research station? (Y or N): ")

        if (choice.upper() != "Y"):
            return

        else:
            station_list = []
            counter = 1
            for x in board.city_list:
                if (board.city_list[x].has_station == True):
                    print("City " + str(counter) + ": " + board.city_list[x].name)
                    counter += 1
                    station_list.append(x)

            choice = input("\nSelect the city that you want to remove a research station from (\"0\" to cancel): ")
            choice = int(choice) - 1

            board.remove_station(station_list[choice])
            print("\nThe research station in " + station_list[choice] + " has been removed.")

    city = input("\nWhat city would you like to build a research station in? (Enter the name): ")

    success = board.government_grant(player, city)
    if success == True:
        print("\nA research station was built in " + city + ".\n")
    else:
        print("\nA research station was unable to be built in " + city + ".\n")


# play_airlift()
# plays the Airlift Event Card
def play_airlift(board, player):
    counter = 1
    print()
    for x in board.player_list:
        print ("Player " + str(counter) + ": " + x.username)
        counter += 1

    choice = input("\nWho is being moved? (Enter Player Number): ")
    choice = int(choice) - 1
    moving_player = board.player_list[choice]

    city = input("\nWhat city would you like " + moving_player.username + " to move to? ")

    success = board.airlift(player, moving_player, city)
    if success == True:
        print(moving_player.username + " is now in " + city + "\n")
    else:
        print(moving_player.username + " was unable to move to " + city + "\n")


# play_resilient_population()
# plays the Resilient Population Event Card
def play_resilient_population(board, player):
    if (len(board.infection_discard_pile) == 0):
        print ("The infection discard pile is empty.\n")
        return

    counter = 1
    discard_list = []
    print()
    for x in board.infection_discard_pile:
        print("CARD " + str(counter) + ": " + x.city + " / " + x.color)
        counter += 1  
        discard_list.append(x)  

    choice = input("\nWhat infection card would you like to remove from the game? (Enter the number of the card): ")
    choice = int(choice) - 1

    success = board.resilient_population(player, discard_list[choice])
    if success == True:
        print("\nThe " + discard_list[choice].city + " infection card has been removed from the game.\n")
    else:
        print("\nThe " + discard_list[choice].city + " infection card was unable to be removed from the game.\n")



# - - - MAIN ROUTING - - -
if __name__ == "__main__":
    # Show title and set up the game
    print_title()
    player_count, usernames, difficulty = start_game_data()
    board = GameBoard(player_count, usernames, difficulty)
    show_roles(board)

    # Main loop: playing the game
    while(board.victory == False and board.defeat == False):
        print_menu(board)

        # Make a copy that is saved for when a reset is called
        temp_board = copy.deepcopy(board)

        # Internal loop: current player's turn
        while(True):

            # Confirm action selection, then break out of loop
            if(board.actions_remaining == 0 or board.victory == True):
                break 

            # Prompt user input for action
            choice = input("> ")

            # Parse user input
            if(choice == "M" or choice == "m"):
                print_menu(board)
            else:
                resetting = parse_input(choice, board)      
                if (resetting == True):
                    board = copy.deepcopy(temp_board)
                    resetting = False

        # allow use of event cards before draw phase
        choice = "Y"
        while (choice.upper() == "Y"):
            choice = input("\nWould anybody like to use an event card before the player draw phase begins? (Y or N): ")
            if choice.upper() == "Y":
                play_event_card(board)
        
        # draw cards
        player = board.get_current_player()
        print("\nDrawing the cards from the Player Deck...\n")
        board.draw_cards()
        if (board.defeat == True):
            continue

        # show acquired cards
        temp = 2 - board.epidemics_occuring
        for x in range(temp):
            card = player.playerhand[-(x+1)]
            if(isinstance(card, CityCard)):
                print(player.username + " acquired: " + card.city + " / " + card.color)
            else:
                print(player.username + " acquired: " + event_card_string(card.value))
        print()

        # epidemic time
        while (board.epidemics_occuring != 0):
            print ("\nOH NO! AN EPIDEMIC IS OCCURRING!!!\n")

            board.epidemic()
            infected_city = board.infection_discard_pile[-1]
            print(infected_city.city + " was infected!\n")

            for x in board.city_list:
                if board.city_list[x].had_outbreak == True:
                    print("Ruh Roh Raggy! " + x + " had an outbreak!")

            if (board.defeat == True):
                continue

            has_resilient_population = False
            for x in board.player_list:
                for y in x.playerhand:
                    if (isinstance(y, EventCard) and y.value == 5):
                        resilient_population_player = x
                        has_resilient_population = True

            if (has_resilient_population == True):
                print(resilient_population_player.username + " has the Resilient Population card.")
                choice = input("Would " + resilient_population_player.username + " like to play this card? (Y or N): ")
                if (choice.upper() == "Y"):
                    play_resilient_population(board, resilient_population_player)

            board.intensify()

        # allow use of event cards before draw phase
        choice = "Y"
        while (choice.upper() == "Y"):
            choice = input("\nWould anybody like to use an event card before the infection draw phase begins? (Y or N): ")
            if choice.upper() == "Y":
                play_event_card(board)

        if (board.skip_infect_cities == False):   
            for x in range(board.infection_rate):
                board.draw_infection_card()
                print("\nCard drawn from the infection pile: " + board.infection_discard_pile[-1].city)

                for x in board.city_list:
                    if board.city_list[x].had_outbreak == True:
                        print("Ruh Roh Raggy! " + x + " had an outbreak!")
            print()
                
        else:
            board.skip_infect_cities = False
            print ("\nThankfully, the infect phase has been skipped.\n")

        while player.over_hand_limit() == True:
            print("\nYou got too many cards in your pockets, either use 'em or throw 'em away.\n")
            show_player_hand(player)

            choice = input("Pick a card that you want to use or lose. (Enter the number): ")
            choice = int(choice) - 1

            card = player.playerhand[choice]
            if (isinstance(card, CityCard)):
                board.discard(card)
                print("\nBye Bye Mr. Card, A.K.A: " + card.city + "\n")

            if (isinstance(card, EventCard)):
                if (card.value == 1):
                    play_one_quiet_night(board,player)
                elif (card.value == 2):
                    play_forecast(board,player)
                elif (card.value == 3):
                    play_government_grant(board,player)
                elif (card.value == 4):
                    play_airlift(board,player)
                elif (card.value == 5):
                    play_resilient_population(board,player)

        board.next_turn()

    # End-of-game stuff
    if (board.victory == True):
        print("\nMission Complete! You saved the world from impending doom!\n")
    else:
        print("\nMission Failed. The world is going to perish and it is all your fault.\n")