# Assignment 5
total_bill = float(input("Enter the total bill amount: "))

if total_bill > 1000:
    discount = total_bill * 0.10
    final_bill = total_bill - discount
else:
    final_bill = total_bill

print("Your final payable bill is: ", final_bill)