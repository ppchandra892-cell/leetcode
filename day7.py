#rock paper sessiors
import random

# function to get computer choice
def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

# function to check winner
def check_winner(user, computer):
    if user == computer:
        return "Game Tie"

    elif (user == "Rock" and computer == "Scissors") or (user == "Paper" and computer == "Rock") or (user == "Scissors" and computer == "Paper"):
        return "Game Winner is You"

    else:
        return "Game Winner is Computer"


print("----- Welcome To Rock 🪨 Paper 📃 Scissors ✂️ Game -----")
print("R = Rock | P = Paper | S = Scissors | Q = Quit")

choices = {
    "R": "Rock",
    "P": "Paper",
    "S": "Scissors"
}

while True:
    user_input = input("Enter R/P/S or Q: ").upper()

    if user_input == "Q":
        print("----- Game Over -----")
        break

    if user_input not in choices:
        print("Invalid input! Try again.\n")
        continue

    user_choice = choices[user_input]
    computer_choice = get_computer_choice()

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(check_winner(user_choice, computer_choice))
    print()
