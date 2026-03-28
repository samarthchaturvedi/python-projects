# Find maximum and minimum element in array

arr = list(map(int, input("Enter elements: ").split()))

max_val = arr[0]
min_val = arr[0]

for num in arr:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print("Maximum:", max_val)
print("Minimum:", min_val)