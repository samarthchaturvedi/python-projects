# Password Generator

import random
import string

length = int(input("Enter password length: "))

chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for _ in range(length))

print("Password:", password)

# Strength check
if length < 6:
    print("Weak")
elif length < 10:
    print("Medium")
else:
    print("Strong")