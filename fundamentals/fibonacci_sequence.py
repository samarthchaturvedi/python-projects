# Generate Fibonacci sequence up to N terms

n = int(input("Enter number of terms: "))

if n <= 0:
    print("Please enter a positive number")
else:
    first, second = 0, 1

    for _ in range(n):
        print(first, end=" ")
        next_term = first + second
        first = second
        second = next_term