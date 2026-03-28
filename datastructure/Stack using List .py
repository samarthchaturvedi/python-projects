# Stack implementation

stack = []

n = int(input("Enter number of elements: "))

for i in range(n):
    val = int(input("Enter value to push: "))
    stack.append(val)

print("Stack:", stack)

if stack:
    print("Popped:", stack.pop())

print("After pop:", stack)