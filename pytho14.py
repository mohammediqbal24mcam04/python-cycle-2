string = input("Enter a string: ")
if string.endswith('ing'):
    string += 'ly'
else:
    string += 'ing'
print(string)
