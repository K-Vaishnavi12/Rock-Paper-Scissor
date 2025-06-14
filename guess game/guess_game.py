import random

def play_game():
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose {computer_choice}.")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

while True:
    play_game()
    if input("Play again? (y/n): ").lower() != "y":
        break
