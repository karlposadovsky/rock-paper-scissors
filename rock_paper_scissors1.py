import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1  # all caps/constant variable
    PAPER = 2
    SCISSORS = 3


# print(RPS.ROCK)
# print(RPS(2))
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# sys.exit()
player_choice = input("""\nEnter...\n1 For Rock\n2 for Paper or, \n3 for Scissors:\n\n""")
player = int(player_choice)

if player < 1 or player > 3:
    sys.exit("You must enter 1,2 or 3")

computer = random.randint(1, 3)

print(f"\nPlayer's choice is " + str(RPS(player)).replace("RPS.", "") + ". Computer's choice is " + str(RPS(computer)).replace("RPS.", "") + ".")

if player == computer:
    print("It's a tie.😒")
elif player == 1:
    if computer == 2:
        print("Rock smashes scissors. You win!🥷🏻")
    else:
        print("Paper covers rock. You lose.🤮")
elif player == 2:
    if computer == 1:
        print("Paper covers rock. You win!🥷🏻")
    else:
        print("Scissors cuts paper. You lose.🤮")
elif player == 3:
    if computer == 2:
        print("Scissors cut paper. You win!🥷🏻")
    else:
        print("Rock smashes scissors. You lose.🤮")


