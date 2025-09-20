import random

secret_number = random.randint(1,15)

print("Welcome to the number guessing Game!")
print("I have chosen a number between 1 and 15. Try to guess it!")

while True:
    guess = int(input("Enter your guess:"))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congrajulations! you guessed it right.")
        break
