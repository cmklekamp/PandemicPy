# - - - - - - - - - - - - - - - - - - - -
# COP 4521 -- Term Project
# Daniel Fletcher, Connor Klekamp, Jacob Gregie
# PANDEMIC board game implementation
# - - - - - - - - - - - - - - - - - - - -


# * * * Decks.py * * *
# Card deck inheritance hierarchy
# Base "Deck" class
# Derived "InfectionDeck" and "PlayerDeck" classes
# Separation allows for unique and convenient constructor calls


# Relevant import statements
from Cards import *
import random


# Deck class
# Contains general card deck behavior and attributes
class Deck(object):

    # Default constructor (should only be called by derived class constructors)
    def __init__(self):
        self._cardlist = list()

    # shuffle()
    # Shuffle cards in the deck using the random library's prebuilt list shuffling method
    # NOTE: Is this method necessary with the pre-existing shuffle method already usable?
    def shuffle(self):
        random.shuffle(self._cardlist)

    # top_card()
    # Returns the top card from the deck, removing it from the deck in the process
    def top_card(self):
        return self._cardlist.pop(0)

    # get_size()
    # Returns the size of the deck
    def get_size(self):
        return self._cardlist.len()

    # is_empty()
    # Returns True if the deck is empty, False otherwise
    def is_empty(self):
        if self._cardlist.get_size() == 0:
            return True
        else:
            return False

# InfectionDeck class
# Contains Infection cards and behavior unique to Infection deck
class InfectionDeck(Deck):

    # Default constructor
    # Initializes 48 Infection cards with appropriate city names and colors
    def __init__(self):
        # First, call parent constructor
        super().__init__()

        # Initializing all 48 Infection cards with appropriate city names and colors.
        self._cardlist.append(InfectionCard("Bogotá", "yellow"))
        self._cardlist.append(InfectionCard("Johannesburg", "yellow"))
        self._cardlist.append(InfectionCard("Buenos Aires", "yellow"))
        self._cardlist.append(InfectionCard("Mexico City", "yellow"))
        self._cardlist.append(InfectionCard("Lima", "yellow"))
        self._cardlist.append(InfectionCard("Los Angeles", "yellow"))
        self._cardlist.append(InfectionCard("Miami", "yellow"))
        self._cardlist.append(InfectionCard("Kinshasa", "yellow"))
        self._cardlist.append(InfectionCard("São Paulo", "yellow"))
        self._cardlist.append(InfectionCard("Santiago", "yellow"))
        self._cardlist.append(InfectionCard("Khartoum", "yellow"))
        self._cardlist.append(InfectionCard("Lagos", "yellow"))

        self._cardlist.append(InfectionCard("Istanbul", "black"))
        self._cardlist.append(InfectionCard("Kolkata", "black"))
        self._cardlist.append(InfectionCard("Tehran", "black"))
        self._cardlist.append(InfectionCard("Cairo", "black"))
        self._cardlist.append(InfectionCard("Algiers", "black"))
        self._cardlist.append(InfectionCard("Moscow", "black"))
        self._cardlist.append(InfectionCard("Chennai", "black"))
        self._cardlist.append(InfectionCard("Karachi", "black"))
        self._cardlist.append(InfectionCard("Delhi", "black"))
        self._cardlist.append(InfectionCard("Mumbai", "black"))
        self._cardlist.append(InfectionCard("Riyadh", "black"))
        self._cardlist.append(InfectionCard("Baghdad", "black"))

        self._cardlist.append(InfectionCard("San Francisco", "blue"))
        self._cardlist.append(InfectionCard("Atlanta", "blue"))
        self._cardlist.append(InfectionCard("Madrid", "blue"))
        self._cardlist.append(InfectionCard("New York", "blue"))
        self._cardlist.append(InfectionCard("Essen", "blue"))
        self._cardlist.append(InfectionCard("Chicago", "blue"))
        self._cardlist.append(InfectionCard("St. Petersburg", "blue"))
        self._cardlist.append(InfectionCard("Montréal", "blue"))
        self._cardlist.append(InfectionCard("London", "blue"))
        self._cardlist.append(InfectionCard("Paris", "blue"))
        self._cardlist.append(InfectionCard("Milan", "blue"))
        self._cardlist.append(InfectionCard("Washington", "blue"))

        self._cardlist.append(InfectionCard("Tokyo", "red"))
        self._cardlist.append(InfectionCard("Beijing", "red"))
        self._cardlist.append(InfectionCard("Shanghai", "red"))
        self._cardlist.append(InfectionCard("Bangkok", "red"))
        self._cardlist.append(InfectionCard("Manila", "red"))
        self._cardlist.append(InfectionCard("Ho Chi Minh City", "red"))
        self._cardlist.append(InfectionCard("Sydney", "red"))
        self._cardlist.append(InfectionCard("Seoul", "red"))
        self._cardlist.append(InfectionCard("Taipei", "red"))
        self._cardlist.append(InfectionCard("Jakarta", "red"))
        self._cardlist.append(InfectionCard("Osaka", "red"))
        self._cardlist.append(InfectionCard("Hong Kong", "red"))

        # Shuffle the deck
        super().shuffle()

    # bottom_card()
    # Returns the bottom card from the deck, removing it from the deck in the process
    # Occurs during 2 - INFECT phase of Epidemics
    def bottom_card(self):
        return self._cardlist.pop()

    # intensify()
    # Reshuffles cards from Infection discard, adds them back to TOP of Infection deck
    # Occurs during 3 - INTENSIFY phase of Epidemics
    def intensify(self, discard_pile):
        discard_pile.shuffle()
        while discard_pile.len() > 0:
            self._cardlist.append(discard_pile.pop())


# PlayerDeck class
# Contains Player cards and behavior unique to Player deck
class PlayerDeck(Deck):

    # Default constructor
    # Initializes 48 City cards (w/ population data), 5 Event cards (NO Epidemic cards yet) 
    def __init__(self):
        # First, call parent constructor
        super().__init__()

        # Initializing all 48 City cards with appropriate city names and colors.
        self._cardlist.append(CityCard("Bogotá", "yellow", 8702000, 21000))
        self._cardlist.append(CityCard("Johannesburg", "yellow", 3888000, 2400))
        self._cardlist.append(CityCard("Buenos Aires", "yellow", 13639000, 5200))
        self._cardlist.append(CityCard("Mexico City", "yellow", 19463000, 9500))
        self._cardlist.append(CityCard("Lima", "yellow", 9121000, 14100))
        self._cardlist.append(CityCard("Los Angeles", "yellow", 14900000, 2400))
        self._cardlist.append(CityCard("Miami", "yellow", 5582000, 1700))
        self._cardlist.append(CityCard("Kinshasa", "yellow", 9046000, 15500))
        self._cardlist.append(CityCard("São Paulo", "yellow", 20186000, 6400))
        self._cardlist.append(CityCard("Santiago", "yellow", 6015000, 6500))
        self._cardlist.append(CityCard("Khartoum", "yellow", 4887000, 4500))
        self._cardlist.append(CityCard("Lagos", "yellow", 11547000, 12700))

        self._cardlist.append(CityCard("Istanbul", "black", 13576000, 9700))
        self._cardlist.append(CityCard("Kolkata", "black", 14374000, 11900))
        self._cardlist.append(CityCard("Tehran", "black", 7419000, 9500))
        self._cardlist.append(CityCard("Cairo", "black", 14718000, 8900))
        self._cardlist.append(CityCard("Algiers", "black", 2946000, 6500))
        self._cardlist.append(CityCard("Moscow", "black", 15512000, 3500))
        self._cardlist.append(CityCard("Chennai", "black", 8865000, 14600))
        self._cardlist.append(CityCard("Karachi", "black", 20711000, 25800))
        self._cardlist.append(CityCard("Delhi", "black", 22242000, 11500))
        self._cardlist.append(CityCard("Mumbai", "black", 16910000, 30900))
        self._cardlist.append(CityCard("Riyadh", "black", 5037000, 3400))
        self._cardlist.append(CityCard("Baghdad", "black", 6204000, 10400))

        self._cardlist.append(CityCard("San Francisco", "blue", 5864000, 2100))
        self._cardlist.append(CityCard("Atlanta", "blue", 4715000, 700))
        self._cardlist.append(CityCard("Madrid", "blue", 5427000, 5700))
        self._cardlist.append(CityCard("New York", "blue", 20464000, 1800))
        self._cardlist.append(CityCard("Essen", "blue", 575000, 2800))
        self._cardlist.append(CityCard("Chicago", "blue", 9121000, 1300))
        self._cardlist.append(CityCard("St. Petersburg", "blue", 4879000, 4100))
        self._cardlist.append(CityCard("Montréal", "blue", 3429000, 2200))
        self._cardlist.append(CityCard("London", "blue", 8586000, 5300))
        self._cardlist.append(CityCard("Paris", "blue", 10755000, 3800))
        self._cardlist.append(CityCard("Milan", "blue", 5232000, 2800))
        self._cardlist.append(CityCard("Washington", "blue", 4679000, 1400))

        self._cardlist.append(CityCard("Tokyo", "red", 13189000, 6030))
        self._cardlist.append(CityCard("Beijing", "red", 17311000, 5000))
        self._cardlist.append(CityCard("Shanghai", "red", 13482000, 2200))
        self._cardlist.append(CityCard("Bangkok", "red", 7151000, 3200))
        self._cardlist.append(CityCard("Manila", "red", 20767000, 14400))
        self._cardlist.append(CityCard("Ho Chi Minh City", "red", 8314000, 9900))
        self._cardlist.append(CityCard("Sydney", "red", 3785000, 2100))
        self._cardlist.append(CityCard("Seoul", "red", 22547000, 10400))
        self._cardlist.append(CityCard("Taipei", "red", 8338000, 7300))
        self._cardlist.append(CityCard("Jakarta", "red", 26063000, 9400))
        self._cardlist.append(CityCard("Osaka", "red", 2871000, 13000))
        self._cardlist.append(CityCard("Hong Kong", "red", 7106000, 25900))

        # Initializing the 5 Event cards.
        self._cardlist.append(EventCard(1))
        self._cardlist.append(EventCard(2))
        self._cardlist.append(EventCard(3))
        self._cardlist.append(EventCard(4))
        self._cardlist.append(EventCard(5))


        # Shuffle the deck
        super().shuffle()

    # prepare()
    # Adds 4, 5, or 6 Epidemic cards to the deck (based on parameter)
    # Shuffles deck according to Step 5 of game setup
    def prepare(self, num_epidemics):
        # Slicing the list into smaller lists.
        if num_epidemics == 4:
            cardlist1 = self._cardlist[0::13]
            cardlist2 = self._cardlist[13::26]
            cardlist3 = self._cardlist[26::39]
            cardlist4 = self._cardlist[39::54]
        elif num_epidemics == 5:
            cardlist1 = self._cardlist[0::11]
            cardlist2 = self._cardlist[11::22]
            cardlist3 = self._cardlist[22::33]
            cardlist4 = self._cardlist[33::44]
            cardlist5 = self._cardlist[44::54]
        elif num_epidemics == 6:
            cardlist1 = self._cardlist[0::9]
            cardlist2 = self._cardlist[9::18]
            cardlist3 = self._cardlist[18::27]
            cardlist4 = self._cardlist[27::36]
            cardlist5 = self._cardlist[36::45]
            cardlist6 = self._cardlist[45::54]

        # Adding in the epidemic cards and shuffling.
        cardlist1.append(EpidemicCard())
        random.shuffle(cardlist1)
        cardlist2.append(EpidemicCard())
        random.shuffle(cardlist2)
        cardlist3.append(EpidemicCard())
        random.shuffle(cardlist3)
        cardlist4.append(EpidemicCard())
        random.shuffle(cardlist4)
        if num_epidemics >= 5:
            cardlist5.append(EpidemicCard())
            random.shuffle(cardlist5)
        if num_epidemics == 6:
            cardlist6.append(EpidemicCard())
            random.shuffle(cardlist6)

        # Adding everything back into the original deck.
        self._cardlist = cardlist1
        self._cardlist.extend(cardlist2)
        self._cardlist.extend(cardlist3)
        self._cardlist.extend(cardlist4)
        if num_epidemics >= 5:
            self._cardlist.extend(cardlist5)
        if num_epidemics == 6:
            self._cardlist.extend(cardlist6)
