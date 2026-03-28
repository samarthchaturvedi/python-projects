# Circular queue (basic)

size = int(input("Enter size: "))
cq = [None] * size

front = -1
rear = -1

val = int(input("Enter value: "))

if (rear + 1) % size == front:
    print("Queue Full")
else:
    if front == -1:
        front = 0
    rear = (rear + 1) % size
    cq[rear] = val

print("Circular Queue:", cq)