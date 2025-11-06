# Assignment 4
age = int(input("Enter your age: "))

if age < 5:
    print("Ticket Price: Free")
elif age <= 18:
    print("Ticket Price: 50% Discount")
elif age >= 60:
    print("Ticket Price: 30% Discount")
else:
    print("Ticket Price: Full Price")