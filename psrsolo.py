import random

user = input("Your Name: ")
user_wins = 0
pc_wins = 0

options = ["paper", "scisscors", "rock"]

while True:
    user_input = input("Style: Paper/Scissors/Rock or Q für Cancel: ").lower()
    if user_input == "q":
        break

    elif user_input not in options:
        print("Invalid!")
        continue




    pc_input = random.choice(options)
    print("Computer Choose " + pc_input)

    if user_input == "paper" and pc_input == "rock" or user_input == "scissors" and pc_input == "paper" or user_input == "rock" and pc_input == "scissors":
        print("You Won!")
        user_wins += 1
        print(user, "has", user_wins, "Points!")
        print("Computer has", pc_wins, "Points!")
        continue

    elif user_input == "paper" and pc_input == "paper" or user_input == "scissors" and pc_input == "scissors" or user_input == "rock" and pc_input == "rock":
        print("Both the Same! Continue!")
        print(user, "has", user_wins, "Points!")
        print("Computer has", pc_wins, "Points!")
        continue

    else:
        print("You Lost!")
        pc_wins += 1
        print(user, "has", user_wins, "Points!")
        print("Computer has", pc_wins, "Points!")
        continue
