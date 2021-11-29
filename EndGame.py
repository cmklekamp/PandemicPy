# - - - - - - - - - - - - - - - - - - - -
# COP 4521 -- Term Project
# Daniel Fletcher, Connor Klekamp, Jacob Gregie
# PANDEMIC board game implementation
# - - - - - - - - - - - - - - - - - - - -

# * * * EndGame.py * * *
# Implements custom EndGameFrame class
# Used for displaying victory/defeat information at the end of a game


# Relevant import statements -- custom classes (logic)
from Cards import *
from Decks import *
from City import *
from Player import *
from GameBoard import *

# Relevant import statements -- custom classes (GUI)
import PandemicGame

# Relevant import statements -- tkinter
from tkinter import *
from tkinter.font import Font


# Custom frame: CityViewerFrame
class EndGameFrame(Frame):

    # Overridden constructor
    def __init__(self, app, win_status, master=None):
        self.win_status = win_status
        if(self.win_status == True):
            Frame.__init__(self, master, bg="green")
        else:
            Frame.__init__(self, master, bg="red")
        self.app = app
        self.createWidgets()


    # createWidgets()
    # Creates widgets upon initialization in constructor
    def createWidgets(self):
        # Initialize fonts to be used
        self.title_font = Font(family="Times New Roman", size=72, weight="bold")
        self.report_font = Font(family="Times New Roman", size=24, weight="normal")
        self.button_font = Font(family="Arial", size=14, weight="normal")

        # Create strings based on win status
        if(self.win_status == True):
            win_string = "VICTORY"
            report_string = "You won the game in " + str(self.app.board.turn_number) + " turns"
        else:
            win_string = "DEFEAT"
            report_string = "You lost the game in " + str(self.app.board.turn_number) + " turns"

        # Create labels for messages
        if(self.win_status == True):
            self.title_text = Label(self, text=win_string, font=self.title_font, bg="green")
            self.message_text = Label(self, text=report_string, font=self.report_font, bg="green")
        else:
            self.title_text = Label(self, text=win_string, font=self.title_font, bg="red")
            self.message_text = Label(self, text=report_string, font=self.report_font, bg="red")
        self.title_text.grid(row=0, column=0, bg=None)
        self.message_text.grid(row=1, column=0, bg=None)

        # Create button for returning to main menu
        self.return_button = Button(self, text="Return to Menu", command=self.return_to_menu, font=self.button_font)
        self.return_button.grid(row=2, column=0, pady=40)

        # Update database with board stats
        self.app.database_frame.update_database()


    # return_to_menu()
    # Clears screen and returns to main menu
    def return_to_menu(self):
        self.title_text.grid_forget()
        self.message_text.grid_forget()
        self.return_button.grid_forget()
        self.grid_forget()
        self.app.menu_frame.createWidgets()


# Main routing for testing InfoFrame
if __name__ == "__main__":
    app = PandemicGame.MainApplication()
    app.board = GameBoard(3, ["Connor", "Daniel", "Jacob"])
    frame = EndGameFrame(app, False)
    app.add_test(frame)
    app.master.title("EndGameFrame test")
    app.mainloop()