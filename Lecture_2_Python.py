# """
# Exercise -1
# Find the minimum from 3 givven number
# """

# num1 = input("Enter fist number:")
# num2 = input("Enter scond number:")
# num3 = input("Enter third number:")

# print(num1,num2,num3)

# if num1<num2 and num1<num3: 
#     print("minimum number is:",num1)

# elif num2<num1 and num2<num3:
#     print("minimum number is:",num2)

# else:
#     print("minimum number is:",num3)



"""
Exercise -2
ATM Machin menu

1. pin change
2. blance check
3. withdral
4. deposite
5. exit
"""


menu = input("""
hi there ! welcome to ATM
please choose,
1. enter 1 for pin change
2. enter 2 for blance check
3. enter 3 for withdral
4. enter 4 for deposite
5. enter 5 for exit
""")

if menu == "1":
    print("pin change")
elif menu == "2":
    print("blance check")
elif menu == "3":
    print("withdral")
elif menu == "4":
    print("deposite")


else:
    print("exit")

