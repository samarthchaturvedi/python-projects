# Find first and last occurrence

arr = list(map(int, input("Enter elements: ").split()))
target = int(input("Enter target: "))

first = -1
last = -1

for i in range(len(arr)):
    if arr[i] == target:
        if first == -1:
            first = i
        last = i

print("First:", first)
print("Last:", last)