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


    # Button click events
    # Remember to add log_print functionality (i.e. make sure actions print to the log)

    # AFTER EVERY ACTION, MAY HAVE TO RETURN SELECTED CITY AND CARD TO EMPTY
    # AFTER THE ACTION PHASE, DISABLE BUTTONS UNTIL NEXT ACTION PHASE

    def simple_move_click(self):
        self.app.board_frame.log_print("Please select a city to drive to.")
        self.app.board_frame.buttons[i].wait_variable(var)
        if self.app.board.simple_move(self.app.board.get_current_player(), self.app.selected_city):
            log_str = self.app.board.get_current_player().username + " drove to " + self.app.selected_city + "\n"
            self.app.board_frame.log_print(log_str)
            if self.app.board.actions_remaining == 0:
                self.app.board_frame.show_draw_phase_button()
        else:
            self.app.board_frame.log_print("Invalid city. You may only drive to a city you are next to.")

    def direct_flight_click(self):
        self.app.board_frame.log_print("Please select a city card to take a direct flight to.")
        # self.app.hand_frame.currentplayerhandetc.wait_variable(var)
        if self.app.board.direct_flight(self.app.board.get_current_player(), CITYCARDNAME):
            log_str = self.app.board.get_current_player().username + " took a direct flight to " + CITYCARDNAME + "\n"
            self.app.board_frame.log_print(log_str)
            if self.app.board.actions_remaining == 0:
                self.app.board_frame.show_draw_phase_button()
        else:
            self.app.board_frame.log_print("Something went wrong. This error should not be reached, as the card is selected directly.")

    def charter_flight_click(self):
        self.app.board_frame.log_print("Please select a city to charter a flight to.")
        self.app.board_frame.buttons[i].wait_variable(var)
        if self.app.board.charter_flight(self.app.board.get_current_player(), self.app.selected_city):
            log_str = self.app.board.get_current_player().username + " chartered a flight to " + self.app.selected_city + "\n"
            self.app.board_frame.log_print(log_str)
            if self.app.board.actions_remaining == 0:
                self.app.board_frame.show_draw_phase_button()
        else:
            self.app.board_frame.log_print("You do not have the card matching your current city for this action.")

    def shuttle_flight_click(self):
        if self.app.board.get_current_player().current_city.has_station():
            self.app.board_frame.log_print("Please select a city with a research station to take a shuttle flight to.")
            self.app.board_frame.buttons[i].wait_variable(var)
            if self.app.board.shuttle_flight(self.app.board.get_current_player(), self.app.selected_city):
                log_str = self.app.board.get_current_player().username + " took a shuttle flight to " + self.app.selected_city + "\n"
                self.app.board_frame.log_print(log_str)
                if self.app.board.actions_remaining == 0:
                    self.app.board_frame.show_draw_phase_button()
            else:
                self.app.board_frame.log_print("The selected city does not have a research station. Please try again, or select a new action.")
        else:
            self.app.board_frame.log_print("Your current city does not have a research station. Please select a new action.")

    def build_station_click(self):
        if board.build_station():
            log_str = self.app.board.get_current_player().username + " built a research station in " + self.app.board.get_current_player().current_city
            self.app.board_frame.log_print(log_str)
        elif board.research_stations_remaining == 0:
            self.app.board_frame.log_print("There are no more available research stations. Please click the city you would like to remove one from.")
            # SELECT CITY HERE
        else:
            self.app.board_frame.log_print("You do not have the required city card to build a station here!")

    def treat_disease_click(self):
        pass

    def share_knowledge_click(self):
        pass
        # select the city card from any player's hand, recording who's hand it's from as well as the giving player
        # select the player name of the taking player, and then pass them both into the function (this will allow for the researcher's role to work as intended)
        # if false, give appropriate error message; if true, proceed as normal

    def discover_cure_click(self):
        pass

    def role_action_click(self):
        pass

    def play_event_click(self):
        pass

    def pass_click(self):
        self.app.board.pass_actions()
        if self.app.board.actions_remaining == 0:
            log_str = self.app.board.get_current_player().username + " has passed on the rest of their actions.\n"
            self.app.board_frame.log_print(log_str)
            self.app.board_frame.show_draw_phase_button()

    def reset_click(self):
        pass


# Main routing for testing ActionFrame
if __name__ == "__main__":
    app = PandemicGame.MainApplication()
    frame = ActionFrame(app)
    app.add_test(frame)
    app.master.title("ActionFrame test")
    app.mainloop()
