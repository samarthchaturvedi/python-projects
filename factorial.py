number = int(input("Enter a number: "))

if number < 0:
    print("Factorial not defined for negative numbers")
else:
    factorial = 1

    # Multiply numbers from 1 to n
    for i in range(1, number + 1):
        factorial *= i

    print("Factorial =", factorial)