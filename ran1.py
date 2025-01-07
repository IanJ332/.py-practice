import random

# .randint() it will give random integer between a and b
# print( random.randint(1,10) )

# .random() it will give a float number
# print( random.random() )

# This is pick a random choise form the list
import random

options = ['rock', 'paper', 'scissors']
random_choice = random.choice(options)
choice = input("Choose rock, paper or scissors: ").lower()

while choice not in options:
    choice = input("Please choose rock, paper or scissors: ").lower()

print(f"Computer chose: {random_choice}")

if random_choice == choice:
    print("Tie!")
elif (random_choice == 'rock' and choice == 'scissors') or \
     (random_choice == 'paper' and choice == 'rock') or \
     (random_choice == 'scissors' and choice == 'paper'):
    print("Ops! You lose!")
else:
    print("You win!")

# This is how you shuffle your list
# cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# random_card = random.choice(cards)
# random.shuffle(cards)

# guesses = 0
# low = int(input("Enter the low range: "))
# high = int(input("Enter the high range: "))
# number = random.randint(low,high)
# guess = int(input(f"Guess a number between {low} and {high}: "))
# while guess != number:
#     guesses += 1
#     if guesses == 5:
#         print(f"You have run out of guesses, you lose! The correct number was: {number}")
#         break
#     if guess < number:
#         print("Too low!")
#     else:
#         print("Too high!")
#     guess = int(input("Guess again: "))
#     if guess == number:
#         print(f"Congratulations! You guessed the number {number} correctly!")
