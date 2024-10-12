dictionary = {'a': 3, 'b': 1, 'c': 2}
ascending = dict(sorted(dictionary.items()))
descending = dict(sorted(dictionary.items(), reverse=True))
print(ascending, descending)
