# Password Generator with Strength Checker
# Author: Samarth Chaturvedi
# Description:
# This tool generates random passwords and evaluates their strength
# based on length, uppercase, lowercase, digits, and special characters.

import random
import string

def generate_password(length):
    """Generate a random password of given length"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_strength(password):
    """Evaluate password strength"""
    length = len(password)

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = 0

    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1

    # Strength levels
    if score <= 2:
        return "Weak ❌"
    elif score <= 4:
        return "Medium ⚠️"
    else:
        return "Strong ✅"

def main():
    print("\n🔐 Password Generator & Strength Checker\n")

    length = int(input("Enter desired password length: "))

    password = generate_password(length)

    print("\nGenerated Password:")
    print(password)

    strength = check_strength(password)

    print("\nPassword Strength:")
    print(strength)


if __name__ == "__main__":
    main()