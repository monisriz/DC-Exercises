# #8 Play again?

def replay():
    answer = input("Do you wnt to play again (Y or N)?")
    if answer.lower() == "y":
        return True
    elif answer.lower() == "n":
        return False
# To make sure:
print(replay())
