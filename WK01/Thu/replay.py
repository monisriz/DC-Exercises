# #8 Play again?

def replay():
    answer = input("Do you wnt to play again (Y or N)?").upper()
    if answer == "Y":
        return True
    elif answer == "N":
        return False
# To make sure:
print(replay())
