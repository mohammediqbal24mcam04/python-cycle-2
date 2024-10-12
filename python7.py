text = input("Enter a line of text: ")
words = text.split()
word_count = {word: words.count(word) for word in words}
print(word_count)
