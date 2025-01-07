import random

import random

dice_art = {
    1: (
        " ------- \n"
        "|       |\n"
        "|   o   |\n"
        "|       |\n"
        " ------- "
    ),
    2: (
        " ------- \n"
        "| o     |\n"
        "|       |\n"
        "|     o |\n"
        " ------- "
    ),
    3: (
        " ------- \n"
        "| o     |\n"
        "|   o   |\n"
        "|     o |\n"
        " ------- "
    ),
    4: (
        " ------- \n"
        "| o   o |\n"
        "|       |\n"
        "| o   o |\n"
        " ------- "
    ),
    5: (
        " ------- \n"
        "| o   o |\n"
        "|   o   |\n"
        "| o   o |\n"
        " ------- "
    ),
    6: (
        " ------- \n"
        "| o   o |\n"
        "| o   o |\n"
        "| o   o |\n"
        " ------- "
    )
}

# dice_number = random.randint(1, 6)
# print(dice_art.get(dice_number))

# for i in range(1, 7):
#     print(dice_art.get(i))

def get_random_dice():
    dice_number = random.randint(1, 6)
    return dice_number
    # print(f"Dice number is {dice_number}")
    # print(dice_art.get(dice_number))

num1 = []
num2 = []
dice_roll = int(input("Enter the dice roll number: "))


for i in range(1, dice_roll + 1):
    temp = get_random_dice()
    temp_2 = get_random_dice()
    print(f"The {i} time roll is {temp}")
    print(dice_art.get(temp))
    num1.append(temp)
    num2.append(temp_2)
    print(f"Your total is {sum(num1)}")
    print(f"The bot total is {sum(num2)}")

if sum(num1) == sum(num2):
    print("It's a tie")
elif sum(num1) > sum(num2):
    print("Player wins")
else:
    print("Bot wins")

