# Reverse string using stack

string = input("Enter string: ")

stack = []

for ch in string:
    stack.append(ch)

reversed_string = ""

while stack:
    reversed_string += stack.pop()

print("Reversed string:", reversed_string)