# Merge two lists and remove duplicates (without using set)

list1 = list(map(int, input("Enter first list elements: ").split()))
list2 = list(map(int, input("Enter second list elements: ").split()))

merged_list = []

# Add elements from first list
for num in list1:
    if num not in merged_list:
        merged_list.append(num)

# Add elements from second list
for num in list2:
    if num not in merged_list:
        merged_list.append(num)

print("Merged list without duplicates:", merged_list)