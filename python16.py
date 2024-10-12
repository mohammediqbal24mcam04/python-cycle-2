numbers = [1, -2, 3, -4, 5]
positive_numbers = [num for num in numbers if num > 0]
squares = [num ** 2 for num in numbers]
word = "hello"
vowels = [char for char in word if char in 'aeiou']
ordinal_values = [ord(char) for char in word]
print(positive_numbers, squares, vowels, ordinal_values)
