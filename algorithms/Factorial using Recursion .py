# Factorial using recursion

def factorial(n):
    # base case
    if n == 0 or n == 1:
        return 1
    
    # recursive case
    return n * factorial(n - 1)

n = int(input("Enter a number: "))

if n < 0:
    print("Factorial not defined for negative numbers")
else:
    print("Factorial is:", factorial(n))