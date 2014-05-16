#Dice roll program
#Describe the purpose of this program here.

import random
import time
roll_no = 0
first_no = 9
## this section contains the graphics for displaying the number rolled

s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"
## this is where we roll the dice by generating a random number between 1 and 6
def roll():
#    print("rolling.....") / testing which function I am in
    roll_no = random.randint(1,6)
#    print (roll_no) ## used to check that correct dice was being show for random number generated
    return roll_no

## This section checks to see which number has been rolled and displays the appropriate dice face
def show_dice(roll_no):
#   print("roll") / testing which function I am in
#    print (roll_no) / checking correct parameter has been passed
    if roll_no == 1:
        print(s1)
    if roll_no == 2:
        print(s2)
    if roll_no == 3:
        print(s3)
    if roll_no == 4:
        print(s4)
    if roll_no == 5:
        print(s5)
    if roll_no == 6:
        print(s6)

## Main part of the program, roll dice and then display a dice face
# ask the user if they would like to roll a dice accept upper or lowercase entry
user_input = input("Would you like to roll a dice?(Y/N)")
# Do this if they want to roll the dice
if user_input == "y" or user_input == "Y":
    print ("lets try and roll a six")
    while roll_no != 6:
        roll_no = roll()
        time.sleep(1)
        show_dice(roll_no)
        if roll_no == 6:
            print ("Hooray!!!!")
        else:
            print ("Lets keep going")
    print ("now lets try and roll a double")
    while first_no != roll_no:
        roll_no = roll()
        time.sleep(1)
        show_dice(roll_no)
        if roll_no == first_no:
            print ("Hooray!!!!")
        else:
            print ("Lets keep going")
            first_no = roll_no
            roll_no = 0
        
        
    
# show this message to show that you have understood that they don't want to play
else:
    print("Oh Well!")
