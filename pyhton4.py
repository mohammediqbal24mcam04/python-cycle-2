numbers = input("Enter a list of integers (comma-separated): ").split(',')
result = ['over' if int(num) > 100 else num for num in numbers]
print(result)
