# Find the second largest element in a list

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

n = len(numbers)

if n < 2:
    print("Need at least two elements")
else:
    largest = second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float('-inf'):
        print("No second largest element (all elements may be equal)")
    else:
        print("Second largest element:", second_largest)