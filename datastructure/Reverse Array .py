# Reverse an array manually

arr = list(map(int, input("Enter elements: ").split()))

reversed_arr = []

for i in range(len(arr)-1, -1, -1):
    reversed_arr.append(arr[i])

print("Reversed array:", reversed_arr)