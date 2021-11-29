# - - - - - - - - - - - - - - - - - - - -
# COP 4521 -- Term Project
# Daniel Fletcher, Connor Klekamp, Jacob Gregie
# PANDEMIC board game implementation
# - - - - - - - - - - - - - - - - - - - -

# * * * PlayerHands.py * * *
# GUI implementation of the player hand display

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
class HandFrame(Frame):
    # Overridden constructor
    def __init__(self, app, master=None):
        Frame.__init__(self, master, height=600, width=200, bg = 'blue')
        self.app = app
        self.createWidgets()

    # createWidgets()
    # Creates widgets upon initialization in constructor
    def createWidgets(self):
        # Setting row number (for grid) to zero, so the correct amount of card buttons is always shown.
        row = 0

        if self.app.menu_frame.playercount >= 2:
            # Creating buttons for first player name and cards.
            self.p1_name = self.app.board.player_list[0].username
            self.p1_name_button = Button(self, text=self.p1_name, command=lambda: self.player_click(self.p1_name), font = ("Times New Roman",10), width=20)
            self.p1_name_button.grid(row=row, column=0, padx=8, pady=4, ipadx=10)
            row += 1

            self.p1_card_buttons = list()
            card_num = 0
            for i in self.app.board.player_list[0].playerhand:
                if isinstance(i, CityCard):
                    self.cardname = self.app.board.player_list[0].playerhand[card_num].city
                    text_color = "white"
                    if self.app.board.player_list[0].playerhand[card_num].color == "yellow":
                        text_color = "black"
                    self.p1_card_button = Button(self, text=self.cardname, fg=text_color, bg=self.app.board.player_list[0].playerhand[card_num].color, command=lambda: self.card_click(self.cardname), font = ("Times New Roman",10), width=20)
                else:
                    self.val = self.app.board.player_list[0].playerhand[card_num].value
                    if self.val == 1:
                        self.cardname = "EVENT - One Quiet Night"
                    elif self.val == 2:
                        self.cardname = "EVENT - Forecast"
                    elif self.val == 3:
                        self.cardname = "EVENT - Government Grant"
                    elif self.val == 4:
                        self.cardname = "EVENT - Airlift"
                    elif self.val == 5:
                        self.cardname = "EVENT - Resilient Population"
                    else:
                        self.cardname = "Error - Invalid Value"
                    self.p1_card_button = Button(self, text=self.cardname, command=lambda: self.card_click(self.cardname), font = ("Times New Roman",10), width=20)

                self.p1_card_buttons.append(self.p1_card_button)
                self.p1_card_buttons[card_num].grid(row=row, column=0, padx=8, pady=4, ipadx=10)
                row += 1
                card_num += 1

            # Creating buttons for second player name and cards.
            self.p2_name = self.app.board.player_list[1].username
            self.p2_name_button = Button(self, text=self.p2_name, command=lambda: self.player_click(self.p2_name), font = ("Times New Roman",10), width=20)
            self.p2_name_button.grid(row=row, column=0, padx=8, pady=4, ipadx=10)
            row += 1

            self.p2_card_buttons = list()
            card_num = 0
            for i in self.app.board.player_list[1].playerhand:
                if isinstance(i, CityCard):
                    self.cardname = self.app.board.player_list[1].playerhand[card_num].city
                    text_color = "white"
                    if self.app.board.player_list[1].playerhand[card_num].color == "yellow":
                        text_color = "black"
                    self.p2_card_button = Button(self, text=self.cardname, fg=text_color, bg=self.app.board.player_list[1].playerhand[card_num].color, command=lambda: self.card_click(self.cardname), font = ("Times New Roman",10), width=20)
                else:
                    self.val = self.app.board.player_list[1].playerhand[card_num].value
                    if self.val == 1:
                        self.cardname = "EVENT - One Quiet Night"
                    elif self.val == 2:
                        self.cardname = "EVENT - Forecast"
                    elif self.val == 3:
                        self.cardname = "EVENT - Government Grant"
                    elif self.val == 4:
                        self.cardname = "EVENT - Airlift"
                    elif self.val == 5:
                        self.cardname = "EVENT - Resilient Population"
                    else:
                        self.cardname = "Error - Invalid Value"
                    self.p2_card_button = Button(self, text=self.cardname, command=lambda: self.card_click(self.cardname), font = ("Times New Roman",10), width=20)

                self.p2_card_buttons.append(self.p2_card_button)
                self.p2_card_buttons[card_num].grid(row=row, column=0, padx=8, pady=4, ipadx=10)
                row += 1
                card_num += 1

        if self.app.menu_frame.playercount >= 3:
            # Creating buttons for third player name and cards, if applicable.
            self.p3_name = self.app.board.player_list[2].username
            self.p3_name_button = Button(self, text=self.p3_name, command=lambda: self.player_click(self.p3_name), font = ("Times New Roman",10), width=20)
            self.p3_name_button.grid(row=row, column=0, padx=8, pady=4, ipadx=10)
            row += 1

            self.p3_card_buttons = list()
            card_num = 0
            for i in self.app.board.player_list[2].playerhand:
                if isinstance(i, CityCard):
                    self.cardname = self.app.board.player_list[2].playerhand[card_num].city
                    text_color = "white"
                    if self.app.board.player_list[2].playerhand[card_num].color == "yellow":
                        text_color = "black"
                    self.p3_card_button = Button(self, text=self.cardname, fg=text_color, bg=self.app.board.player_list[2].playerhand[card_num].color, command=lambda: self.card_click(self.cardname), font = ("Times New Roman",10), width=20)
                else:
                    self.val = self.app.board.player_list[2].playerhand[card_num].value
                    if self.val == 1:
                        self.cardname = "EVENT - One Quiet Night"
                    elif self.val == 2:
                        self.cardname = "EVENT - Forecast"
                    elif self.val == 3:
                        self.cardname = "EVENT - Government Grant"
                    elif self.val == 4:
                        self.cardname = "EVENT - Airlift"
                    elif self.val == 5:
                        self.cardname = "EVENT - Resilient Population"
                    else:
                        self.cardname = "Error - Invalid Value"
                    self.p3_card_button = Button(self, text=self.cardname, command=lambda: self.card_click(self.cardname), font = ("Times New Roman",10), width=20)

                self.p3_card_buttons.append(self.p3_card_button)
                self.p3_card_buttons[card_num].grid(row=row, column=0, padx=8, pady=4, ipadx=10)
                row += 1
                card_num += 1

        if self.app.menu_frame.playercount == 4:
            # Creating buttons for fourth player name and cards, if applicable.
            self.p4_name = self.app.board.player_list[3].username
            self.p4_name_button = Button(self, text=self.p4_name, command=lambda: self.player_click(self.p4_name), font = ("Times New Roman",10), width=20)
            self.p4_name_button.grid(row=row, column=0, padx=8, pady=4, ipadx=10)
            row += 1

            self.p4_card_buttons = list()
            card_num = 0
            for i in self.app.board.player_list[3].playerhand:
                if isinstance(i, CityCard):
                    self.cardname = self.app.board.player_list[3].playerhand[card_num].city
                    text_color = "white"
                    if self.app.board.player_list[3].playerhand[card_num].color == "yellow":
                        text_color = "black"
                    p4_card_button = Button(self, text=self.cardname, fg=text_color, bg=self.app.board.player_list[3].playerhand[card_num].color, command=lambda: self.card_click(self.cardname), font = ("Times New Roman",10), width=20)
                else:
                    self.val = self.app.board.player_list[3].playerhand[card_num].value
                    if self.val == 1:
                        self.cardname = "EVENT - One Quiet Night"
                    elif self.val == 2:
                        self.cardname = "EVENT - Forecast"
                    elif self.val == 3:
                        self.cardname = "EVENT - Government Grant"
                    elif self.val == 4:
                        self.cardname = "EVENT - Airlift"
                    elif self.val == 5:
                        self.cardname = "EVENT - Resilient Population"
                    else:
                        self.cardname = "Error - Invalid Value"
                    self.p4_card_button = Button(self, text=self.cardname, command=lambda: self.card_click(self.cardname), font = ("Times New Roman",10), width=20)

                self.p4_card_buttons.append(p4_card_button)
                self.p4_card_buttons[card_num].grid(row=row, column=0, padx=8, pady=4, ipadx=10)
                row += 1
                card_num += 1

        
        self.confirm_button = Button(self, text="Confirm Selection", fg='white', bg='green', command=lambda: self.confirm_click(), font = ("Times New Roman",10), width=20)
        self.confirm_button.grid(row=row, column=0, padx=8, pady=4, ipadx=10)


    def player_click(self, username):
        self.app.selected_player = username

    def card_click(self, cardname):
        self.app.selected_card = cardname

    def confirm_click(self):
        self.app.confirmed_card = self.app.selected_card


# Main routing for testing HandFrame
if __name__ == "__main__":
    app = PandemicGame.MainApplication()
    frame = HandFrame(app)
    app.add_test(frame)
    app.master.title("HandFrame test")
    app.mainloop()
