n = int(input("Enter the Terms:"))

a,b=0,1
print("Fabonacci Series:")

for i in range(n):
    print(a, end=" ")
    a, b=b, a+b
