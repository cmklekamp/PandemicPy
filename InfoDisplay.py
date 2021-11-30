# - - - - - - - - - - - - - - - - - - - -
# COP 4521 -- Term Project
# Daniel Fletcher, Connor Klekamp, Jacob Gregie
# PANDEMIC board game implementation
# - - - - - - - - - - - - - - - - - - - -

# * * * InfoDisplay.py * * *
# Implements custom InfoFrame class
# Used for displaying miscellaneous game board information during a play session

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


# Custom frame: InfoFrame
class InfoFrame(Frame):

    # Overridden constructor
    def __init__(self, app, master=None):
        Frame.__init__(self, master, height=100, width=1050, bg="blue")
        self.app = app
        self.createWidgets()


    # createWidgets()
    # Creates widgets upon initialization in constructor
    def createWidgets(self):
        # Initialize fonts to be used
        self.title_font = Font(family="Times New Roman", size=14, weight="bold")
        self.info_font = Font(family="Times New Roman", size=10, weight="normal")

        # Display data on screen
        self.is_displaying = False
        self.update_info()


    # update_info()
    # Updates all displayed visual elements in case an item changed
    def update_info(self):
        # If currently on the screen, clear all visual elements
        if(self.is_displaying == True):
            self.clear()

        # Create header for info section
        # self.title_text = Label(self, text="--- Miscellaneous Board Information ---", font=self.title_font, bg="blue", fg="white")
        # self.title_text.grid(row=0, column=0, pady=20, columnspan=2)

        # Outbreak tracker
        self.outbreak_label = Label(self, text="Outbreak tracker: " + str(self.app.board.outbreak_counter) + " of 8", font=self.info_font, bg="blue", fg="white")
        self.outbreak_label.grid(row=1, column=0, padx=30)
        # info_string = "0\t1\t2\t3\t4\t5\t6\t7\t8\n"
        # if(self.app.board.outbreak_counter == 0):
        #     info_string += "^\t \t \t \t \t \t \t \t  "
        # elif(self.app.board.outbreak_counter == 1):
        #     info_string += " \t^\t \t \t \t \t \t \t  "
        # elif(self.app.board.outbreak_counter == 2):
        #     info_string += " \t \t^\t \t \t \t \t \t  "
        # elif(self.app.board.outbreak_counter == 3):
        #     info_string += " \t \t \t^\t \t \t \t \t  "
        # elif(self.app.board.outbreak_counter == 4):
        #     info_string += " \t \t \t \t^\t \t \t \t  "
        # elif(self.app.board.outbreak_counter == 5):
        #     info_string += " \t \t \t \t \t^\t \t \t  "
        # elif(self.app.board.outbreak_counter == 6):
        #     info_string += " \t \t \t \t \t \t^\t \t  "
        # elif(self.app.board.outbreak_counter == 7):
        #     info_string += " \t \t \t \t \t \t \t^\t  "
        # else:
        #     info_string += " \t \t \t \t \t \t \t \t^ "
        # self.outbreak_info = Label(self, text=info_string, font=self.info_font, bg="blue", fg="white")
        # self.outbreak_info.grid(row=1, column=1)

        # Infection rate
        self.infection_label = Label(self, text="Infection rate: " + str(self.app.board.infection_rate), font=self.info_font, bg="blue", fg="white")
        self.infection_label.grid(row=1, column=1, padx=30)
        # info_string = "2\t2\t2\t3\t3\t4\t4\n"
        # if(self.app.board.infection_rate_counter == 0):
        #     info_string += "^\t \t \t \t \t \t  "
        # elif(self.app.board.infection_rate_counter == 1):
        #     info_string += " \t^\t \t \t \t \t  "
        # elif(self.app.board.infection_rate_counter == 2):
        #     info_string += " \t \t^\t \t \t \t  "
        # elif(self.app.board.infection_rate_counter == 3):
        #     info_string += " \t \t \t^\t \t \t  "
        # elif(self.app.board.infection_rate_counter == 4):
        #     info_string += " \t \t \t \t^\t \t  "
        # elif(self.app.board.infection_rate_counter == 5):
        #     info_string += " \t \t \t \t \t^\t  "
        # else:
        #     info_string += " \t \t \t \t \t \t^ "
        # self.infection_info = Label(self, text=info_string, font=self.info_font, bg="blue", fg="white")
        # self.infection_info.grid(row=2, column=1)

        # Cured diseases
        self.cure_label = Label(self, text="Cured diseases: ", font=self.info_font, bg="blue", fg="white")
        self.cure_label.grid(row=2, column=0, padx=30)
        info_string = ""
        if(self.app.board.blue_cured == True):
            info_string += "blue, "
        if(self.app.board.red_cured == True):
            info_string += "red, "
        if(self.app.board.black_cured == True):
            info_string += "black, "
        if(self.app.board.yellow_cured == True):
            info_string += "yellow, "
        if(len(info_string) > 0):
            info_string = info_string[:-2]
        else:
            info_string = "N/A"
        self.cure_info = Label(self, text=info_string, font=self.info_font, bg="blue", fg="white")
        self.cure_info.grid(row=2, column=1)

        # Eradicated diseases
        self.eradicate_label = Label(self, text="Eradicated diseases: ", font=self.info_font, bg="blue", fg="white")
        self.eradicate_label.grid(row=3, column=0, padx=30)
        info_string = ""
        if(self.app.board.blue_eradicated == True):
            info_string += "blue, "
        if(self.app.board.red_eradicated == True):
            info_string += "red, "
        if(self.app.board.black_eradicated == True):
            info_string += "black, "
        if(self.app.board.yellow_eradicated == True):
            info_string += "yellow, "
        if(len(info_string) > 0):
            info_string = info_string[:-2]
        else:
            info_string = "N/A"
        self.eradicate_info = Label(self, text=info_string, font=self.info_font, bg="blue", fg="white")
        self.eradicate_info.grid(row=3, column=1)

        # Remaining disease cubes on the board
        self.remaining_label = Label(self, text="Disease cubes remaining: ", font=self.info_font, bg="blue", fg="white")
        self.remaining_label.grid(row=4, column=0, padx=30)
        info_string = ""
        info_string += "Blue: " + str(self.app.board.blue_remaining)
        info_string += "\t\tRed: " + str(self.app.board.red_remaining)
        info_string += "\t\tBlack: " + str(self.app.board.black_remaining)
        info_string += "\t\tYellow: " + str(self.app.board.yellow_remaining)
        self.remaining_info = Label(self, text=info_string, font=self.info_font, bg="blue", fg="white")
        self.remaining_info.grid(row=4, column=1)       

        # Set is_displaying flag to True
        self.is_displaying = True


    # clear()
    # Clears the frame of all displayed visual elements
    def clear(self):
        items_to_delete_1 = (self.outbreak_label, self.infection_label)
        items_to_delete_2 = (self.cure_label, self.cure_info, self.eradicate_label, self.eradicate_info, self.remaining_label, self.remaining_info)
        for item in items_to_delete_1:
            item.grid_forget()
        for item in items_to_delete_2:
            item.grid_forget()



# Main routing for testing InfoFrame
if __name__ == "__main__":
    app = PandemicGame.MainApplication()
    app.board = GameBoard(3, ["Connor", "Daniel", "Jacob"])
    frame = InfoFrame(app)
    app.add_test(frame)
    app.master.title("InfoFrame test")
    app.mainloop()