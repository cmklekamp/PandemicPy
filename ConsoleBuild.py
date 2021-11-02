# invariant culture case

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


# print_menu()
# Prints menu of options to the screen and prompts user input
def print_menu(board):
    # Heading for current player's turn
    print("==========================")
    print("PLAYER " + str(board.player_turn))
    print(board.get_current_player().username + "'s turn")
    print("==========================")
    print()

    # Viewing actions
    print("- - - VIEWING ACTIONS - - -")
    print("(A) Show All Gameplay Elements")
    print("(B) Show Current City and Surrounding City")
    print("(C) Show Infected Cities")
    print("(D) Show All Cities")
    print("(E) Show Misc Board Data")
    print("(F) View Hand")
    print("(G) View All Player Hands")
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
        # Show infected cities
        show_infected_cities(board)

    elif(choice == "D" or choice == "d"):
        # Show all cities
        show_all_cities(board)

    elif(choice == "E" or choice == "e"):
        # Show misc board data
        show_misc_data(board)

    elif(choice == "F" or choice == "f"):
        # View hand
        show_player_hand(board.get_current_player())

    elif(choice == "G" or choice == "g"):
        # View all player hands
        for x in board.player_list:
            show_player_hand(x)

    elif(choice == "1"):
        # Drive / ferry
        print("Showing cities surrounding your current city...")
        for x in (board.city_list[board.get_current_player().current_city].connected_cities):
            show_city_details(board.city_list[x])
        print()
        city_name = input("Move to which city? ")
        if board.simple_move(board.get_current_player(), city_name):
            print("Success! " + board.get_current_player().username + " moved to " + city_name + ".")
        else:
            print(city_name + " is not connected to your current city. Please try again, or select a new action.")

    elif(choice == "2"):
        # Direct flight
        show_player_hand(board.get_current_player())
        city_name = input("Please choose one of your currently held cities to move to: ")
        if board.direct_flight(board.get_current_player(), city_name):
            print("Success! " + board.get_current_player().username + " took a direct flight to " + city_name + ".")
        else:
            print(board.get_current_player().username + " did not have the required card to take a flight here. Please try again, or select a new action.")

    elif(choice == "3"):
        # Charter flight
        show_all_cities(board)
        city_name = input("Please choose a city to move to: ")
        city_is_valid = False
        for x in board.city_list:
            if x[city_name] == city_name:
                city_is_valid = True
                if board.charter_flight(board.get_current_player(), city_name):
                    print("Success! " + board.get_current_player().username + " chartered a flight to " + city_name + ".")
                else:
                    print(board.get_current_player().username + " did not have the required card to charter a flight. Please try again, or select a new action.")
                break
        if city_is_valid == False:
            print("City not found. Action could not be taken.")

    elif(choice == "4"):
        # Shuttle flight
        print("Printing cities with research stations...")
        for x in (board.city_list):
            if x.has_station:
                show_city_details(board.city_list[x])
            print()
        city_name = input("Move to which city? ")
        if board.shuttle_flight(board.get_current_player(), city_name):
            print("Success! " + board.get_current_player().username + " was shuttled to " + city_name + ".")
        else:
            print(city_name + " or the current city does not have the required research station. Please try again, or select a new action.")

    elif(choice == "5"):
        # Build a research station
        print("Building a research station in current city...")
        if board.build_station():
            print("Success! A research station has been built in this city, and its card discarded from your hand.")
        elif board.research_stations_remaining == 0:
            print("You are out of research stations to build. Remove an old one to build a new one here, or select a new action?")
            choice = input("To remove an old one, enter \"R\", to skip and select a new action, enter \"S\": ")
            while choice != 'r' and choice != 'R' and choice != 's' and choice != 'S':
                choice = input("Please enter a valid choice.")
            if choice == 'r' or choice == 'R':
                print("Printing cities with research stations...")
                for x in (board.city_list):
                    if x.has_station:
                        show_city_details(board.city_list[x])
                    print()
                city_name = input("Choose city to remove a research station from, or type \"cancel\" to cancel action: ")
                if board.remove_station(city_name):
                    print("Station removed. You can now build a station.")
                else:
                    print("You chose \"cancel\" or typed an invalid city. Cancelling action...")
            else:
                print("Skipping this action. Please choose a new action.")
        else:
            print("You do not have the required city card to build a station here! Please try again, or select a new action.")

    elif(choice == "6"):
        # Treat disease
        print("Please enter color disease to treat...")
        color = input("red, blue, black, or yellow: ")
        if board.treat_disease(color):
            print("Success! Disease cube(s) removed from your current city!")
        else:
            print("There were no disease cubes of color \"" + color + "\" to remove from this city. Please try again, or select a new action.")

    elif(choice == "7"):
        # Share knowledge
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
                show_player_hand(giving_player)
                card_name = input("Which card to give?")
                if board.share_knowledge(giving_player, taking_player, card_name):
                    print("Success! Knowledge shared!")
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
            else:
                print("One or both players could not be found. Please try again, or select a new action.")
        else:
            print("Player can not share knowledge to themselves. Please try again, or select a new action.")

    elif(choice == "8"):
        # Discover a cure
        if board.get_current_player.can_turn_in():
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

    elif(choice == "role"):
        # Special role action
        pass

    elif(choice == "event"):
        play_event_card(board)

            
    elif(choice == "reset"):
        # Reset this turn
        pass

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
    print("\nShowing " + player.username + "'s hand...\n")
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

    # Show the contingency planner's card if they have one
    if (player.role == 5 and player.contingency_planner_card.value != 0):
        print("CONTIGENCY PLANNER CARD: EVENT -- " + event_card_string(player.contingency_planner_card.value))

    for x in player.playerhand:
        if(isinstance(x, EventCard)):
            print("CARD " + str(counter) + ": EVENT -- " + event_card_string(x.value))
            has_event_card = True
            event_card_list.append(x)
            counter += 1
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
    city = city.capitalize()

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
    city = city.capitalize()

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

    # Main loop: playing the game
    while(board.victory == False and board.defeat == False):
        print_menu(board)

        # Internal loop: current player's turn
        while(True):

            # Confirm action selection, then break out of loop
            if(board.actions_remaining == 0):
                break 

            # Prompt user input for action
            choice = input("> ")

            # Parse user input
            if(choice == "M" or choice == "m"):
                print_menu(board)
            else:
                parse_input(choice, board)


    # End-of-game stuff