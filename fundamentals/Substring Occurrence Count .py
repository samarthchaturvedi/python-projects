# Count occurrences of a substring in a string

text = input("Enter main string: ")
substring = input("Enter substring: ")

count = 0
n = len(text)
m = len(substring)

# Loop through the string and match substring
for i in range(n - m + 1):
    if text[i:i + m] == substring:
        count += 1

print("Occurrences:", count)