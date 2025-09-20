import random

number = random.randiant(1,15)
guess = int(input("Guess the Number between 1 and 15:"))

if guess == number:
    print("Correct You Guessed it!")

else:
    print(f"Wrong! the number was {number}")
