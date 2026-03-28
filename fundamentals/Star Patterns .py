# Print different star patterns

n = int(input("Enter number of rows: "))

# Triangle
print("\nTriangle Pattern:")
for i in range(1, n + 1):
    print("*" * i)

# Inverted Triangle
print("\nInverted Triangle:")
for i in range(n, 0, -1):
    print("*" * i)

# Pyramid
print("\nPyramid Pattern:")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)