# - - - - - - - - - - - - - - - - - - - -
# COP 4521 -- Term Project
# Daniel Fletcher, Connor Klekamp, Jacob Gregie
# PANDEMIC board game implementation
# - - - - - - - - - - - - - - - - - - - -

# * * * ColorDisplay.py * * *
# GUI implementation of a color display for picking disease/cure colors

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
class ColorFrame(Frame):
    # Overridden constructor
    def __init__(self, app, master=None):
        Frame.__init__(self, master, height=200, width=200, bg = 'blue')
        self.app = app
        self.createWidgets()

    # createWidgets()
    # Creates widgets upon initialization in constructor
    def createWidgets(self):
        self.red_button = Button(self, text="RED", fg="white", bg="red", command=lambda: self.color_click("red"), font = ("Times New Roman",10), height=2, width=10)
        self.red_button.grid(row=0, column=0, padx=4, pady=4, ipadx=3)
        self.blue_button = Button(self, text="BLUE", fg="white", bg="blue", command=lambda: self.color_click("blue"), font = ("Times New Roman",10), height=2, width=10)
        self.blue_button.grid(row=0, column=1, padx=4, pady=4, ipadx=3)
        self.black_button = Button(self, text="BLACK", fg="white", bg="black", command=lambda: self.color_click("black"), font = ("Times New Roman",10), height=2, width=10)
        self.black_button.grid(row=1, column=0, padx=4, pady=4, ipadx=3)
        self.yellow_button = Button(self, text="YELLOW", fg="black", bg="yellow", command=lambda: self.color_click("yellow"), font = ("Times New Roman",10), height=2, width=10)
        self.yellow_button.grid(row=1, column=1, padx=4, pady=4, ipadx=3)

        self.disable_buttons()

    # Enable buttons function for general use.
    def enable_buttons(self):
        self.red_button["state"] = "normal"
        self.blue_button["state"] = "normal"
        self.black_button["state"] = "normal"
        self.yellow_button["state"] = "normal"

    # Disable buttons function for general use.
    def disable_buttons(self):
        self.red_button["state"] = "disabled"
        self.blue_button["state"] = "disabled"
        self.black_button["state"] = "disabled"
        self.yellow_button["state"] = "disabled"

    def color_click(self, color):
        self.app.selected_color.set(color)


# Main routing for testing HandFrame
if __name__ == "__main__":
    app = PandemicGame.MainApplication()
    frame = ColorFrame(app)
    app.add_test(frame)
    app.master.title("ColorFrame test")
    app.mainloop()
