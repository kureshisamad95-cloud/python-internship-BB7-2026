from functools import reduce

numbers = [10, 45, 20, 80, 30, 60]

largest = reduce(lambda a, b: a if a > b else b, numbers)

print("Largest Number:", largest)