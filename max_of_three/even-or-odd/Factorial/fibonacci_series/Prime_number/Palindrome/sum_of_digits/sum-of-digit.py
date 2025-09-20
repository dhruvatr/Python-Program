num = int(input("Enter a Number:"))
total = 0

while num > 0:
    digit = num % 10
    total += 10
    num //= 10

print("som of digits is:", total)

