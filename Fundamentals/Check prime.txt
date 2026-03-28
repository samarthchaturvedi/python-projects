number = int(input("Enter a number: "))

# Numbers less than 2 are not prime
if number < 2:
    print("Not a prime number")
else:
    is_prime = True

    # Check divisibility up to square root for efficiency
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    print("Prime number" if is_prime else "Not a prime number")
    