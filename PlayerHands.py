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
        if self.app.menu_frame.playercount == 2:
            # p1_label_text = self.app.board.playernames[0] + "'s Hand"
            # p1_label = Label(text = p1_label_text, font = ("Times New Roman",10))
            # self.p1_label.place(x=25, y=25)
            pass
        elif self.app.menu_frame.playercount == 3:
            pass
        else:
            pass


# Main routing for testing HandFrame
if __name__ == "__main__":
    app = PandemicGame.MainApplication()
    frame = HandFrame(app)
    app.add_test(frame)
    app.master.title("HandFrame test")
    app.mainloop()
