# Count frequency of each element in a list

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Element frequencies:")

for key in frequency:
    print(f"{key} -> {frequency[key]}")