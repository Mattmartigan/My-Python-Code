
import random
outcomes = ['r','p','s']
play = "y"
losses = {"r":"p","p":"s","s":"r"}
while play == "y":
    compthrow = random.choice(outcomes)
    throw = input("Input (R) for Rock, (P) for Paper or (S) for Scissors: ")
    print("Computer throws: {}".format(compthrow))
    if throw not in losses:
        print("you must enter r,p,s")
    elif losses[throw]==compthrow:
            print("You lose")
    elif throw == compthrow:
        print("Draw")
    else:
        print("You Win!")
    play = input("Play again?")
