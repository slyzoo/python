#---------------------------------------------------------------------------------------------------
import random
while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

#---------------------------------------------------------------------------------------------------


    while player not in choices:
        player = input("rock, paper, or scissors: ").lower()

#---------------------------------------------------------------------------------------------------

    if player == computer:

        print("player chose: " + player)
        print("computer chose: " + computer)
        print("TIED!")

#---------------------------------------------------------------------------------------------------

    elif player == "rock":
        if computer=="paper":

            print("player chose: " + player)
            print("computer chose: " + computer)
            print("YOU LOSE!")

#---------------------------------------------------------------------------------------------------

        if computer=="scissors":

            print("player chose: " + player)
            print("computer chose: " + computer)
            print("YOU WIN!")

#---------------------------------------------------------------------------------------------------

    elif player == "paper":
        if computer=="scissors":

            print("player chose: " + player)
            print("computer chose: " + computer)
            print("YOU LOSE!")

#---------------------------------------------------------------------------------------------------

        if computer=="rock":

            print("player chose: " + player)
            print("computer chose: " + computer)
            print("YOU WIN!")

#---------------------------------------------------------------------------------------------------

    elif player == "scissors":
        if computer=="rock":

            print("player chose: " + player)
            print("computer chose: " + computer)
            print("YOU LOSE!")

#---------------------------------------------------------------------------------------------------

        if computer=="paper":

            print("player chose: " + player)
            print("computer chose: " + computer)
            print("YOU WIN!")

#---------------------------------------------------------------------------------------------------

    play_again = input("play again? (yes / no): ").lower()

    if play_again != "yes":
        break
    
print("goodbye")
