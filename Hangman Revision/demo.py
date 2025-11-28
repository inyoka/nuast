def answerYorN():
    success = False
    while success != True:
        Input = input("Yes or No?(Y or N): ")
        if Input.lower() == "y":
            Valid = Input.lower()
            success = True
        elif Input.lower() == "n":
            Valid = Input.lower()
            success = True
        else:
            success = False
    return Valid

response = answerYorN()