# - - - - - - - - - - - - - - - - - - - -
# COP 4521 -- Term Project
# Daniel Fletcher, Connor Klekamp, Jacob Gregie
# PANDEMIC board game implementation
# - - - - - - - - - - - - - - - - - - - -

# * * * Database.py * * *
# Implements database of game history
# Also implements DatabaseFrame for displaying database to screen from main menu

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

# Relevant import statements -- SQL and file logic
import os
import sqlite3


# Database frame class
class DatabaseFrame(Frame):
    # Overridden constructor
    def __init__(self, app, master=None):
        Frame.__init__(self, master)
        self.app = app
        self.createWidgets()


    # createWidgets()
    # Creates widgets upon initialization in constructor
    def createWidgets(self):
        # Set up fonts for use by display functions
        self.title_font = Font(family="Times New Roman", size=24, weight="bold")
        self.header_font = Font(family="Times New Roman", size=12, weight="bold")
        self.data_font = Font(family="Times New Roman", size=12, weight="normal")
        self.button_font = Font(family="Arial", size=16, weight="normal") 

        # Initialize values for paging
        self.top_data_row = 0
        self.bottom_data_row = 10


    # create_database()
    # Creates a database file with the relevant data tables
    def create_database(self):
        # Check if file already exists
        pathname = "GameHistory.db"
        if(os.path.isfile(pathname) == False):
            # If file does not exist, create the database tables!
            connection = sqlite3.connect("GameHistory.db")
            connection.execute("CREATE TABLE SystemStats (GameNum VARCHAR(20), Players VARCHAR(100), Difficulty VARCHAR(30), WinStatus VARCHAR(10), Turns INTEGER(5))")
            connection.execute("CREATE TABLE PlayerStats (Username VARCHAR(50), Wins INTEGER(3), Losses INTEGER(3), TotalGames INTEGER(3))")
            connection.close()


    # update_database()
    # Updates database with information from the Game Board
    def update_database(self):
        # Create database if it does not already exist
        self.create_database()

        # Update both databases
        self.update_system_stats()
        self.update_player_stats()


    # update_system_stats()
    # Helper function for updating the SystemStats database
    def update_system_stats(self):
        # Setup connection
        connection = sqlite3.connect("GameHistory.db")
        data_cursor = connection.cursor()
        cursor = connection.cursor()

        # Extract data from current game session
        data_cursor.execute("SELECT COUNT(*) FROM SystemStats")
        data = data_cursor.fetchall()
        game_num = "Game " + str(data[0][0] + 1)
        players = list()
        player_string = ""
        difficulty_string = ""
        win_string = ""
        for i in range(len(self.app.board.player_list)):
            players.append(self.app.board.player_list[i].username)
            player_string += self.app.board.player_list[i].username
            if(i != len(self.app.board.player_list) - 1):
                player_string += ", "
        if(self.app.board.difficulty == 4):
            difficulty_string = "4 - Introductory"
        elif(self.app.board.difficulty == 5):
            difficulty_string = "5 - Standard"
        else:
            difficulty_string = "6 - Heroic"
        if(self.app.board.victory == True):
            win_string = "Win"
        else:
            win_string = "Lose"
        turn_count = int(self.app.board.turn_number)

        # Insert data into SystemStats table for this session
        cursor.execute("INSERT INTO SystemStats VALUES (?,?,?,?,?)", (game_num, player_string, difficulty_string, win_string, turn_count))
        connection.commit()
        connection.close()


    # update_player_stats()
    # Helper function for updating the PlayerStats database
    def update_player_stats(self):
        # Setup connection
        connection = sqlite3.connect("GameHistory.db")
        cursor = connection.cursor()
        players_in_database = list()

        # Loop through players currently in database
        for row in cursor.execute("SELECT * FROM PlayerStats"):
            players_in_database.append(row[0])

        # Loop through players from current game, updating database accordingly
        data_cursor = connection.cursor()
        for player in self.app.board.player_list:
            if(player.username in players_in_database):
                # If the player is already in the database, increment appropriate values by 1
                for row in data_cursor.execute("SELECT * FROM PlayerStats"):
                    if(row[0] == player.username):
                        wins = row[1]
                        losses = row[2]
                        games = row[3]
                        break
                games += 1
                if(self.app.board.victory == True):
                    wins += 1
                else:
                    losses +=1
                cursor.execute("UPDATE PlayerStats SET Wins=?, Losses=?, TotalGames=? WHERE Username=?", (wins, losses, games, player.username))
            else:
                # If the player is NOT already in the database, set appropriate values to 0 or 1
                username = player.username
                wins = 0
                losses = 0
                games = 1
                if(self.app.board.victory == True):
                    wins += 1
                else:
                    losses +=1
                cursor.execute("INSERT INTO PlayerStats VALUES (?,?,?,?)", (username, wins, losses, games))

        # Insert data into PlayerStats table for this session
        connection.commit()
        connection.close()

    
    # display_system_stats()
    # Displays the system stats database table to the screen
    def display_system_stats(self):
        # Title text (show system stats first)
        self.title_text = Label(self, text="Game History: System Stats", font=self.title_font)
        self.title_text.grid(row=0, column=0, pady=50, columnspan=5)

        # Extract rows from database
        self.datalist = list()
        pathname = "GameHistory.db"
        if(os.path.isfile(pathname) == True):
            connection = sqlite3.connect("GameHistory.db")
            cursor = connection.cursor()
            for row in cursor.execute("SELECT * FROM SystemStats"):
                self.datalist.append(row)
            connection.close()

        # Create and display header
        self.header_list = list()
        self.header_list.append(Label(self, text="Game #", font=self.header_font, anchor="w"))
        self.header_list[-1].grid(row=1, column=0, pady=5, padx=40)
        self.header_list.append(Label(self, text="Players", font=self.header_font, anchor="w"))
        self.header_list[-1].grid(row=1, column=1, pady=5, padx=40)
        self.header_list.append(Label(self, text="Difficulty", font=self.header_font, anchor="w"))
        self.header_list[-1].grid(row=1, column=2, pady=5, padx=40)
        self.header_list.append(Label(self, text="Win/Lose", font=self.header_font, anchor="w"))
        self.header_list[-1].grid(row=1, column=3, pady=5, padx=40)
        self.header_list.append(Label(self, text="Turns Taken", font=self.header_font, anchor="w"))
        self.header_list[-1].grid(row=1, column=4, pady=5, padx=40)

        # Add rows to grid
        self.data_labels = list()
        row_num = 2
        for row in self.datalist[self.top_data_row:self.bottom_data_row]:
            # Convert column values to strings
            game_string = str(row[0])
            players_string = str(row[1])
            difficulty_string = str(row[2])
            win_string = str(row[3])
            turn_string = str(row[4])

            # Add each label to the label list
            self.data_labels.append(Label(self, text=game_string, font=self.data_font, anchor="w"))
            self.data_labels[-1].grid(row=row_num, column=0, pady=2)
            self.data_labels.append(Label(self, text=players_string, font=self.data_font, anchor="w"))
            self.data_labels[-1].grid(row=row_num, column=1, pady=2)
            self.data_labels.append(Label(self, text=difficulty_string, font=self.data_font, anchor="w"))
            self.data_labels[-1].grid(row=row_num, column=2, pady=2)
            self.data_labels.append(Label(self, text=win_string, font=self.data_font, anchor="w"))
            self.data_labels[-1].grid(row=row_num, column=3, pady=2)
            self.data_labels.append(Label(self, text=turn_string, font=self.data_font, anchor="w"))
            self.data_labels[-1].grid(row=row_num, column=4, pady=2)
            row_num += 1

        # If row_num is still 2, database is empty (no data to display)
        if(row_num == 2):
            row_string = "\n\n--- no data to display ---"
            self.data_labels.append(Label(self, text=row_string, font=self.data_font))
            self.data_labels[-1].grid(row=row_num, column=0, pady=2, columnspan=5)
            row_num += 1

        # Add spacer
        self.spacer = Label(self, text=" ")
        self.spacer.grid(row=row_num, column=0, pady=50)
        row_num += 1

        # Display paging buttons
        row_num = self.display_paging_buttons(row_num, (3, 0), "system")

        # Switch stats button
        self.switch_button = Button(self, text="Player Stats", command=lambda: self.update_paging_then_display("player"), font=self.button_font, padx=55)
        self.switch_button.grid(row=row_num, column=0, pady=15, columnspan=2)

        # Return to menu button
        self.return_button = Button(self, text="Return to Menu", command=self.return_to_menu, font=self.button_font, padx=55)
        self.return_button.grid(row=row_num, column=3, pady=15, columnspan=2)


    # display_player_stats()
    # Displays the player stats database table to the screen
    def display_player_stats(self):
        # First, clear the screen
        self.clear_screen()

        # Title text (show system stats first)
        self.title_text = Label(self, text="Game History: Player Stats", font=self.title_font)
        self.title_text.grid(row=0, column=0, pady=50, columnspan=4)

        # Extract rows from database
        self.datalist = list()
        pathname = "GameHistory.db"
        if(os.path.isfile(pathname) == True):
            connection = sqlite3.connect("GameHistory.db")
            cursor = connection.cursor()
            for row in cursor.execute("SELECT * FROM PlayerStats"):
                self.datalist.append(row)
            connection.close()

        # Create and display header
        self.header_list = list()
        self.header_list.append(Label(self, text="Player", font=self.header_font, anchor="w"))
        self.header_list[-1].grid(row=1, column=0, pady=5, padx=40)
        self.header_list.append(Label(self, text="Wins", font=self.header_font, anchor="w"))
        self.header_list[-1].grid(row=1, column=1, pady=5, padx=40)
        self.header_list.append(Label(self, text="Losses", font=self.header_font, anchor="w"))
        self.header_list[-1].grid(row=1, column=2, pady=5, padx=40)
        self.header_list.append(Label(self, text="Total Games Played", font=self.header_font, anchor="w"))
        self.header_list[-1].grid(row=1, column=3, pady=5, padx=40)

        # Add rows to grid
        self.data_labels = list()
        row_num = 2
        for row in self.datalist[self.top_data_row:self.bottom_data_row]:
            # Convert column values to strings
            username_string = str(row[0])
            wins_string = str(row[1])
            losses_string = str(row[2])
            total_string = str(row[3])

            # Add each label to the label list
            self.data_labels.append(Label(self, text=username_string, font=self.data_font, anchor="w"))
            self.data_labels[-1].grid(row=row_num, column=0, pady=2)
            self.data_labels.append(Label(self, text=wins_string, font=self.data_font, anchor="w"))
            self.data_labels[-1].grid(row=row_num, column=1, pady=2)
            self.data_labels.append(Label(self, text=losses_string, font=self.data_font, anchor="w"))
            self.data_labels[-1].grid(row=row_num, column=2, pady=2)
            self.data_labels.append(Label(self, text=total_string, font=self.data_font, anchor="w"))
            self.data_labels[-1].grid(row=row_num, column=3, pady=2)
            row_num += 1

        # If row_num is still 2, database is empty (no data to display)
        if(row_num == 2):
            row_string = "\n\n--- no data to display ---"
            self.data_labels.append(Label(self, text=row_string, font=self.data_font))
            self.data_labels[-1].grid(row=row_num, column=0, pady=2, columnspan=4)
            row_num += 1

        # Add spacer
        self.spacer = Label(self, text=" ")
        self.spacer.grid(row=row_num, column=0, pady=50)
        row_num += 1

        # Display paging buttons
        row_num = self.display_paging_buttons(row_num, (2, 0), "player")

        # Switch stats button
        self.switch_button = Button(self, text="System Stats", command=lambda: self.update_paging_then_display("system"), font=self.button_font, padx=55)
        self.switch_button.grid(row=row_num, column=0, pady=15, columnspan=2)

        # Return to menu button
        self.return_button = Button(self, text="Return to Menu", command=self.return_to_menu, font=self.button_font, padx=55)
        self.return_button.grid(row=row_num, column=2, pady=15, columnspan=2)


    # display_paging_buttons()
    # Displays Next >> / << Prev paging buttons based on data stored
    # Returns row_num, either unchanged or incremented by one
    def display_paging_buttons(self, row_num, columns, display_type):
        # Next Page >>> button
        self.next_button = Button(self, text="Next Page >>>", command=lambda: self.turn_the_page("next", display_type), font=self.button_font, padx=55)
        self.next_button.grid(row=row_num, column=columns[0], pady=15, columnspan=2)

        # <<< Prev Page button
        self.prev_button = Button(self, text="<<< Prev Page", command=lambda: self.turn_the_page("prev", display_type), font=self.button_font, padx=55)
        self.prev_button.grid(row=row_num, column=columns[1], pady=15, columnspan=2)

        # Increment row_num
        row_num += 1

        # Check if buttons need to be displayed
        if(len(self.datalist) <= 10):
            self.next_button.grid_forget()
            self.prev_button.grid_forget()
            row_num -= 1
        else:
            if(self.top_data_row == 0):
                self.prev_button.grid_forget()
            if(self.bottom_data_row >= len(self.datalist)):
                self.next_button.grid_forget()

        # Return row_num
        return row_num
    

    # return_to_menu()
    # Returns to the main menu upon a button click
    def return_to_menu(self):
        self.clear_screen()
        self.grid_forget()
        self.app.menu_frame.createWidgets()


    # turn_the_page()
    # Updates what values should be displayed on the screen for paging
    def turn_the_page(self, method, display):
        # Update top/bottom row values based on previous/next paging method
        if(method == "prev"):
            self.bottom_data_row -= 10
            self.top_data_row -= 10
        else:
            self.bottom_data_row += 10
            self.top_data_row += 10

        # Reperform the appropriate display function
        if(display == "system"):
            self.clear_then_display_system_stats()
        else:
            self.display_player_stats()

    
    # update_paging_then_display()
    # Resets paging values before displaying, used on button clicks
    def update_paging_then_display(self, display):
        # Reset paging values
        self.bottom_data_row = 10
        self.top_data_row = 0

        # Display appropriate elements
        if(display == "system"):
            self.clear_then_display_system_stats()
        else:
            self.display_player_stats()


    # clear_then_display_system_stats()
    # Clears the screen, then displays system stats
    def clear_then_display_system_stats(self):
        self.clear_screen()
        self.display_system_stats()


    # clear_screen()
    # Clears the screen of all items related to the database
    def clear_screen(self):
        for label in self.data_labels:
            label.grid_forget()
        for label in self.header_list:
            label.grid_forget()
        data_to_forget = (self.title_text, self.spacer, self.switch_button, self.return_button, self.next_button, self.prev_button)
        for label in data_to_forget:
            label.grid_forget()


# Main routing for testing MenuFrame
if __name__ == "__main__":
    app = PandemicGame.MainApplication()
    frame = DatabaseFrame(app)
    app.add_test(frame)
    app.master.title("DatabaseFrame test")
    app.mainloop()