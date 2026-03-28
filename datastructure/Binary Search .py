# Binary search (array must be sorted)

arr = list(map(int, input("Enter sorted elements: ").split()))
target = int(input("Enter target: "))

left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        print("Found at index:", mid)
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print("Not found")