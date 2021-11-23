# - - - - - - - - - - - - - - - - - - - -
# COP 4521 -- Term Project
# Daniel Fletcher, Connor Klekamp, Jacob Gregie
# PANDEMIC board game implementation
# - - - - - - - - - - - - - - - - - - - -

# * * * MainMenu.py * * *
# GUI implementation -- abstraction of main menu
# Contains main menu, buttons, and functionality for each button

# Relevant import statements
from tkinter import *
from tkinter.font import Font
from GameBoard import *
import PandemicGame

# Custom frame: MenuFrame
class MenuFrame(Frame):

    # Overridden constructor
    def __init__(self, app, master=None):
        Frame.__init__(self, master)
        self.app = app
        self.createWidgets()

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

        # Title text
        self.title_font = Font(family="Times New Roman", size=72, weight="bold")
        self.title_text = Label(self, text="PANDEMIC", font=self.title_font)
        self.title_text.grid(row=0, column=0, pady=2)

        # Subtitle 1 -- developed by Connor, Jacob, and Daniel
        self.subtitle_devs_font = Font(family="Times New Roman", size=14, weight="normal")
        self.subtitle_devs_text = Label(self, text="digital implementation developed by Connor Klekamp, Jacob Gregie, and Daniel Fletcher", font=self.subtitle_devs_font)
        self.subtitle_devs_text.grid(row=1, column=0, pady=5)

        # Subtitle 2 -- original game credits
        self.subtitle_credits_font = Font(family="Times New Roman", size=14, weight="normal")
        self.subtitle_credits_text = Label(self, text="original game design by Matt Leacock, published by Z-Man Games\n\n\n\n", font=self.subtitle_credits_font)
        self.subtitle_credits_text.grid(row=2, column=0, pady=5)

        # New Game button
        self.button_font = Font(family="Arial", size=24, weight="normal")
        self.start_button = Button(self, text="New Game", command=self.start_game_info, font=self.button_font, padx=55)
        self.start_button.grid(row=3, column=0, pady=15)

        # Game History button
        self.history_button = Button(self, text="Past Game History", font=self.button_font)
        self.history_button.grid(row=4, column=0, pady=15)

        # Quit button
        self.quit_button = Button(self, text="Quit", command=self.quit, font=self.button_font, padx=105)
        self.quit_button.grid(row=5, column=0, pady=15)


    # start_game_info()
    # Prompts collection of start-game data, like difficulty and player count
    def start_game_info(self):
        # Remove title screen elements from screen
        self.items_to_delete = (self.title_text, self.subtitle_devs_text, self.subtitle_credits_text, self.start_button, self.history_button, self.quit_button)
        for item in self.items_to_delete:
            item.grid_forget()

        # Difficulty selection
        self.heading_font = Font(family="Arial", size=24, weight="normal")
        self.difficulty_button = Menubutton(self, text="Choose difficulty...", borderwidth=5, font=self.heading_font, bg="#B2B2B2")
        self.difficulty_button.grid(row=0, column=0, padx=25, pady=25)
        self.difficulty_menu = Menu(self.difficulty_button)
        self.difficulty_button["menu"] = self.difficulty_menu
        self.difficulty_menu.add_command(label="Introductory - 4 Epidemic cards", command=lambda: self.select_difficulty(4))
        self.difficulty_menu.add_command(label="Standard - 5 Epidemic cards", command=lambda: self.select_difficulty(5))
        self.difficulty_menu.add_command(label="Heroic - 6 Epidemic cards", command=lambda: self.select_difficulty(6))

        # Player count selection revealed after difficulty selection

    
    # select_difficulty()
    # Sets the difficulty based on a button selection
    def select_difficulty(self, number):
        self.difficulty = number
        self.difficulty_button.grid_forget()
        if(number == 4):
            self.difficulty_button = Menubutton(self, text="Introductory - 4 Epidemic Cards", borderwidth=5, font=self.heading_font, bg="#B2B2B2", state=DISABLED)
        elif(number == 5):
            self.difficulty_button = Menubutton(self, text="Standard - 5 Epidemic Cards", borderwidth=5, font=self.heading_font, bg="#B2B2B2", state=DISABLED)
        else:
            self.difficulty_button = Menubutton(self, text="Heroic - 6 Epidemic Cards", borderwidth=5, font=self.heading_font, bg="#B2B2B2", state=DISABLED)
        self.difficulty_button.grid(row=0, column=0, padx=25, pady=25)

        # Player count selection
        self.playercount_button = Menubutton(self, text="Choose player count...", borderwidth=5, font=self.heading_font, bg="#B2B2B2")
        self.playercount_button.grid(row=1, column=0, padx=25, pady=25)
        self.playercount_menu = Menu(self.playercount_button)
        self.playercount_button["menu"] = self.playercount_menu
        self.playercount_menu.add_command(label="2 player game", command=lambda: self.set_player_count(2))
        self.playercount_menu.add_command(label="3 player game", command=lambda: self.set_player_count(3))
        self.playercount_menu.add_command(label="4 player game", command=lambda: self.set_player_count(4))


    
    # set_player_count()
    # Sets the player count based on a button selection
    def set_player_count(self, number):
        self.playercount = number
        self.playercount_button.grid_forget()
        if(number == 2):
            self.playercount_button = Menubutton(self, text="2 player game", borderwidth=5, font=self.heading_font, bg="#B2B2B2", state=DISABLED)
        elif(number == 3):
            self.playercount_button = Menubutton(self, text="3 player game", borderwidth=5, font=self.heading_font, bg="#B2B2B2", state=DISABLED)
        else:
            self.playercount_button = Menubutton(self, text="4 player game", borderwidth=5, font=self.heading_font, bg="#B2B2B2", state=DISABLED)
        self.playercount_button.grid(row=1, column=0)

        # Reveal player username input
        self.player_usernames(number)


    # player_usernames()
    # Prompts input of player usernames, adding a "Start Game" button
    def player_usernames(self, number):
        # Helper variables
        self.username_entries = list()

        # Add header
        self.header_text = Label(self, text="Enter player usernames:", font=self.heading_font)
        self.header_text.grid(row=2, column=0, pady=25)
        row_num = 0

        # Add entry fields
        for player in range(0, number):
            row_num = player + 3
            self.username_entries.append(Entry(self, width=50, font=self.heading_font))
            self.username_entries[player].grid(row=row_num, column=0, pady=10)
            self.username_entries[player].insert(0, "Player " + str(player + 1))

        # Set up "Start Game" button
        self.start_button = Button(self, text="Start Game!", command=self.start_game, font=self.button_font, padx=55)
        self.start_button.grid(row=row_num + 1, column=0, pady=15)

    
    # start_game()
    # Starts the actual game after collecting all start game info
    def start_game(self):
        # Extract usernames from input fields, deleting the field after extraction
        self.playernames = list()
        for item in self.username_entries:
            self.playernames.append(item.get())
            item.grid_forget()

        # Remove remaining game info collection elements from screen
        self.items_to_delete = (self.difficulty_button, self.playercount_button, self.header_text, self.start_button)
        for item in self.items_to_delete:
            item.grid_forget()

        # Call start_game() in MainApplication
        self.app.start_game(self.playercount, self.playernames, self.difficulty)



# Main routing for testing MenuFrame
if __name__ == "__main__":
    app = PandemicGame.MainApplication()
    frame = MenuFrame(app)
    app.add_test(frame)
    app.master.title("MenuFrame test")
    app.mainloop()