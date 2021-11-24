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

# Relevant import statements -- tkinter
from tkinter import *
from tkinter.font import Font


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
    
    # start_game()
    # Starts the game based on call from MenuFrame
    def start_game(self, playercount, playernames, difficulty):
        # Initialize game board
        self.board = GameBoard(playercount, playernames, difficulty)

        # -- DISPLAYS FOR TESTING --
        self.title_frame = Frame()
        self.title_frame.grid(row=0, column=0)
        self.heading_font = Font(family="Arial", size=24, weight="normal")
        self.header_text = Label(self.title_frame, text="Player usernames, as retrieved from GameBoard class:", font=self.heading_font)
        self.header_text.grid(row=0, column=0, pady=25)
        self.name_labels = list()
        counter = 0
        for player in self.board.player_list:
            self.name_labels.append(Label(self.title_frame, text=player.username, font=self.heading_font))
            self.name_labels[counter].grid(row=counter + 1, column=0)
            counter += 1



# Main game loop
if __name__ == "__main__":
    app = MainApplication()
    app.master.title("Pandemic")
    app.mainloop()
