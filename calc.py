# Project name : calculator
# Author : Abhishek Prajapati
# Date : October 11th, 2020;


a = int(input("Please Enter first number:"))

b = int(input("Please Enter second number: "))

print("What operation do you want to perform ? PPlease Enter in capital letters:")

print("Enter A >> for addition",
       "\nEnter S >> for substraction",
       "\nEnter M >> for multiplication",
       "\nEnter D >> for division",
       "\nEnter R >> for remainder after division")

operator = input("Enter here >>>")

def add(num1, num2):
    print(num1+num2)

def substract(num1, num2):
    if num1>num2:
        print(num1-num2)
    else:
        print(num2-num1)

def multiplication(num1, num2):
    print(num1*num2)

def division(num1, num2):
    if num1>num2:
        print(num1/num2)
    else:
        print(num2/num1)

def modulation(num1, num2):
    if num1>num2:
        print(num1%num2)
    else:
        print(num2%num1)

if operator == "A":
    add(a, b)
elif operator == "S":
    substract(a, b)
elif operator == "M":
    multiplication(a, b)
elif operator == "D":
    division(a, b)
else:
    modulation(a, b)
