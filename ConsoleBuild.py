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
        pass

    elif(choice == "2"):
        # Direct flight
        pass

    elif(choice == "3"):
        # Charter flight
        pass

    elif(choice == "4"):
        # Shuttle flight
        pass

    elif(choice == "5"):
        # Build a research station
        pass

    elif(choice == "6"):
        # Treat disease
        pass

    elif(choice == "7"):
        # Share knowledge
        pass

    elif(choice == "8"):
        # Discover a cure
        pass

    elif(choice == "role"):
        # Special role action
        pass

    elif(choice == "event"):
        # Play event card
        pass

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