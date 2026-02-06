# Word and Character Counter

text = input("Enter a text: ")

# Number of characters (with spaces)
characters_with_spaces = len(text)

# Number of words
words = text.split()
word_count = len(words)

# Number of characters (without spaces)
characters_without_spaces = len(text.replace(" ", ""))

print("Number of words:", word_count)
print("Number of characters (with spaces):", characters_with_spaces)
print("Number of characters (without spaces):", characters_without_spaces)
