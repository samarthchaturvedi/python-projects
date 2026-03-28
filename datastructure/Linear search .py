# Linear search implementation

arr = list(map(int, input("Enter elements: ").split()))
target = int(input("Enter target: "))

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index:", i)
        break
else:
    print("Not found")