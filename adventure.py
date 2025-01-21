"""
   Name: adventure.py
   Author: Juan Ardon
   Created: 3/01/2023
   Purpose: Create a Game
"""
import sys

def main():
    # Start the game
    start()

#---------------------------START--------------------------------#
def start():
    # Prompt the user for input
    print("\nThe road that you are in, will be closed in 5 miles.")
    print("There is 1 street to the left and another to the righ before getting to the obstruction.")
    print("which one do think it will be the faster? (1 or r)")

    # Convert the player's input () to lower_case
    answer =input("> ").lower()

    if "1" in answer:
        # if the player choose left or 1 take him to street Hollow_Rd()
        hollow_rd("Are you ready for what's coming?")
        
    elif "r" in answer:
        # Else if player choose rigth or r lead him to the Bones_Rd()
        bones_rd("You may enconter the death himself.")
        
    else:
        # Call game_over() fuction with the reason argument
        game_over("Try again!")

#----------------------Hollow Rd---------------------------------#
def hollow_rd(message):
    print(message)
    # Tell the story to This point
    # Prompt the user for input
    print("You are in the Hollow Rd, Welcome:>.")
    print("This road looks so creapy.")
    print("In the next 1 mile there is an exit.")
    print("(1). Stay in Hollow rd.")
    print("(2). Take the exit. " )

    # Get User Imput 
    answer = input("> ")

    if answer == "1":
        # The player chooses to stay in the Hollow Rd
        game_over("You are in the Hollow Rd for the next 100 miles.")
    elif answer == "2":
        # The player take the exit, lead him to the Arcangel_Dr()
        archangel_rd("\nYou has arrive to the exit, take it!")
        
    else:
        # Call game_over () function with the "reason" argument
        game_over("Try again.")
#--------------------Bones Rd-------------------------------------#
def bones_rd(message):
    print(message)
    # Tell the story to This point
    # Prompt the user for input
    print("You are in the Bones Rd, Welcome:>.") 
    print("There is a person in the middle of the road.")
    print("He ask for help, but you can't see his face.")
    print("(1). Stop the car and help him.")
    print("(2). Keep going and go faster as you can and take the next exit. ")

    # Get User Imput 
    answer = input("> ")

    if answer == "1":
        # The player is killed by a sataninc creature
        game_over("The sataninc creature that looked like human fool you and killed you.")
    elif answer == "2":
        # The player din't stop and has to faster as he can and lead him to the Valley_St()
        valley_st("\nYou has entered the Valley St.")
        
    else:
        # Call game_over () function with the "reason" argument
        game_over("Try again.")
#-------------------Arcangel Rd------------------------------------#
def archangel_rd(message):
    print(message)
    # Tell the story to This point
    # Prompt the user for input
    print("You are in the Archangel Rd, Welcome:).")
    print("The road looks amazing with incredible mountains.")
    print("In the next 2 miles there is an exit to go more down to the mountains. ")
    print("(1). Stay in the same road.")
    print("(2). Take the exit.")

    # Get User Imput 
    answer = input("> ")

    if answer == "1":
        # The player choose to stay in the same road.
        game_over("You are in the Archangel Rd for the next 50 miles.")
    elif answer == "2":
        # The player decide to take the exit, lead him to the Valley_St()
        valley_st("\nYou are going down the mountain on Valley St.")
        
    else:
        # Call game_over () function with the "reason" argument
        game_over("Try again.")

#-----------------Valley St------------------------------------------#
def valley_st(message):
    print(message)
    # Tell the story to This point
    # Prompt the user for input
    print("You are on Valley st, Welcome:).")
    print("This street will guide you to your destination.")
    print("(1). Stay in the road until you has reached your final destination.")
    print("(2). Look for another road.")
     # Get User Imput 
    answer = input("> ")

    if answer =="1":
        # The player only option is to continue trogth valley st until he reach his destination.
        game_over("You will be arriving at yor destination in the next 72 miles. ")
    elif answer == "2":
        # The player want to look for another road, lead him to the hollow.rd()
        hollow_rd("You are going back to Hollow road and find other way there.")
    else:
        # Call game_over () function with the "reason" argument
        game_over("Try again.")

#---------------Game Over---------------------------------------------#
def game_over(reason):
    # Print the reason in a new line (\n)
    print("\n" + reason)
    print("Game Over!")

    # Ask player to play again or not by activation play_again() function
    play_again()

#--------------Play Again---------------------------------------------#
def play_again():
    print("\nDo you want to play again? (y or n)")

    # Convert the player input to lower_case
    answer = input("> ").lower()

    if "y" in answer:
        # if player choose yes or y start the game from the beginning
        start()
    else:
        # If user types anything besides yes or y, exit() the program
        sys.exit()

#----------------------------------------------------------------------#
#If standalone, run function
#Else, run as module
if __name__ == "__main__":
    main()