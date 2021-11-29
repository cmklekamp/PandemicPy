# - - - - - - - - - - - - - - - - - - - -
# COP 4521 -- Term Project
# Daniel Fletcher, Connor Klekamp, Jacob Gregie
# PANDEMIC board game implementation
# - - - - - - - - - - - - - - - - - - - -

# * * * CityViewer.py * * *
# Implements custom CityViewerFrame class
# Used for displaying city information during a game session


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
class CityViewerFrame(Frame):

    # Overridden constructor
    def __init__(self, app, master=None):
        Frame.__init__(self, master, height=600, width=200, bg="blue")
        self.app = app
        self.createWidgets()


    # createWidgets()
    # Creates widgets upon initialization in constructor
    def createWidgets(self):
        # Initialize fonts to be used
        self.title_font = Font(family="Times New Roman", size=14, weight="bold")
        self.display_font = Font(family="Times New Roman", size=8, weight="normal")
        self.button_font = Font(family="Arial", size=14, weight="normal")

        # Display data on screen
        self.is_displaying_player = False
        self.is_displaying_infected = False
        self.update_info()

    
    # update_info()
    # Updates all displayed visual elements in case an item changed
    def update_info(self):
        # If currently on the screen, clear all visual elements
        if(self.is_displaying_player == True or self.is_displaying_infected == True):
            self.clear()

        # Update visual elements based on what is currently showing
        if(self.is_displaying_infected == True):
            self.display_infected_cities()
        else:
            self.display_player_cities()


    # display_player_cities()
    # Displays the cities that the players are currently in
    def display_player_cities(self):
        # Clear visual elements if switching from other view
        if(self.is_displaying_infected == True):
            self.clear()
            
        # Create header for info section
        self.title_text = Label(self, text="--- City Viewer: Player Cities ---", font=self.title_font, bg="blue", fg="white")
        self.title_text.grid(row=0, column=0, pady=20, columnspan=2)

        # Create button for switching to infected cities view
        row_num = 1
        self.buttons_list = list()
        self.buttons_list.append(Button(self, text="Switch to\nInfected View", command=self.display_infected_cities, font=self.button_font))
        self.buttons_list[-1].grid(row=row_num, column=0, columnspan=2, pady=40)
        row_num += 1

        # Create list of player name labels and corresponding city locations
        self.display_list = list()
        self.display_list.append(Label(self, text="Player locations:", font=self.display_font, bg="blue", fg="white"))
        self.display_list[-1].grid(row=row_num, column=0, columnspan=2, padx=30, pady=10)
        row_num += 1
        for player in self.app.board.player_list:
            self.display_list.append(Label(self, text=player.username + " is in:", font=self.display_font, bg="blue", fg="white"))
            self.display_list[-1].grid(row=row_num, column=0, padx=30, pady=5)
            self.display_list.append(Label(self, text=player.current_city, font=self.display_font, bg="blue", fg="white"))
            self.display_list[-1].grid(row=row_num, column=1, padx=30, pady=5)
            row_num +=1

        # Create list of research station labels
        self.display_list.append(Label(self, text="\nResearch station locations:", font=self.display_font, bg="blue", fg="white"))
        self.display_list[-1].grid(row=row_num, column=0, columnspan=2, padx=30, pady=10)
        row_num += 1
        research_string = ""
        for city in self.app.board.city_list:
            if(self.app.board.city_list[city].has_station == True):
                research_string += city + "\n"
        self.display_list.append(Label(self, text=research_string, font=self.display_font, bg="blue", fg="white"))
        self.display_list[-1].grid(row=row_num, column=0, columnspan=2, padx=30, pady=2)

        # Update display flags
        self.is_displaying_player = True
        self.is_displaying_infected = False



    # display_infected_cities()
    # Displays ALL cities, showing how many disease cubes are in each one
    def display_infected_cities(self):
        # Clear visual elements if switching from other view
        if(self.is_displaying_player == True):
            self.clear()

        # Create header for info section
        self.title_text = Label(self, text="--- City Viewer: Infected Cities ---", font=self.title_font, bg="blue", fg="white")
        self.title_text.grid(row=0, column=0, pady=20, columnspan=2)

        # Create button for switching to player cities view
        row_num = 1
        self.buttons_list = list()
        self.buttons_list.append(Button(self, text="Switch to\nPlayerView", command=self.display_player_cities, font=self.button_font))
        self.buttons_list[-1].grid(row=row_num, column=0, columnspan=2, pady=40)
        row_num += 1

        # Capture cities as list of cities
        list_of_cities = list(self.app.board.city_list.keys())

        # Blue city labels
        self.display_list.append(Label(self, text="-- Blue cities --", font=self.display_font, bg="blue", fg="white"))
        self.display_list[-1].grid(row=row_num, column=0, padx=30)
        row_num += 1
        for city in list_of_cities[24:36]:
            if(self.app.board.city_list[city].blue != 0 or self.app.board.city_list[city].red != 0 or self.app.board.city_list[city].black != 0 or self.app.board.city_list[city].yellow != 0):
                display_string = city + " - " + str(self.app.board.city_list[city].blue) + " blue, " + str(self.app.board.city_list[city].red)
                display_string += " red, " + str(self.app.board.city_list[city].black) + " black, " + str(self.app.board.city_list[city].yellow) + " yellow"
                self.display_list.append(Label(self, text=display_string, font=self.display_font, bg="blue", fg="white"))
                self.display_list[-1].grid(row=row_num, column=0, padx=30)
                row_num += 1

        # Red city labels
        self.display_list.append(Label(self, text="\n-- Red cities --", font=self.display_font, bg="blue", fg="white"))
        self.display_list[-1].grid(row=row_num, column=0, padx=30)
        row_num += 1
        for city in list_of_cities[36:48]:
            if(self.app.board.city_list[city].blue != 0 or self.app.board.city_list[city].red != 0 or self.app.board.city_list[city].black != 0 or self.app.board.city_list[city].yellow != 0):
                display_string = city + " - " + str(self.app.board.city_list[city].blue) + " blue, " + str(self.app.board.city_list[city].red)
                display_string += " red, " + str(self.app.board.city_list[city].black) + " black, " + str(self.app.board.city_list[city].yellow) + " yellow"
                self.display_list.append(Label(self, text=display_string, font=self.display_font, bg="blue", fg="white"))
                self.display_list[-1].grid(row=row_num, column=0, padx=30)
                row_num += 1

        # Black city labels
        self.display_list.append(Label(self, text="\n-- Black cities --", font=self.display_font, bg="blue", fg="white"))
        self.display_list[-1].grid(row=row_num, column=0, padx=30)
        row_num += 1
        for city in list_of_cities[12:24]:
            if(self.app.board.city_list[city].blue != 0 or self.app.board.city_list[city].red != 0 or self.app.board.city_list[city].black != 0 or self.app.board.city_list[city].yellow != 0):
                display_string = city + " - " + str(self.app.board.city_list[city].blue) + " blue, " + str(self.app.board.city_list[city].red)
                display_string += " red, " + str(self.app.board.city_list[city].black) + " black, " + str(self.app.board.city_list[city].yellow) + " yellow"
                self.display_list.append(Label(self, text=display_string, font=self.display_font, bg="blue", fg="white"))
                self.display_list[-1].grid(row=row_num, column=0, padx=30)
                row_num += 1

        # Yellow city labels
        self.display_list.append(Label(self, text="\n-- Yellow cities --", font=self.display_font, bg="blue", fg="white"))
        self.display_list[-1].grid(row=row_num, column=0, padx=30)
        row_num += 1
        for city in list_of_cities[0:12]:
            if(self.app.board.city_list[city].blue != 0 or self.app.board.city_list[city].red != 0 or self.app.board.city_list[city].black != 0 or self.app.board.city_list[city].yellow != 0):
                display_string = city + " - " + str(self.app.board.city_list[city].blue) + " blue, " + str(self.app.board.city_list[city].red)
                display_string += " red, " + str(self.app.board.city_list[city].black) + " black, " + str(self.app.board.city_list[city].yellow) + " yellow"
                self.display_list.append(Label(self, text=display_string, font=self.display_font, bg="blue", fg="white"))
                self.display_list[-1].grid(row=row_num, column=0, padx=30)
                row_num += 1

        # Update display flag
        self.is_displaying_player = False
        self.is_displaying_infected = True


    # clear()
    # Clears the frame of all displayed visual elements
    def clear(self):
        for button in self.buttons_list:
            button.grid_forget()
        for label in self.display_list:
            label.grid_forget()
        self.title_text.grid_forget()


# Main routing for testing InfoFrame
if __name__ == "__main__":
    app = PandemicGame.MainApplication()
    app.board = GameBoard(3, ["Connor", "Daniel", "Jacob"])
    frame = CityViewerFrame(app)
    app.add_test(frame)
    app.master.title("CityViewerFrame test")
    app.mainloop()