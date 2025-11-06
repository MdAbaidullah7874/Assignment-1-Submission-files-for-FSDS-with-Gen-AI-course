# Assignment 10
units = int(input("Enter number of units consumed: "))

bill = 0.0

if units <= 100:
    bill = units * 5
elif units <= 200:
    first_100_bill = 100 * 5
    remaining_units = units - 100
    remaining_bill = remaining_units * 7
    bill = first_100_bill + remaining_bill
else:
    first_100_bill = 100 * 5
    second_100_bill = 100 * 7
    remaining_units = units - 200
    remaining_bill = remaining_units * 10
    bill = first_100_bill + second_100_bill + remaining_bill

print("Total payable amount:", bill, "RS")