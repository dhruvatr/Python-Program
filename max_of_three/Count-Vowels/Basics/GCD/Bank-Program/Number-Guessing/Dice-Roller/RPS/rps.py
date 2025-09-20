import random

options = ["rock","paper","scissors"]

user = input("Enter rock,paper,scissors: ").lower()
computer = random.choice(options)

print(f"computer chose: {computer}")

if user == computer:
    print("it is a tie:")
elif(
    (user == "rock" and computer == "scissors")or
    (user == "paper" and computer == "rock") or
    (user == "scissors" and computer == "paper")
    ):
    print("you win")

else:
    print("you lose")

