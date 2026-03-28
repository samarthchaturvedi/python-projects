# Advanced Calculator

import math

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1.+ 2.- 3.* 4./ 5.Power")
ch = input("Choice: ")

if ch == '1':
    print(a + b)
elif ch == '2':
    print(a - b)
elif ch == '3':
    print(a * b)
elif ch == '4':
    print(a / b)
elif ch == '5':
    print(math.pow(a, b))