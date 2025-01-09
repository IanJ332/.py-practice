import random
print("Welcome to the Rock Paper Scissors Game!")

def play_game():
    print("What is your choice? (rock, paper, scissors)")
    user_choice = input()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        return

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You lose!")
    else:
        print("You win!")

want_play = input("Do you want to play? (yes/no) ")

while want_play.lower() == "yes":
    play_game()
    want_play = input("Do you want to play again? (yes/no) ")
print("Thanks for playing!")