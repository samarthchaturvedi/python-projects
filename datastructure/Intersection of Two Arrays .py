# Find intersection of two arrays

arr1 = list(map(int, input("Enter first array: ").split()))
arr2 = list(map(int, input("Enter second array: ").split()))

intersection = []

for i in arr1:
    if i in arr2 and i not in intersection:
        intersection.append(i)

print("Intersection:", intersection)