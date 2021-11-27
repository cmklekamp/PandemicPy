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
        self.simple_move_button = Button(self, text="Drive/Ferry", command=lambda: self.simple_move_click(), font = ("Times New Roman",10))
        self.simple_move_button.place(height = 50, width = 100, x=35, y=25)

        # Direct flight button creation
        self.direct_flight_button = Button(self, text="Direct Flight", command=lambda: self.direct_flight_click(), font = ("Times New Roman",10))
        self.direct_flight_button.place(height = 50, width = 100, x=145, y=25)

        # Charter flight button creation
        self.charter_flight_button = Button(self, text="Charter Flight", command=lambda: self.charter_flight_click(), font = ("Times New Roman",10))
        self.charter_flight_button.place(height = 50, width = 100, x=255, y=25)

        # Shuttle flight button creation
        self.shuttle_flight_button = Button(self, text="Shuttle Flight", command=lambda: self.shuttle_flight_click(), font = ("Times New Roman",10))
        self.shuttle_flight_button.place(height = 50, width = 100, x=365, y=25)

        # Build station button creation
        self.build_station_button = Button(self, text="Build Station", command=lambda: self.build_station_click(), font = ("Times New Roman",10))
        self.build_station_button.place(height = 50, width = 100, x=475, y=25)

        # Treat disease button creation
        self.treat_disease_button = Button(self, text="Treat Disease", command=lambda: self.treat_disease_click(), font = ("Times New Roman",10))
        self.treat_disease_button.place(height = 50, width = 100, x=585, y=25)

        # Share knowledge button creation
        self.share_knowledge_button = Button(self, text="Share Knowledge", command=lambda: self.share_knowledge_click(), font = ("Times New Roman",10))
        self.share_knowledge_button.place(height = 50, width = 100, x=695, y=25)

        # Discover cure button creation
        self.discover_cure_button = Button(self, text="Discover Cure", command=lambda: self.discover_cure_click(), font = ("Times New Roman",10))
        self.discover_cure_button.place(height = 50, width = 100, x=805, y=25)

        # Pass button creation
        self.pass_button = Button(self, text="Pass", command=lambda: self.pass_click(), font = ("Times New Roman",10))
        self.pass_button.place(height = 50, width = 100, x=915, y=25)


    # Button click events
    # Remember to add log_print functionality (i.e. make sure actions print to the log)
    def simple_move_click(self):
        self.app.board_frame.log_print("Please select a city to drive to.")
        # self.app.board_frame.wait_variable(button_clicked)
        # if self.app.board.simple_move(self.app.board.get_current_player(), self.app.selected_city):
        #     log_str = self.app.board.get_current_player().username + " drove to " + self.app.selected_city + "\n"
        #     self.app.board_frame.log_print(log_str)
        #     if self.app.board.actions_remaining == 0:
        #         self.app.board_frame.show_draw_phase_button()
        # else:
        #     self.app.board_frame.log_print("Invalid city. You may only drive to a city you are next to.")

    def direct_flight_click(self):
        self.app.board_frame.log_print("Please select a city to take a direct flight to.")

    def charter_flight_click(self):
        self.app.board_frame.log_print("Please select a city to charter a flight to.")

    def shuttle_flight_click(self):
        self.app.board_frame.log_print("Please select a city to take a shuttle flight to.")

    def build_station_click(self):
        pass

    def treat_disease_click(self):
        pass

    def share_knowledge_click(self):
        pass

    def discover_cure_click(self):
        pass

    def pass_click(self):
        self.app.board.pass_actions()
        if self.app.board.actions_remaining == 0:
            log_str = self.app.board.get_current_player().username + " has passed on the rest of their actions.\n"
            self.app.board_frame.log_print(log_str)
            self.app.board_frame.show_draw_phase_button()


# Main routing for testing ActionFrame
if __name__ == "__main__":
    app = PandemicGame.MainApplication()
    frame = ActionFrame(app)
    app.add_test(frame)
    app.master.title("ActionFrame test")
    app.mainloop()
