# Check whether a string is a palindrome

text = input("Enter a string: ")

cleaned_text = text.replace(" ", "").lower()

reversed_text = cleaned_text[::-1]

if cleaned_text == reversed_text:
    print("Palindrome string")
else:
    print("Not a palindrome string")