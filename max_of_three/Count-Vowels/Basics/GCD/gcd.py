a = int(input("Enter a Number:"))
b = int(input("Enter a Number:"))

gcd = 1
for i in range(1, min(a,b) +1):
    if a%2 == 0 and b%2 == 0:
        gcd = i

print("GCD of", a, "and", b, "is:", gcd)