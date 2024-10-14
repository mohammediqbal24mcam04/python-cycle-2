n = int(input("Enter the number of items in the dictionary: "))
dictionary = {}
for _ in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dictionary[key] = value

ascending = dict(sorted(dictionary.items()))
descending = dict(sorted(dictionary.items(), reverse=True))

print("Ascending:", ascending)
print("Descending:", descending)
