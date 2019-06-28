import random
outcomes = ['r','p','s']
play = "y"
while play == "y":
    compthrow = random.choice(outcomes)
    throw = input("Input (R) for Rock, (P) for Paper or (S) for Scissors: ")
    print("Computer throws: {}".format(compthrow))

    if throw == compthrow:
        print("Draw")
    elif throw == "r" and compthrow == "s":
        print("You Win!")
    elif throw == "s" and compthrow == "r":
        print("You Lose")
    elif throw == "r" and compthrow == "p":
        print("You Lose")
    elif throw == "p" and compthrow == "r":
        print("You Win!")
    elif throw == "s" and compthrow == "p":
        print("You Win!")
    elif throw == "p" and compthrow == "s":
        print("You Lose")
    else:
        print("you must enter r,p,s")

    play = input("Play again?")
