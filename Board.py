# - - - - - - - - - - - - - - - - - - - -
# COP 4521 -- Term Project
# Daniel Fletcher, Connor Klekamp, Jacob Gregie
# PANDEMIC board game implementation
# - - - - - - - - - - - - - - - - - - - -

# * * * Board.py * * *
# GUI implementation of the Pandemic Board

# Relevant import statements -- custom classes (logic)
from Cards import *
from Decks import *
from City import *
from Player import *
from GameBoard import *
import PandemicGame

# Relevant import statements -- tkinter
from tkinter import *
from tkinter.font import Font
from PIL import ImageTk,Image

# Main application class
class BoardFrame(Frame):
    # Overridden constructor
    def __init__(self, app, master=None):
        Frame.__init__(self, master, height=600, width=1050, bg = 'red')
        self.app = app
        self.createWidgets()

    # createWidgets()
    # Creates widgets upon initialization in constructor
    def createWidgets(self):
        
        # Set up image background
        img = Image.open("Resources/MapFinal.png")
        resized_image= img.resize((1050,600), Image.ANTIALIAS)
        new_image= ImageTk.PhotoImage(resized_image)
        background = Label(self,image = new_image)
        background.photo = new_image
        background.place(x=0, y=0)
        
        self.names = ["Bogotá","Johannesburg","Buenos Aires","Mexico City","Lima","Los Angeles","Miami","Kinshasa",
                      "São Paulo","Santiago","Khartoum","Lagos","Istanbul","Kolkata","Tehran","Cairo",
                      "Algiers","Moscow","Chennai","Karachi","Delhi","Mumbai","Riyadh","Baghdad",
                      "San Francisco","Atlanta","Madrid","New York","Essen","Chicago","St. Petersburg","Montréal",
                      "London","Paris","Milan","Washington","Tokyo","Beijing","Shanghai","Bangkok",
                      "Manila","Ho Chi Minh City","Sydney","Seoul","Taipei","Jakarta","Osaka","Hong Kong",]

        self.coordinates = [(272,364),(575,460),(318,488),(197,320),(263,414),(141,272),(254,300),(537,391),
                            (354,451),(282,485),(587,332),(502,360),(577,244),(753,310),(644,265),(584,286),
                            (501,262),(604,178),(730,339),(690,303),(721,290),(708,321),(631,304),(623,273),
                            (128,258),(242,272),(480,247),(275,245),(514,200),(232,242),(582,155),(273,226),
                            (488,198),(501,214),(519,227),(261,255),(908,266),(836,249),(852,281),(789,337),
                            (850,335),(809,347),(940,486),(869,259),(852,303),(809,398),(891,269),(830,311)]

        self.buttons = list()
        
        # create buttons for each city
        for i in range(48):
            if (i < 12):
                path = "Resources/yellow.png"
            elif (i >= 12 and i < 24):
                path = "Resources/black.png"
            elif (i >= 24 and i < 36):
                path = "Resources/blue.png"
            else:
                path = "Resources/red.png"

            button_img = Image.open(path)
            new_image= ImageTk.PhotoImage(button_img)
            new_button = Button(self, image=new_image, borderwidth=0, command=lambda i = i: self.button_click(self.names[i]))
            new_button.image = new_image
            
            x_coordinate,y_coordinate = self.coordinates[i]
            self.buttons.append(new_button)
            self.buttons[i].place(height = 17, width = 17, x=x_coordinate, y=y_coordinate)       
    
    def button_click(self, name):
        self.app.selected_city = name

# Main routing for testing MenuFrame
if __name__ == "__main__":
    app = PandemicGame.MainApplication()
    frame = BoardFrame(app)
    app.add_test(frame)
    app.master.title("BoardFrame test")
    app.mainloop()