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

# def get_random_dice():
#     dice_number = random.randint(1, 6)
#     print(f"Dice number is {dice_number}")
#     print(dice_art.get(dice_number))