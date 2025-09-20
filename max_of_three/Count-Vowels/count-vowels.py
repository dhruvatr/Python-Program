vowels = "aeiouAEIOU"
text = input("Enter a Sentence:")
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of Vowels:" , count)
