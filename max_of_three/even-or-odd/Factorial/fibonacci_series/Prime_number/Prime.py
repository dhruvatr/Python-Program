num = int(input("Enter a Number:"))

if num > 1:
    for i in range(2, num):
        if num%i==0:
            print(f"{num} is NOT a Prime Number:")
            break

    else:
        print(f"{num} is a Prime Number:")
            
