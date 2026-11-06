def convert_to_frozenset(my_list):

    return frozenset(my_list)


numbers = [10, 20, 30, 40, 20, 10]

result = convert_to_frozenset(numbers)

print("Original List:", numbers)

print("Frozenset:", result)

print("Type:", type(result))