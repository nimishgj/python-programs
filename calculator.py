import math


def add():
    sum = 0
    choice = int(input("Enter the number of elements you want to add:"))
    for i in range(choice):
        sum = sum + float(input("Enter the number:"))
    return sum


def sub():
    diff = 0
    choice = int(
        input("Enter the number of subtractions you want to perform:"))
    for i in range(choice):
        diff = diff - float(input("Enter the number:"))
    return diff


def multiply():
    product = 1
    choice = int(
        input("Enter the number of multiplication you want to perform:"))
    for i in range(choice):
        product = product * float(input("Enter the number:"))
    return product


def div():
    return float(input("Enter the dividend:")) / float(input("enter the divisor"))


def pow():
    return float(input("Enter the base:")) ** int(input("Enter the order:"))


print("\n\n\n\n" + "*"*20 + "CALCULATOR" + "*"*20 +
      "Calculations available:\n->Addition\n->Subtraction\n->Division\n->Multiplication\n->Power\n->Square Root\n->Sin(x)\n->Cos(x)\n->Tan(x)\n->cosh(x)\n->sinh(x)")
ch = input("Enter your calculation")
