# #9 Play again? Again.

def replay():
    while True:
        answer = input("Do you want to play again - Y or N?")
        if answer.lower() == "y":
            return True
        elif answer.lower() == "n":
            return False
        else:
            print("Invalid response!")

replay()
