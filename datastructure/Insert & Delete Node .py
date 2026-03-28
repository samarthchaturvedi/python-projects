# Insert and delete node

val = int(input("Enter value to insert at beginning: "))

new_node = Node(val)
new_node.next = head
head = new_node

print("Inserted at beginning")

if head:
    head = head.next
    print("Deleted first node")