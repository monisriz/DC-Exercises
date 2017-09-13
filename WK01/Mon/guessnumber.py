# Guess a number
import random
replay = "Y"
while replay == "Y":
    secretnum = random.randint(1, 10)
    guessleft = 5
    print("I am thinking of a number between 1 and 10.")

    while guessleft > 0:
        yournum = int(input("Guess a number: "))
        guessleft -= 1
        print("You guessed: {}. Guesses left: {}.".format(yournum, guessleft))
        if yournum < 1 or yournum > 10:
            print("I said your guess has got to be between 1 and 10!")
        elif yournum < secretnum:
            print(yournum, "is too low")
        elif yournum > secretnum:
            print(yournum, "is too high")
        else:
            print("You win!")
            break
        if guessleft == 0:
            print("You lose. You ran out of guesses!")
            break

    while True:
        replay = input("Do you want to play again? - (Y or N): ").upper()
        if replay == "Y":
            guessleft = 5
            break
        elif replay == "N":
            print("GAME OVER!")
            break
