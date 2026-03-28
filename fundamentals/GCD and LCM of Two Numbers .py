# Calculate GCD and LCM of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Store original values for LCM calculation
x, y = a, b

# Compute GCD using Euclidean Algorithm
while b != 0:
    temp = b
    b = a % b
    a = temp

gcd = a

# Compute LCM using formula: LCM = (x * y) // GCD
lcm = (x * y) // gcd if gcd != 0 else 0

print("GCD:", gcd)
print("LCM:", lcm)