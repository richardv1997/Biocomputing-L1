#Calculator program
#if , elif and else, make sure theres no spaces and remember at add :
#else:

import math
print("Welcome to the Calculator")
print("(-) Subtraction ")
print("(+)) Addition ")
print("(*) Multiplication ")
print("(/) Division ")
print("(^) Exponentiation ")
print("(!) Square root of (This will be your first number)")

num1= float(input("Please enter your first number:"))

sign= input("Please enter a mathematical symbols (*,+,-, /,^,!):")

num2= float(input("Please enter your second number:"))

if sign == "+":
    result= num1+num2
    print(round(result,2))
elif sign == "-":
    result = num1 - num2
    print(round(result,2))
elif sign== "*":
    result= num1 * num2
    print(round(result,2))
elif sign== ("/"):
    result= num1 / num2
    print(round(result,2))
elif sign == ("^"):
    result = pow(num1,num2)
    print(round(result, 2))
elif sign == ("!"):
    result = math.sqrt(num1)
    print(round(result,2))
else:
    print(f"{sign} is not a vaild operator.")