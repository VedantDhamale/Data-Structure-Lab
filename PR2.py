#Write a Python program that computes the net amount of a bank account based a transaction
#log from console input. The transaction log format is shown as following: D 100 W 200
#(Withdrawal is not allowed if balance is going negative. Write functions for withdraw and
#deposit) D means deposit while W means withdrawal.
#Suppose the following input is supplied to the program:
#D 300, D 300 , W 200, D 100 Then, the output should be:

balance =0
while True:
  
    print("1.Deposit Money")
    print("2.Withdraw Money")
    print("3.Check Balance")
    print("4.Exit")
    choice = int(input("Enter your choice: "))
    if choice== 1:
        D=int(input("Enter amount to deposit: "))
        balance += D
    elif choice == 2:
        W=int(input("Enter amount to withdraw:"))
        if W > balance:
            print("Insufficient Balance")
        else:
            balance -= W
    elif choice == 3:
        print("Balance is:",balance)
    elif choice == 4:
        break;

<--------------------------------OUTPUT-------------------------->
1.Deposit Money
2.Withdraw Money
3.Check Balance
4.Exit
Enter your choice: 1
Enter amount to deposit: 300
1.Deposit Money
2.Withdraw Money
3.Check Balance
4.Exit
Enter your choice: 1
Enter amount to deposit: 300
1.Deposit Money
2.Withdraw Money
3.Check Balance
4.Exit
Enter your choice: 2
Enter amount to withdraw:200
1.Deposit Money
2.Withdraw Money
3.Check Balance
4.Exit
Enter your choice: 1
Enter amount to deposit: 100
1.Deposit Money
2.Withdraw Money
3.Check Balance
4.Exit
Enter your choice: 3
Balance is: 500
1.Deposit Money
2.Withdraw Money
3.Check Balance
4.Exit
Enter your choice: 4
