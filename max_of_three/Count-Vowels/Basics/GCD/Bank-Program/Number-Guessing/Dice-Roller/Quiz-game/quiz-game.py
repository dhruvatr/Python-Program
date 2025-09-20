print("Welcome to The Quiz Game:")

question = "What is the capital of India?"
answer = "delhi"

user_answer = input(question + " ").lower()

if user_answer == answer:
    print("Correct")
else:
    print("wrong! The correct answer is Delhi.")
