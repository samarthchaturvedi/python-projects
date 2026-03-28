# Traverse linked list

temp = head

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")