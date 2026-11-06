numbers = [12, 45, 23, 12, 75, 34, 54, 65, 45, 55, 87, 89, 45, 10, 10, 54, 75, 12]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
        
        print("Original numbers:", numbers)
        print("list after removing duplicates:", unique_numbers)