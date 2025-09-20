balance = 0

while True:
    print("\n--- Bank Menu---")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.check balance")
    print("4.exit")

    choice = int(input("Enter a choice (1-4):"))

    if choice == 1:
        amount = float(input("Enter a amount to deposit:"))
        balance += amount
        print("Deposited:", amount)

    elif choice == 2:
        amount = float(input("Enter a amount to withdraw: $"))
        if amount <= balance:
            balance -= amount
            print("withdrawn:", amount)

        else:
            print("Insufficient balance!:")

    elif choice == 3:
        print("Your Balance is:", balance)

    elif choice == 4:
        print("Thank you for using our bank system!")
        break

    else:
        print("Invalid choice! please enter (1-4).")

    
