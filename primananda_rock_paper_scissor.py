import random

print("This game was made by Primananda Andhika\nYou can visit my github on https://github.com/ItsAndhika \nEnjoy!")
user_choice = str(input("Choose between rock, paper, or scissor : ")).lower()
choices = ["rock", "paper", "scissor"]
computer_choice = random.choice(choices)

print("You choose ", user_choice, " and computer chooses ", computer_choice)

if user_choice == computer_choice:
    print("Both players selected the same choice. Tie game!")
elif user_choice == "rock":
    if computer_choice == "scissor":
        print("You win!")
    else:
        print("You lose!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    else:
        print("You lose!")
elif user_choice == "scissor":
    if computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!")
else:
    print("Please choose between rock, paper, or scissor")
