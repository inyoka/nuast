'''
This will manage importing and saving flashcards
'''
import os
import keyboard
from simple_colors import *
class FileManager:
    def __init__(self,argument,action="ActionSelect",StartDir="./Hangman Revision/Flashcard Storage/"):
        self.action = action
        self.argument = argument
        self.StartDir = StartDir
        print("Welcome to File Manager!")
        if action == "ActionSelect" and argument == None:
            self.ActionSelect(self)
    # FileManager(action(argument))
        
        
    def ActionPresent(self):
        argument = input("What option would you like to choose?" \
        "Select(S)" \
        "Create(C)" \
        "Delete(D)" \
        "View(V)" \
        "Exit(E)")
        return argument
    
    def SetPathList(self,path):
        returned = os.listdir(path)
        return returned

    def SelectPath(self,StartDir):
        SelectorRunning = True
        CurrentSelectionIndex = 0
        CurrentDir = StartDir
        PathList = self.SetPathList(CurrentDir)
        while SelectorRunning != False:
            for i in range(len(PathList)):
                if i == CurrentSelectionIndex:
                    print(green(PathList[i]))
                else:
                    print(PathList[i])    
            if keyboard.read_key() == "<":
                PathList[CurrentSelectionIndex-1] = PathList[CurrentSelectionIndex]
                CurrentSelectionIndex -= 1
            elif keyboard.read_key() == ">":
                PathList[CurrentSelectionIndex+1] = PathList[CurrentSelectionIndex]
                CurrentSelectionIndex += 1
            elif keyboard.read_key() == "enter":
                split = os.path.splitext(PathList[CurrentSelectionIndex])
                if split[1] == None:
                    CurrentDir = CurrentDir.append(split[0]+"/")
                else:
                    print("Not Added yet")
                return PathList[CurrentSelectionIndex]


    def ActionSelect(self,argument):
        doyk = input("Do you know the options? (Y or N): ")
        if doyk.lower() != "y":
            argument = FileManager.ActionPresent(self)
        if argument.lower() == "n":
            os.listdir()


if __name__ == "__main__":
    Files = FileManager("Y")
    print(str(Files.StartDir))
    Files.SelectPath(Files.StartDir)