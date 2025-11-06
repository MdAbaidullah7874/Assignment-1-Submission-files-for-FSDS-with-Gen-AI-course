# Assignment 9
age = int(input("Enter your age: "))
qualification = input("Enter your qualification (e.g., graduate): ").lower()

if age >= 18 and qualification == "graduate":
    print("Eligible for Job")
else:
    print("Not Eligible")