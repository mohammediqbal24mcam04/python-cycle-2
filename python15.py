words = input("Enter a list of words (comma-separated): ").split(',')
longest_word = max(words, key=len)
print(len(longest_word))
