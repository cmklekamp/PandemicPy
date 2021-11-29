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
        pass

    def share_knowledge_click(self):
        self.app.board_frame.log_print("Please select a city card to share with the player in your city.")
        self.app.hand_frame.confirm_card_button.wait_variable(self.app.hand_frame.card_var)
        if self.app.confirmed_card != "":
            self.app.board_frame.log_print("Now please select the player who will be taking the card.")
        else:
            self.app.board_frame.log_print("You have not selected a valid card. Please try again.\n")
        pass
        # select the city card from any player's hand, recording who's hand it's from as well as the giving player
        # select the player name of the taking player, and then pass them both into the function (this will allow for the researcher's role to work as intended)
        # if false, give appropriate error message; if true, proceed as normal

    def discover_cure_click(self):
        pass

    def role_action_click(self):
        # Dispatcher: may move another pawn as if it were their own, discarding from THEIR OWN hand,
        # or may move any pawn to a city with another pawn.
        if(self.app.board.get_current_player().role == 1):
            self.app.board_frame.log_print("You are the Dispatcher. You may either move another pawn as your own, or move any pawn (including your own) to any other pawn. Please click the player's name and do one of these actions.")
        # Operations Expert: may move from a research station to ANY city by discarding ANY city card.
        elif(self.app.board.get_current_player().role == 2):
            self.app.board_frame.log_print("You are the Operations Expert. If you are on a research station, you may discard any card to move to any city on the board. Please click the card you will discard.")
        # Contingency Planner: may take an event card from the discard and place it on their "role card,"
        # not counting towards their hand limit. This card is REMOVED upon usage.
        elif(self.app.board.get_current_player().role == 5):
            self.app.board_frame.log_print("You are the Contingency Planner. Please pick an event card from the discard pile. This card will be added to your hand, but will not count towards your hand limit. Upon usage, this card will be removed from the game.")
        # No unique action.
        else:
            self.app.board_frame.log_print("Your role does not have a unique action associated with it. Please select a new action.")

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
            self.board_frame.log_print("Invalid Card\n")
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
        pass
    
    def play_government_grant(self, player):
        self.app.board_frame.log_print("Select a city to build a research station in.\n")

        self.app.board_frame.confirm_city_button["state"] = "normal"
        self.app.board_frame.confirm_city_button.wait_variable(self.app.board_frame.board_var)

        if self.app.board.government_grant(player, self.app.confirmed_city):
            self.app.board_frame.log_print("Station built successfully.\n")

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

    def play_airlift(self, player):
        self.app.board_frame.log_print("Please select the person that is being airlifted.")
        self.app.hand_frame.p1_name_button.wait_variable(self.app.selected_player)
        moving_player = self.app.selected_player

        self.app.board_frame.log_print("Please select a city to airlift to.")
        self.app.board_frame.confirm_city_button["state"] = "normal"
        self.app.board_frame.confirm_city_button.wait_variable(self.app.board_frame.board_var)
        city = self.app.confirmed_city

        if self.app.board.airlift(player, moving_player, city):
            pass

    def play_resilient_population(self, player):
        pass

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
        self.app.info_frame.createWidgets()
        self.app.city_viewer_frame.update_info()
        self.app.action_frame.createWidgets()


# Main routing for testing ActionFrame
if __name__ == "__main__":
    app = PandemicGame.MainApplication()
    frame = ActionFrame(app)
    app.add_test(frame)
    app.master.title("ActionFrame test")
    app.mainloop()
