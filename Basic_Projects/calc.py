#print CALCULATOR
#print current date

#accept number 1
#accept operator
#accept number 2

#based on operator run operation and print output then exit

import datetime

print("CALCULATOR\n")
print(f"DATE:- {datetime.date.today()}")


def calculator():
    num1 = float(input("Enter number 1: "))
    operator =input("Enter Operation: ")
    num2 = float(input("Enter Number 2: "))

    calculation = f"{num1} {operator} {num2} ="
    print("\n")
    if operator == "+" : 
        print(f"{calculation} {num1 + num2}")
    elif operator == "-":
        print(f"{calculation} {num1 - num2}")
    elif operator == "*":
        print(f"{calculation} {num1 * num2}")
    elif operator == "/":
        if num2==0:
            print("cannot Divide With Zero")
        else:
            print(f"{calculation} {num1 / num2}")
    else:
        print("Enter Valid Operator")

while True:
    calculator()

    choice = input("enter 'exit' to stop or type anything to continue: ")
    if choice.lower()=="exit":
        break







