# Find sum of all elements

arr = list(map(int, input("Enter elements: ").split()))

total = 0
for num in arr:
    total += num

print("Sum:", total)