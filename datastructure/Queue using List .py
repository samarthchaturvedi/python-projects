# Queue implementation

queue = []

n = int(input("Enter number of elements: "))

for i in range(n):
    val = int(input("Enter value: "))
    queue.append(val)

print("Queue:", queue)

if queue:
    print("Dequeued:", queue.pop(0))

print("After dequeue:", queue)