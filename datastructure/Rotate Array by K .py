# Rotate array to right by k positions

arr = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter k: "))

n = len(arr)
k = k % n

rotated = []

for i in range(n-k, n):
    rotated.append(arr[i])

for i in range(0, n-k):
    rotated.append(arr[i])

print("Rotated array:", rotated)