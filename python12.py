numbers = list(map(int, input("Enter a list of integers (comma-separated): ").split(',')))
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)
