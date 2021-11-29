# - - - - - - - - - - - - - - - - - - - -
# COP 4521 -- Term Project
# Daniel Fletcher, Connor Klekamp, Jacob Gregie
# PANDEMIC board game implementation
# - - - - - - - - - - - - - - - - - - - -

# * * * PandemicGame.py * * *
# GUI implementation of the Pandemic game
# Run this file to play the project as intended

# Relevant import statements -- custom classes (logic)
from Cards import *
from Decks import *
from City import *
from Player import *
from GameBoard import *

# Relevant import statements -- custom classes (GUI)
import MainMenu
import Board
import Actions
import PlayerHands
import Database
import InfoDisplay
import CityViewer
import ColorDisplay
import EndGame

# Relevant import statements -- tkinter
from tkinter import *
from tkinter.font import Font
from tkinter import StringVar

# Main application class
class MainApplication(Frame):

    # Overridden constructor
    def __init__(self, master=None):
        Frame.__init__(self, master, height=720, width=1280)
        self.grid(sticky=N+S+E+W)
        self.grid_propagate(0)
        self.createWidgets()

    # add_test()
    # Adds a custom, inherited Frame to the application
    # Used purely for testing purposes (i.e., testing the custom Frames individually)
    def add_test(self, custom_frame):
        self.menu_frame.grid_forget()
        self.custom = custom_frame
        self.custom.grid(row=0, column=0)

    # createWidgets()
    # Creates widgets upon initialization in constructor
    def createWidgets(self):
        # Set up grid resizing and stretching properties
        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        for x in range(0, 6):
            self.rowconfigure(x, weight=1)
        self.columnconfigure(0, weight=1)

        # Set up MenuFrame
        self.menu_frame = MainMenu.MenuFrame(self)
        self.menu_frame.grid(row=0, column=0)

        # Set up DatabaseFrame
        self.database_frame = Database.DatabaseFrame(self)
    
    # start_game()
    # Starts the game based on call from MenuFrame
    def start_game(self, playercount, playernames, difficulty):
        # Initialize game board
        self.board = GameBoard(playercount, playernames, difficulty)
        self.selected_city = ""
        self.confirmed_city = ""
        self.selected_player = StringVar('')
        self.selected_card_player = ""
        self.selected_card = ""
        self.confirmed_card = StringVar('')
        self.selected_color = StringVar('')

        # copy of board used for resetting
        self.temp_board = copy.deepcopy(self.board)

        self.info_frame = InfoDisplay.InfoFrame(self)
        self.info_frame.grid(row=0, column=1)

        self.board_frame = Board.BoardFrame(self)
        self.board_frame.grid(row=1, column=1)
        self.board_frame.log_next_turn()
        self.board_frame.confirm_city_button["state"] = "disabled"

        self.action_frame = Actions.ActionFrame(self)
        self.action_frame.grid(row=2, column=1)

        self.hand_frame = PlayerHands.HandFrame(self)
        self.hand_frame.grid(row=0, column=2, rowspan=3)

        self.city_viewer_frame = CityViewer.CityViewerFrame(self)
        self.city_viewer_frame.grid(row=1, column=0, rowspan=3)

        self.color_frame = ColorDisplay.ColorFrame(self)
        self.color_frame.grid(row=2, column=2)
        

    # player_draw_phase()
    # Handles end of turn actions
    def draw_phase(self):
        # Disable reset button.
        self.action_frame.reset_button["state"] = "disabled"

        # Check if the game is over
        if (self.board.victory == True or self.board.defeat == True):
            self.end_game()

        # draw cards
        player = self.board.get_current_player()
        self.board.draw_cards()

        # show acquired cards
        temp = 2 - self.board.epidemics_occuring
        for x in range(temp):
            card = player.playerhand[-(x+1)]
            if(isinstance(card, CityCard)):
                self.board_frame.log_print(player.username + " acquired: " + card.city + " / " + card.color)
            else:
                self.board_frame.log_print(player.username + " acquired: " + "Event Card " + str(card.value))
        self.board_frame.log_print("")
        self.hand_frame.createWidgets()

        # epidemic time
        if (self.board.epidemics_occuring != 0):
            self.epidemic_phase()
 
        if (player.over_hand_limit() == True):
            self.discard_cards()

        self.board_frame.show_infect_phase_button()

    # discard_cards()
    # Discard cards if the player is over the hand limit.
    def discard_cards(self):
        player = self.board.get_current_player()
        while player.over_hand_limit() == True:
            self.board_frame.log_print("You are over the hand limit. Please click City cards to discard them, or Event cards to play them, until you are down to 7 cards.\n")
            self.confirmed_card.set('')

            # WAIT ON CARD TO BE CLICKED!!!
            self.hand_frame.confirm_card_button.wait_variable(self.confirmed_card)
            card_name = self.confirmed_card.get()

            discard_error = True
            for i in player.playerhand:
                if isinstance(i, CityCard):
                    if (i.city == card_name):
                        discard_error = False
                        card = i
                else: 
                    if (str(i.value) == card_name):
                        discard_error = False
                        card = i

            if discard_error == True:
                self.board_frame.log_print("Invalid Card\n")
                continue

            if (isinstance(card, CityCard)):
                self.board.discard(card)
                log_str = player.username + " has discarded " + card_name + ".\n"
                self.board_frame.log_print(log_str)

            elif (isinstance(card, EventCard)):
                if (card.value == 1):
                    self.action_frame.play_one_quiet_night(player)
                elif (card.value == 2):
                    self.action_frame.play_forecast(player)
                elif (card.value == 3):
                    self.action_frame.play_government_grant(player)
                elif (card.value == 4):
                    self.action_frame.play_airlift(player)
                elif (card.value == 5):
                    self.action_frame.play_resilient_population(player)
                    
            self.hand_frame.confirm_card_button.grid_forget()
            self.hand_frame.createWidgets()

    # epidemic_phase()
    # epidemic time
    def epidemic_phase(self):
        while (self.board.epidemics_occuring != 0):
            # Update Log
            self.board_frame.log_epidemic()
            self.action_frame.play_event_button["state"] = "disabled"

            # Start epidemic and display infected city
            self.board.epidemic()
            infected_city = self.board.infection_discard_pile[-1]
            self.board_frame.log_infect(infected_city.city)

            # -- SHOW WHAT CITIES HAD AN OUTBREAK --
            for x in self.board.city_list:
                if self.board.city_list[x].had_outbreak == True:
                    self.board_frame.log_outbreak(x)

            self.info_frame.update_info()
            self.city_viewer_frame.update_info()

            if (self.board.defeat == True):
                self.end_game() 

            # -- PLAY RESILIENT POPULATION --
            for x in self.board.player_list:
                for y in x.playerhand:
                    if (isinstance(y, EventCard) and y.value == 5):
                        resilient_population_player = x
                        self.board_frame.resilient_population_click(resilient_population_player)
            
            self.intensify_phase()

    # intensify_phase()
    # Intesify step of epidemic
    def intensify_phase(self):
        self.board.intensify()

    # infect_draw_phase()
    # -- INFECT CITIES --
    def infect_phase(self):
        if (self.board.skip_infect_cities == False):
            for x in range(self.board.infection_rate):
                self.board.draw_infection_card()
                self.board_frame.log_infect(self.board.infection_discard_pile[-1].city)

                for x in self.board.city_list:
                    if self.board.city_list[x].had_outbreak == True:
                        self.board_frame.log_outbreak(x)
        else:
            self.board.skip_infect_cities = False
            self.board_frame.log_print("Thankfully, the infect phase has been skipped.")

        self.info_frame.update_info()
        self.city_viewer_frame.update_info()

        if (self.board.defeat == True):
            self.end_game() 
            
        # Re-enable the action buttons.
        self.action_frame.simple_move_button["state"] = "normal"
        self.action_frame.direct_flight_button["state"] = "normal"
        self.action_frame.charter_flight_button["state"] = "normal"
        self.action_frame.shuttle_flight_button["state"] = "normal"
        self.action_frame.build_station_button["state"] = "normal"
        self.action_frame.treat_disease_button["state"] = "normal"
        self.action_frame.share_knowledge_button["state"] = "normal"
        self.action_frame.discover_cure_button["state"] = "normal"
        self.action_frame.role_action_button["state"] = "normal"
        self.action_frame.play_event_button["state"] = "normal"
        self.action_frame.pass_button["state"] = "normal"
        self.action_frame.reset_button["state"] = "normal"

        # Progress to next turn
        self.board.next_turn()
        self.temp_board = copy.deepcopy(self.board)
        self.hand_frame.createWidgets()
        self.board_frame.log_print("")
        self.board_frame.log_next_turn()

    def end_game(self):
        # Clear elements currently on-screen
        items_to_delete = (self.info_frame, self.board_frame, self.action_frame, self.city_viewer_frame, self.hand_frame)
        for item in items_to_delete:
            item.grid_forget()

        # Add endgame screen
        self.end_frame = EndGame.EndGameFrame(self, self.board.victory)
        self.end_frame.grid(row=0, column=0)


# Main game loop
if __name__ == "__main__":
    app = MainApplication()
    app.master.title("Pandemic")
    app.mainloop()
