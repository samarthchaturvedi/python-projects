# Count number of words in a sentence

sentence = input("Enter a sentence: ").strip()

# Split sentence into words based on spaces
words = sentence.split()

print("Number of words:", len(words))