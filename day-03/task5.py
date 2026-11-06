students = [("Riya", 88), ("Aman", 95), ("Sara", 72)]

students_sorted = sorted(students, key=lambda x: x[1], reverse=True)

print(students_sorted)