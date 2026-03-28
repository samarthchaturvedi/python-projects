# Check whether a number is an Armstrong number

number = int(input("Enter a number: "))

original_number = number
num_digits = len(str(number))
result = 0

# Calculate sum of digits raised to power of number of digits
while number > 0:
    digit = number % 10
    result += digit ** num_digits
    number //= 10

# Compare result with original number
if result == original_number:
    print("Armstrong number")
else:
    print("Not an Armstrong number")