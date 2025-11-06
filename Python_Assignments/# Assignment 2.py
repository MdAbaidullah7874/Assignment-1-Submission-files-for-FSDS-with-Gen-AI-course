# Assignment 2
account_balance = float(input("Enter your current account balance: "))
withdraw_amount = float(input("Enter the amount you want to withdraw: "))

if withdraw_amount > account_balance:
    print("Insufficient Balance")
else:
    remaining_balance = account_balance - withdraw_amount
    print("Transaction Successful")
    print("Your remaining balance is: ", remaining_balance)