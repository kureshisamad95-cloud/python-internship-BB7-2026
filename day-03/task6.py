numbers = [10, 25, 45, 30, 60, 50]

largest = numbers[0]
second_largest = numbers[0]

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Largest number:", largest)
print("Second largest number:", second_largest)