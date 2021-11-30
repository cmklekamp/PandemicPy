# - - - - - - - - - - - - - - - - - - - -
# COP 4521 -- Term Project
# Daniel Fletcher, Connor Klekamp, Jacob Gregie
# PANDEMIC board game implementation
# - - - - - - - - - - - - - - - - - - - -

# * * * Actions.py * * *
# GUI implementation of the action buttons

# Relevant import statements -- custom classes (logic)
import tkinter
from Cards import *
from Decks import *
from City import *
from Player import *
from GameBoard import *
import PandemicGame

# Relevant import statements -- tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import simpledialog

# Main application class
class ActionFrame(Frame):
    # Overridden constructor
    def __init__(self, app, master=None):
        Frame.__init__(self, master, height=100, width=1050, bg = 'blue')
        self.app = app
        self.createWidgets()

    # createWidgets()
    # Creates widgets upon initialization in constructor
    def createWidgets(self):
        # Drive/ferry button creation
        self.simple_move_button = Button(self, text="Drive", command=lambda: self.simple_move_click(), font = ("Times New Roman",10))
        self.simple_move_button.place(height = 50, width = 70, x=50, y=25)

        # Direct flight button creation
        self.direct_flight_button = Button(self, text="Direct\nFlight", command=lambda: self.direct_flight_click(), font = ("Times New Roman",10))
        self.direct_flight_button.place(height = 50, width = 70, x=130, y=25)

        # Charter flight button creation
        self.charter_flight_button = Button(self, text="Charter\nFlight", command=lambda: self.charter_flight_click(), font = ("Times New Roman",10))
        self.charter_flight_button.place(height = 50, width = 70, x=210, y=25)

        # Shuttle flight button creation
        self.shuttle_flight_button = Button(self, text="Shuttle\nFlight", command=lambda: self.shuttle_flight_click(), font = ("Times New Roman",10))
        self.shuttle_flight_button.place(height = 50, width = 70, x=290, y=25)

        # Build station button creation
        self.build_station_button = Button(self, text="Build\nStation", command=lambda: self.build_station_click(), font = ("Times New Roman",10))
        self.build_station_button.place(height = 50, width = 70, x=370, y=25)

        # Treat disease button creation
        self.treat_disease_button = Button(self, text="Treat\nDisease", command=lambda: self.treat_disease_click(), font = ("Times New Roman",10))
        self.treat_disease_button.place(height = 50, width = 70, x=450, y=25)

        # Share knowledge button creation
        self.share_knowledge_button = Button(self, text="Share\nKnowledge", command=lambda: self.share_knowledge_click(), font = ("Times New Roman",10))
        self.share_knowledge_button.place(height = 50, width = 70, x=530, y=25)

        # Discover cure button creation
        self.discover_cure_button = Button(self, text="Discover\nCure", command=lambda: self.discover_cure_click(), font = ("Times New Roman",10))
        self.discover_cure_button.place(height = 50, width = 70, x=610, y=25)

        # Player role action button creation
        self.role_action_button = Button(self, text="Role\nAction", command=lambda: self.role_action_click(), font = ("Times New Roman",10))
        self.role_action_button.place(height = 50, width = 70, x=690, y=25)

        # Play event card button creation
        self.play_event_button = Button(self, text="Event\nCard", command=lambda: self.play_event_click(), font = ("Times New Roman",10))
        self.play_event_button.place(height = 50, width = 70, x=770, y=25)

        # Pass button creation
        self.pass_button = Button(self, text="Pass", command=lambda: self.pass_click(), font = ("Times New Roman",10))
        self.pass_button.place(height = 50, width = 70, x=850, y=25)

        # Reset button creation
        self.reset_button = Button(self, text="Reset\nTurn", command=lambda: self.reset_click(), font = ("Times New Roman",10))
        self.reset_button.place(height = 50, width = 70, x=930, y=25)


    # Disable buttons function for general use. Does not include reset button, as that should be available until the draw phase starts.
    def disable_buttons(self):
        self.simple_move_button["state"] = "disabled"
        self.direct_flight_button["state"] = "disabled"
        self.charter_flight_button["state"] = "disabled"
        self.shuttle_flight_button["state"] = "disabled"
        self.build_station_button["state"] = "disabled"
        self.treat_disease_button["state"] = "disabled"
        self.share_knowledge_button["state"] = "disabled"
        self.discover_cure_button["state"] = "disabled"
        self.role_action_button["state"] = "disabled"
        self.pass_button["state"] = "disabled"


    # Button click events
    # Remember to add log_print functionality (i.e. make sure actions print to the log)

    # AFTER EVERY ACTION, MAY HAVE TO RETURN SELECTED CITY AND CARD TO EMPTY
    # AFTER THE ACTION PHASE, DISABLE BUTTONS UNTIL NEXT ACTION PHASE

    def simple_move_click(self):
        # Allows the player to select a city they are next to and drive to it.
        self.app.board_frame.log_print("Please select a city to drive to.")
        self.app.board_frame.confirm_city_button["state"] = "normal"
        self.app.board_frame.confirm_city_button.wait_variable(self.app.board_frame.board_var) 
        if self.app.board.simple_move(self.app.board.get_current_player(), self.app.confirmed_city):
            self.app.city_viewer_frame.update_info()
            log_str = self.app.board.get_current_player().username + " drove to " + self.app.selected_city + ". " + str(self.app.board.actions_remaining) + " action(s) remaining.\n"
            self.app.board_frame.log_print(log_str)
            if self.app.board.actions_remaining == 0:
                self.disable_buttons()
                self.app.board_frame.show_draw_phase_button()
        else:
            self.app.board_frame.log_print("Invalid city. You may only drive to a city you are next to.\n")
        self.app.board_frame.confirm_city_button["state"] = "disabled"

    def direct_flight_click(self):
        # Allows the player to select a card from their hand to take a direct flight to.
        self.app.board_frame.log_print("Please select a city card to take a direct flight to.")
        self.app.hand_frame.confirm_card_button.wait_variable(self.app.confirmed_card)
        card_name = self.app.confirmed_card.get()
        if card_name != "":
            if self.app.board.direct_flight(self.app.board.get_current_player(), card_name):
                self.app.city_viewer_frame.update_info()
                self.app.hand_frame.createWidgets()
                log_str = self.app.board.get_current_player().username + " took a direct flight to " + card_name + ". " + str(self.app.board.actions_remaining) + " action(s) remaining.\n"
                self.app.board_frame.log_print(log_str)
                # Prepares for draw phase.
                if self.app.board.actions_remaining == 0:
                    self.disable_buttons()
                    self.app.board_frame.show_draw_phase_button()
            else:
                self.app.board_frame.log_print("Something went wrong. This error should not be reached, as the card is selected directly.\n")
        else:
            self.app.board_frame.log_print("You have not selected a valid card. Please try again.\n")

    def charter_flight_click(self):
        # Allows the player to charter a flight if they have the city card matching their current city.
        self.app.board_frame.log_print("Please select a city to charter a flight to.")
        self.app.board_frame.confirm_city_button["state"] = "normal"
        self.app.board_frame.confirm_city_button.wait_variable(self.app.board_frame.board_var)   
        if self.app.confirmed_city != "":
            if self.app.board.charter_flight(self.app.board.get_current_player(), self.app.confirmed_city):
                self.app.city_viewer_frame.update_info()
                self.app.hand_frame.createWidgets()
                log_str = self.app.board.get_current_player().username + " chartered a flight to " + self.app.selected_city + ". " + str(self.app.board.actions_remaining) + " action(s) remaining.\n"
                self.app.board_frame.log_print(log_str)
                # Prepares for draw phase.
                if self.app.board.actions_remaining == 0:
                    self.disable_buttons()
                    self.app.board_frame.show_draw_phase_button()
            else:
                self.app.board_frame.log_print("You do not have the card matching your current city for this action.\n")
        else:
            self.app.board_frame.log_print("You have not selected a valid city. Please try again.\n")
        self.app.board_frame.confirm_city_button["state"] = "disabled"

    def shuttle_flight_click(self):
        # If the current city has a station, allow the player to select another research station to fly to, then carry out the action.
        self.app.board_frame.log_print("Please select a city with a research station to take a shuttle flight to.")
        self.app.board_frame.confirm_city_button["state"] = "normal"
        self.app.board_frame.confirm_city_button.wait_variable(self.app.board_frame.board_var) 
        if self.app.confirmed_city != "":
            if self.app.board.shuttle_flight(self.app.board.get_current_player(), self.app.confirmed_city):
                self.app.city_viewer_frame.update_info()
                log_str = self.app.board.get_current_player().username + " took a shuttle flight to " + self.app.selected_city + ". " + str(self.app.board.actions_remaining) + " action(s) remaining.\n"
                self.app.board_frame.log_print(log_str)
                # Prepares for draw phase.
                if self.app.board.actions_remaining == 0:
                    self.disable_buttons()
                    self.app.board_frame.show_draw_phase_button()
            else:
                self.app.board_frame.log_print("The selected city does not have a research station. Please try again, or select a new action.\n")
        else:
            self.app.board_frame.log_print("You have not selected a valid city. Please try again.\n")
        self.app.board_frame.confirm_city_button["state"] = "disabled"

    def build_station_click(self):
        self.app.board_frame.log_print("Select a city to build a research station in.\n")

        # If station can be built, simply do so.
        if self.app.board.build_station():
            self.app.city_viewer_frame.update_info()
            self.app.hand_frame.createWidgets()
            log_str = self.app.board.get_current_player().username + " built a research station in " + self.app.board.get_current_player().current_city + ". " + str(self.app.board.actions_remaining) + " action(s) remaining.\n"
            self.app.board_frame.log_print(log_str)
            # Prepares for draw phase.
            if self.app.board.actions_remaining == 0:
                    self.disable_buttons()
                    self.app.board_frame.show_draw_phase_button()
        # If there aren't enough stations left, have the player remove one. Then, they can retry the action.
        elif self.app.board.research_stations_remaining == 0:
            self.app.board_frame.log_print("There are no more available research stations. Please click the city you would like to remove one from.")
            self.app.board_frame.confirm_city_button["state"] = "normal"
            self.app.board_frame.confirm_city_button.wait_variable(self.app.board_frame.board_var)
            if self.app.confirmed_city != "":
                if self.app.board.remove_station(self.app.confirmed_city):
                    self.app.board_frame.log_print("Station removed. You can now build a station.\n")
                else:
                    self.app.board_frame.log_print("This city does not have a research station to remove. Please try again, or select a new action.\n")
            else:
                self.app.board_frame.log_print("You have not selected a valid city. Please try again.\n")
        else:
            self.app.board_frame.log_print("You do not have the required city card to build a station here or that city already has a research station!\n")

    def treat_disease_click(self):
        # Removes one or more disease cubes from the player's current city, using the color_frame to select the color cubes to be removed.
        self.app.board_frame.log_print("Please select a color to cure from the color picker.")
        self.app.color_frame.enable_buttons()
        self.app.color_frame.red_button.wait_variable(self.app.selected_color)
        color = self.app.selected_color.get()
        if color != "":
            if self.app.board.treat_disease(color):
                self.app.city_viewer_frame.update_info()
                self.app.hand_frame.createWidgets()
                if self.app.board.get_current_player().role == 3:
                    log_str = self.app.board.get_current_player().username + " (Medic) removed all " + color + " disease cubes from their city. " + str(self.app.board.actions_remaining) + " action(s) remaining.\n"
                else:
                    log_str = self.app.board.get_current_player().username + " removed a " + color + " disease cube(s) from their city. " + str(self.app.board.actions_remaining) + " action(s) remaining.\n"
                self.app.board_frame.log_print(log_str)
                # Prepares for draw phase.
                if self.app.board.actions_remaining == 0:
                    self.disable_buttons()
                    self.app.board_frame.show_draw_phase_button()
            else:
                self.app.board_frame.log_print("There are no disease cubes of this color in the selected city.\n")
        else:
            self.app.board_frame.log_print("You have not selected a valid color. Please try again.\n")


    def share_knowledge_click(self):
        # Allows one player to select a card to give to another, as long as they are in the same city and the card matches the city they are in.
        # If the giving player is the Researcher, they can give ANY city card to another player in their city.
        self.app.board_frame.log_print("Please select a city card to share with the player in your city.")
        self.app.hand_frame.confirm_card_button.wait_variable(self.app.confirmed_card)
        card_name = self.app.confirmed_card.get()
        giving_player_name = self.app.selected_card_player
        self.app.board_frame.log_print("Now please select the player who will be taking the card.")
        self.app.hand_frame.p1_name_button.wait_variable(self.app.selected_player)
        taking_player_name = self.app.selected_player.get()
        if card_name != "" and giving_player_name != "" and taking_player_name != "" and giving_player_name != taking_player_name:
            for i in self.app.board._player_list:
                if i.username == giving_player_name:
                    giving_player = i
                if i.username == taking_player_name:
                    taking_player = i
            if self.app.board.share_knowledge(giving_player, taking_player, card_name):
                self.app.hand_frame.createWidgets()
                log_str = "Success! " + giving_player_name + " has given " + card_name + " to " + taking_player_name + ". " + str(self.app.board.actions_remaining) + " action(s) remaining.\n"
                self.app.board_frame.log_print(log_str)
                self.app.discard_cards()
                # Prepares for draw phase.
                if self.app.board.actions_remaining == 0:
                    self.disable_buttons()
                    self.app.board_frame.show_draw_phase_button()
            else:
                self.app.board_frame.log_print("Knowledge sharing unsuccessful. You may not share a city with this player, or the card may not match the current city.\n")
        else:
            self.app.board_frame.log_print("You have not selected a valid card or player. Please try again.\n")


    def discover_cure_click(self):
        # If the player has enough cards to turn in...
        if self.app.board.get_current_player().can_turn_in():
            # Select a color, and make sure it's valid (this should always be true).
            self.app.board_frame.log_print("Please select a color disease to cure.")
            self.app.color_frame.enable_buttons()
            self.app.color_frame.red_button.wait_variable(self.app.selected_color)
            color = self.app.selected_color.get()
            if color != "":
                self.app.board_frame.log_print("Please select and confirm five cards of the previously chosen color to turn in.")
                card_num = 0
                discard_list = []
                while card_num < 5:
                    self.app.hand_frame.confirm_card_button.wait_variable(self.app.confirmed_card)
                    card_name = self.app.confirmed_card.get()
                    for x in self.app.board.get_current_player().playerhand:
                        if isinstance(x, CityCard):
                            if x.city == card_name:
                                card_num += 1
                                discard_list.append(x)
                                log_str = self.app.board.get_current_player().username + " has chosen " + card_name + "."
                                self.app.board_frame.log_print(log_str)
                if self.app.board.discover_cure(color, discard_list):
                    log_str = "Success! " + self.app.board.get_current_player().username + " has cured the " + color + " disease. " + str(self.app.board.actions_remaining) + " action(s) remaining.\n"
                    self.app.board_frame.log_print(log_str)
                    # Prepares for draw phase.
                    if self.app.board.actions_remaining == 0:
                        self.disable_buttons()
                        self.app.board_frame.show_draw_phase_button()
                else:
                    self.app.board_frame.log_print("This disease was unable to be eradicated. This could be because you did not have the proper cards, or are not positioned on a research station. Please select a new action.\n")
            else:
                self.app.board_frame.log_print("You did not pick a valid color. This error message should never be seen, so please try again.\n")
        else:
            self.app.board_frame.log_print("You do not have enough cards to turn in. Please try again, or select a new action.\n")

    def role_action_click(self):
        # Dispatcher: may move another pawn as if it were their own, discarding from THEIR OWN hand,
        # or may move any pawn to a city with another pawn.
        if(self.app.board.get_current_player().role == 1):
            self.app.board_frame.log_print("You are the Dispatcher. You may either move another pawn as your own, or move any pawn (including your own) to any other pawn. Please choose an action.")
            card_string = "Please select the event card you would like to store for later.\n\n"
            card_string += "1. Simple Move a player."
            card_string += "2. Direct Flight a player."
            card_string += "3. Charter Flight a player."
            card_string += "4. Shuttle Flight a player."
            card_string += "5. Move one player to another (including yourself)."
            
            answer = simpledialog.askstring("Input", card_string, parent=self)
            if answer != None:
                if answer == "1":
                    self.app.board_frame.log_print("Please select the moving player.")
                    self.app.hand_frame.p1_name_button.wait_variable(self.app.selected_player)
                    moving_player_name = self.app.selected_player.get()
                    if moving_player_name != "":
                        for i in self.app.board._player_list:
                            if i.username == moving_player_name:
                                moving_player = i
                    self.app.board_frame.log_print("Now, please select the city to move to.")
                    self.app.board_frame.confirm_city_button["state"] = "normal"
                    self.app.board_frame.confirm_city_button.wait_variable(self.app.board_frame.board_var) 
                    if self.app.confirmed_city != "":
                        if self.app.board.dispatcher_simple_move(moving_player, self.app.confirmed_city):
                            self.app.city_viewer_frame.update_info()
                            log_str = moving_player_name + " drove (Dispatcher action) to " + self.app.selected_city + ". " + str(self.app.board.actions_remaining) + " action(s) remaining.\n"
                            self.app.board_frame.log_print(log_str)
                            # Prepares for draw phase.
                            if self.app.board.actions_remaining == 0:
                                self.disable_buttons()
                                self.app.board_frame.show_draw_phase_button()
                        else:
                            self.app.board_frame.log_print("The Dispatcher action was unable to be completed. Please try again, or select a new action.\n")
                    else:
                        self.app.board_frame.log_print("You did not select a valid city. Please try again, or select a new action.\n")
                    self.app.board_frame.confirm_city_button["state"] = "disabled"
                elif answer == "2":
                    self.app.board_frame.log_print("Please select the moving player.")
                    self.app.hand_frame.p1_name_button.wait_variable(self.app.selected_player)
                    moving_player_name = self.app.selected_player.get()
                    if moving_player_name != "":
                        for i in self.app.board._player_list:
                            if i.username == moving_player_name:
                                moving_player = i
                    self.app.board_frame.log_print("Now, please select the city to move to.")
                    self.app.board_frame.confirm_city_button["state"] = "normal"
                    self.app.board_frame.confirm_city_button.wait_variable(self.app.board_frame.board_var) 
                    if self.app.confirmed_city != "":
                        if self.app.board.dispatcher_direct_flight(moving_player, self.app.confirmed_city):
                            self.app.city_viewer_frame.update_info()
                            log_str = moving_player_name + " took a direct flight (Dispatcher action) to " + self.app.selected_city + ". " + str(self.app.board.actions_remaining) + " action(s) remaining.\n"
                            self.app.board_frame.log_print(log_str)
                            # Prepares for draw phase.
                            if self.app.board.actions_remaining == 0:
                                self.disable_buttons()
                                self.app.board_frame.show_draw_phase_button()
                        else:
                            self.app.board_frame.log_print("The Dispatcher action was unable to be completed. Please try again, or select a new action.\n")
                    else:
                        self.app.board_frame.log_print("You did not select a valid city. Please try again, or select a new action.\n")
                    self.app.board_frame.confirm_city_button["state"] = "disabled"
                elif answer == "3":
                    self.app.board_frame.log_print("Please select the moving player.")
                    self.app.hand_frame.p1_name_button.wait_variable(self.app.selected_player)
                    moving_player_name = self.app.selected_player.get()
                    if moving_player_name != "":
                        for i in self.app.board._player_list:
                            if i.username == moving_player_name:
                                moving_player = i
                    self.app.board_frame.log_print("Now, please select the city to move to.")
                    self.app.board_frame.confirm_city_button["state"] = "normal"
                    self.app.board_frame.confirm_city_button.wait_variable(self.app.board_frame.board_var) 
                    if self.app.confirmed_city != "":
                        if self.app.board.dispatcher_charter_flight(moving_player, self.app.confirmed_city):
                            self.app.city_viewer_frame.update_info()
                            log_str = moving_player_name + " chartered a flight (Dispatcher action) to " + self.app.selected_city + ". " + str(self.app.board.actions_remaining) + " action(s) remaining.\n"
                            self.app.board_frame.log_print(log_str)
                            # Prepares for draw phase.
                            if self.app.board.actions_remaining == 0:
                                self.disable_buttons()
                                self.app.board_frame.show_draw_phase_button()
                        else:
                            self.app.board_frame.log_print("The Dispatcher action was unable to be completed. Please try again, or select a new action.\n")
                    else:
                        self.app.board_frame.log_print("You did not select a valid city. Please try again, or select a new action.\n")
                    self.app.board_frame.confirm_city_button["state"] = "disabled"
                elif answer == "4":
                    self.app.board_frame.log_print("Please select the moving player.")
                    self.app.hand_frame.p1_name_button.wait_variable(self.app.selected_player)
                    moving_player_name = self.app.selected_player.get()
                    if moving_player_name != "":
                        for i in self.app.board._player_list:
                            if i.username == moving_player_name:
                                moving_player = i
                    self.app.board_frame.log_print("Now, please select the city to move to.")
                    self.app.board_frame.confirm_city_button["state"] = "normal"
                    self.app.board_frame.confirm_city_button.wait_variable(self.app.board_frame.board_var) 
                    if self.app.confirmed_city != "":
                        if self.app.board.dispatcher_shuttle_flight(moving_player, self.app.confirmed_city):
                            self.app.city_viewer_frame.update_info()
                            log_str = moving_player_name + " took a shuttle flight (Dispatcher action) to " + self.app.selected_city + ". " + str(self.app.board.actions_remaining) + " action(s) remaining.\n"
                            self.app.board_frame.log_print(log_str)
                            # Prepares for draw phase.
                            if self.app.board.actions_remaining == 0:
                                self.disable_buttons()
                                self.app.board_frame.show_draw_phase_button()
                        else:
                            self.app.board_frame.log_print("The Dispatcher action was unable to be completed. Please try again, or select a new action.\n")
                    else:
                        self.app.board_frame.log_print("You did not select a valid city. Please try again, or select a new action.\n")
                    self.app.board_frame.confirm_city_button["state"] = "disabled"
                elif answer == "5":
                    self.app.board_frame.log_print("Please select the moving player.")
                    self.app.hand_frame.p1_name_button.wait_variable(self.app.selected_player)
                    moving_player_name = self.app.selected_player.get()
                    if moving_player_name != "":
                        for i in self.app.board._player_list:
                            if i.username == moving_player_name:
                                moving_player = i
                    self.app.board_frame.log_print("Please select the player to move to.")
                    self.app.hand_frame.p1_name_button.wait_variable(self.app.selected_player)
                    to_player_name = self.app.selected_player.get()
                    if to_player_name != "":
                        for i in self.app.board._player_list:
                            if i.username == to_player_name:
                                to_player = i
                    if self.app.board.dispatcher_move_p2p(moving_player, to_player):
                        self.app.city_viewer_frame.update_info()
                        log_str = moving_player_name + " moved (Dispatcher action) to " + to_player_name + ". " + str(self.app.board.actions_remaining) + " action(s) remaining.\n"
                        self.app.board_frame.log_print(log_str)
                        # Prepares for draw phase.
                        if self.app.board.actions_remaining == 0:
                            self.disable_buttons()
                            self.app.board_frame.show_draw_phase_button()
                    else:
                        elf.app.board_frame.log_print("The Dispatcher action was unable to be completed. Please try again, or select a new action.\n")
                else:
                    self.app.board_frame.log_print("You did not select a valid choice. Please try again, or select a new action.\n")
            else:
                self.app.board_frame.log_print("You did not select a valid choice. Please try again, or select a new action.\n")
        # Operations Expert: may move from a research station to ANY city by discarding ANY city card.
        elif(self.app.board.get_current_player().role == 2):
            if (self.app.board.operations_expert_action_complete != True):
                self.app.board_frame.log_print("You are the Operations Expert. If you are on a research station, you may discard any card to move to any city on the board. Please click the card you will discard.")
                self.app.hand_frame.confirm_card_button.wait_variable(self.app.confirmed_card)
                card_name = self.app.confirmed_card.get()
                self.app.board_frame.log_print("Now, select the city you wish to move to.")
                self.app.board_frame.confirm_city_button.wait_variable(self.app.board_frame.board_var) 
                if self.app.board.operations_expert_move(card_name, self.app.confirmed_city):
                    log_str = self.app.board.get_current_player().username + " special moved to " + self.app.selected_city + ". " + str(self.app.board.actions_remaining) + " action(s) remaining.\n"
                    self.app.board_frame.log_print(log_str)
                    # Prepares for draw phase.
                    if self.app.board.actions_remaining == 0:
                        self.disable_buttons()
                        self.app.board_frame.show_draw_phase_button()
                else:
                    self.app.board_frame.log_print("You were not able to fulfill this action. This may be because you were not in a city with a research station, or you did not discard a valid city card.\n")
            else:
                self.app.board_frame.log_print("You have already used your Operations Expert special action once this turn, and can not use it again. Please select a different action.\n")
        # Contingency Planner: may take an event card from the discard and place it on their "role card,"
        # not counting towards their hand limit. This card is REMOVED upon usage.
        elif(self.app.board.get_current_player().role == 5):
            self.app.board_frame.log_print("You are the Contingency Planner. Please pick an event card from the discard pile. This card will be added to your hand, but will not count towards your hand limit. Upon usage, this card will be removed from the game.")
            card_string = "Please select the event card you would like to store for later.\n\n"
            counter = 1
            event_discard_list = list()
            for x in self.app.board.player_discard_pile:
                if isinstance(x, EventCard):
                    card_string += str(counter)
                    card_string += ". "
                    if x.val == 1:
                        card_string += "EVENT - One Quiet Night"
                    elif x.val == 2:
                        card_string += "EVENT - Forecast"
                    elif x.val == 3:
                        card_string += "EVENT - Government Grant"
                    elif x.val == 4:
                        card_string += "EVENT - Airlift"
                    elif x.val == 5:
                        card_string += "EVENT - Resilient Population"
                    else:
                        card_string += "Error - Invalid Value"
                    card_string += "\n"
                    counter += 1
                    event_discard_list.append(x)
            
            answer = simpledialog.askstring("Input", card_string, parent=self)
            if answer != None:
                choice = int(answer) - 1
                card = event_discard_list[choice]
                if contingency_planner_take(card):
                    self.app.board_frame.log_print("Success! The event card has been taken from the discard pile and added to your hand. This will not count towards your total.\n")
                    # Prepares for draw phase.
                    if self.app.board.actions_remaining == 0:
                        self.disable_buttons()
                        self.app.board_frame.show_draw_phase_button()
                else:
                    self.app.board_frame.log_print("The event card could not be taken. You may have made an invalid choice, please try again or select a new action.\n")
            else:
                self.app.board_frame.log_print("You did not select a valid choice. Please try again, or select a new action.\n")
        # No unique action.
        else:
            self.app.board_frame.log_print("Your role does not have a unique action associated with it. Please select a new action.\n")

    def play_event_click(self):
        self.app.board_frame.log_print("Pick an event card to play (any player's card will work\n")
        self.app.confirmed_card.set('')

        # WAIT ON CARD TO BE CLICKED!!!
        self.app.hand_frame.confirm_card_button.wait_variable(self.app.confirmed_card)
        card_name = self.app.confirmed_card.get()

        discard_error = True
        for j in self.app.board.player_list:
            for i in j.playerhand:
                if isinstance(i, EventCard):
                    if (str(i.value) == card_name):
                        discard_error = False
                        card = i
                        player = j

        if discard_error == True:
            self.app.board_frame.log_print("Invalid Card\n")
            return

        if card.value == 1:
            self.play_one_quiet_night(player)
        if card.value == 2:
            self.play_forecast(player)
        if card.value == 3:
            self.play_government_grant(player)
        if card.value == 4:
            self.play_airlift(player)
        if card.value == 5:
            self.play_resilient_population(player)

    def play_one_quiet_night(self, player):
        self.app.board.one_quiet_night(player)
        self.app.board_frame.log_print("The next infect phase will be skipped.\n")
        self.app.hand_frame.confirm_card_button.grid_forget()
        self.app.hand_frame.createWidgets()
    
    def play_forecast(self, player):
        card_string = "Please select the order for the top six cards on the infection deck\nFor example: \"4 5 6 1 2 3\" would put card number 3 on top of the deck\n\n"
        counter = 1
        infection_list = []
        for x in range(6):
            x = self.app.board.infection_deck.top_card()
            card_string += str(counter) 
            card_string += ". " 
            card_string += x.city
            card_string += "\n"
            infection_list.append(x)
            counter += 1
            
        answer = simpledialog.askstring("Input", card_string, parent=self)
        if answer == None:
            answer = "6 5 4 3 2 1"
        choice_list = answer.split()

        rearranged_list = []
        for x in range(6):  
            choice = int(choice_list[x]) - 1
            rearranged_list.append(infection_list[choice])

        if self.app.board.forecast(player, rearranged_list):
            self.app.board_frame.log_print("Successfully reordered the infection discard pile!\n")
            self.app.hand_frame.confirm_card_button.grid_forget()
            self.app.hand_frame.createWidgets()
        else:
            self.app.board_frame.log_print("Something has gone wrong\n")
    
    def play_government_grant(self, player):
        self.app.board_frame.log_print("Select a city to build a research station in.\n")

        self.app.board_frame.confirm_city_button["state"] = "normal"
        self.app.board_frame.confirm_city_button.wait_variable(self.app.board_frame.board_var)

        if self.app.board.government_grant(player, self.app.confirmed_city):
            self.app.board_frame.log_print("Station built successfully.\n")
            self.app.hand_frame.confirm_card_button.grid_forget()
            self.app.hand_frame.createWidgets()

        # If there aren't enough stations left, have the player remove one. Then, they can retry the action.
        elif self.app.board.research_stations_remaining == 0:
            self.app.board_frame.log_print("There are no more available research stations. Please click the city you would like to remove one from.")
            self.app.board_frame.confirm_city_button["state"] = "normal"
            self.app.board_frame.confirm_city_button.wait_variable(self.app.board_frame.board_var)
            if self.app.confirmed_city != "":
                if self.app.board.remove_station(self.app.confirmed_city):
                    self.app.board_frame.log_print("Station removed. You can now build a station.\n")
                else:
                    self.app.board_frame.log_print("This city does not have a research station to remove. Please try again, or select a new action.\n")
            else:
                self.app.board_frame.log_print("You have not selected a valid city. Please try again.\n")
        else:
            self.app.board_frame.log_print("You do not have the required city card to build a station here or that city already has a research station!\n")

        self.app.city_viewer_frame.update_info()
        

    def play_airlift(self, player):
        self.app.board_frame.log_print("Please select the person that is being airlifted.\n")
        self.app.hand_frame.p1_name_button.wait_variable(self.app.selected_player)
        moving_player = self.app.selected_player.get()

        if moving_player == "":
            self.app.board_frame.log_print("Invalid Player.\n")
            return

        for x in self.app.board.player_list:
            if x.username == moving_player:
                moving_player = x

        self.app.board_frame.log_print("Please select a city to airlift to.\n")
        self.app.board_frame.confirm_city_button["state"] = "normal"
        self.app.board_frame.confirm_city_button.wait_variable(self.app.board_frame.board_var)
        city = self.app.confirmed_city

        if self.app.board.airlift(player, moving_player, city):
            self.app.board_frame.log_print(moving_player.username + " successfully moved to " + city)
            self.app.city_viewer_frame.update_info()
            self.app.hand_frame.confirm_card_button.grid_forget()
            self.app.hand_frame.createWidgets()
        else:
            self.app.board_frame.log_print(moving_player.username + " could not move to " + city)

    def play_resilient_population(self, player):
        card_string = "Please select the number of the card you wish to remove from the game\n\n"
        counter = 1
        for x in self.app.board.infection_discard_pile:
            card_string += str(counter)
            card_string += ". " 
            card_string += x.city
            card_string += "\n"
            counter += 1
            
        answer = simpledialog.askstring("Input", card_string, parent=self)
        if answer == None:
            return
        choice = int(answer) - 1

        card = self.app.board.infection_discard_pile[choice]
        if self.app.board.resilient_population(player, card):
            self.app.board_frame.log_print("\nSuccessfully removed the " + card.city + " infection card from the game!\n")
            self.app.hand_frame.confirm_card_button.grid_forget()
            self.app.hand_frame.createWidgets()
        else:
            self.app.board_frame.log_print("\nCould not remove the " + card.city + " infection card from the game.\n")

    def pass_click(self):
        # Sets the player's remaining actions to zero.
        self.app.board.pass_actions()
        # Prepares for draw phase.
        if self.app.board.actions_remaining == 0:
            self.disable_buttons()
            log_str = self.app.board.get_current_player().username + " has passed on the rest of their actions.\n"
            self.app.board_frame.log_print(log_str)
            self.app.board_frame.show_draw_phase_button()

    def reset_click(self):
        self.app.board = copy.deepcopy(self.app.temp_board)
        self.app.board_frame.createWidgets()
        self.app.board_frame.log_next_turn()
        self.app.hand_frame.createWidgets()
        self.app.info_frame.update_info()
        self.app.city_viewer_frame.update_info()
        self.app.action_frame.createWidgets()


# Main routing for testing ActionFrame
if __name__ == "__main__":
    app = PandemicGame.MainApplication()
    frame = ActionFrame(app)
    app.add_test(frame)
    app.master.title("ActionFrame test")
    app.mainloop()
