# Check balanced parentheses

expr = input("Enter expression: ")

stack = []
balanced = True

for ch in expr:
    if ch in "({[":
        stack.append(ch)
    elif ch in ")}]":
        if not stack:
            balanced = False
            break

        top = stack.pop()

        if (ch == ')' and top != '(') or \
           (ch == '}' and top != '{') or \
           (ch == ']' and top != '['):
            balanced = False
            break

if balanced and not stack:
    print("Balanced")
else:
    print("Not Balanced")