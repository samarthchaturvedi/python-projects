# Power using fast exponentiation

def power(a, b):
    if b == 0:
        return 1
    
    half = power(a, b//2)
    
    if b % 2 == 0:
        return half * half
    else:
        return a * half * half

a = int(input("Enter base: "))
b = int(input("Enter exponent: "))

print("Result:", power(a, b))