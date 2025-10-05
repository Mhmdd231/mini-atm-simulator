Balance = 1000
print("Welcome to the ATM \n\nYour balance is",Balance)

while True:
    print("\n1. Check Balance \n2.Deposit Money \n3.Withdraw Money \n4.Exit\n")
    print("Choose an option:" ,end=" ")
    opt = int(input())

    if opt == 1:
        print("\nYour balance is: ", Balance)

    elif opt == 2:
            print("Enter amount to deposit:" ,end = " ")
            opt_a = int(input())
            Balance += opt_a
            print("Deposit successful. New balance =",Balance)

    elif opt == 3:
        print("Enter amount to withdraw:", end = " ")
        opt_b = int(input())

        if(opt_b <= Balance):
            Balance -= opt_b
            print("Withdrawal successful. New balance = ", Balance)
            

        else:
            print("Insufficient funds!")

    elif opt == 4:
        print("Goodbye!")
        break

    else:
        print("Wrong input.")



