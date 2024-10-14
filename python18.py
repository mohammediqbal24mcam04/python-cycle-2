
dict1_input = input("Enter first dictionary (key:value pairs separated by commas): ")
dict1 = dict(item.split(":") for item in dict1_input.split(",") if item)


dict2_input = input("Enter second dictionary (key:value pairs separated by commas): ")
dict2 = dict(item.split(":") for item in dict2_input.split(",") if item)


dict1 = {k: int(v) for k, v in dict1.items()}
dict2 = {k: int(v) for k, v in dict2.items()}


merged_dict = {**dict1, **dict2}

print("Merged Dictionary:", merged_dict)
