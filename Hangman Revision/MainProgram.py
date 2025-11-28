'''

This is the main program!!!
This will join the modules together


'''

from Game import Game


global VersionOfProgram
VersionOfProgram = 0.2

print("Welcome to the Hangman Revision Game!\n"+"Current Version:"+str(VersionOfProgram))

def GameLoop():
    Stopping = False
    while Stopping != True:             #Keep main game in a loop so that it runs forever.
        MenuSelection = input("Select an option: \nPlay(P) \nChoose Deck(CD), \nDeck Manager(DM)), \nExit(E).\n(Options:P, CD, DM, E): ")

        if MenuSelection.lower() == "cd":   
            print("This hasn't been implemented properly yet, so you can only choose defualt")          # Will implement proper system in future release
            DeckSelection = input("Select deck: Defualt(D)")
            if DeckSelection.lower() == "d":
                CurrentDeck = {
                "Properties":{
                    "Deckname" : "Development deck",
                    "Date Created" : "26/11/2025",
                    "Created by" : "Default" #A user system might be implemented later 
                },
                1 : {
                "Decomposition/Procedural thinking" : "breaking down problems into smaller, more manageable tasks."
                },
                2 : {
                "Abstraction" : "Removing unnecessary data from a piece of information to make it easier to understand for the average user."    
                },
                3 : {
                "Thinking Ahead" : "Identifying the preconditions of a system: inputs, outputs, and reusable components."    
                } 
                }
            else:
                print("Invalid Selection, returning to title screen...")
        elif MenuSelection.lower() == "dm":
            pass
        elif MenuSelection.lower() == "dd":
            pass
        elif MenuSelection.lower() == "e":
            Stopping = True
        elif MenuSelection.lower() == "p":
            print("Game starting!")
            CurrentGame = Game(CurrentDeck)
            print(CurrentGame)
            print(CurrentGame.decklength)
        else:
            print("Invalid Option!")

GameLoop()