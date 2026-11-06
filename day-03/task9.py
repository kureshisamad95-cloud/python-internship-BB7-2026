def student_marks(marks):

    lowest = min(marks)
    highest = max(marks)
    average = sum(marks) / len(marks)

    return (lowest, highest, average)


marks = [85, 90, 72, 65, 95, 88]

result = student_marks(marks)

lowest, highest, average = result

print("Lowest Marks:", lowest)
print("Highest Marks:", highest)
print("Average Marks:", average)