# Sort a list using Bubble Sort (without built-in functions)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

n = len(numbers)

if n == 0:
    print("List is empty")
else:
    # Bubble Sort Algorithm
    for i in range(n):
        swapped = False  # Optimization to stop early if already sorted

        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                # Swap elements
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
                swapped = True

        # If no swaps happened, list is already sorted
        if not swapped:
            break

    print("Sorted list:", numbers)