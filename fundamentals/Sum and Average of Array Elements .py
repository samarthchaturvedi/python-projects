# Calculate sum and average of elements in a list

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

if len(numbers) == 0:
    print("List is empty")
else:
    total = 0

    for num in numbers:
        total += num

    average = total / len(numbers)

    print("Sum:", total)
    print("Average:", average)