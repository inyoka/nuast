# A simple subroutine that outputs a user-friendly representation of the stage of the game based on the inpu

def StageOut(num):
    Stages = [
    
'''You have not messed up yet and shouldn't be seeing this'''
    
            ,'''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    
    
    
    
    print("You have "+str((len(Stages)-(num+1)))+" chances left!")
    if num > 0 and num <=7:
        return Stages[num]
    else:
        print("Invalid stage")


if __name__ == "__main__":
   print(StageOut(int(input("Input a stage to test"))))
