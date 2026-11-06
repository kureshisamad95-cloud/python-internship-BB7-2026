students = [
    {"name": "Riya", "marks": 88},
    {"name": "rizvan", "marks": 95},
    {"name": "Sara", "marks": 72},
    {"name": "Arjun", "marks": 91}
]

topper = students[0]

for student in students:

    if student["marks"] > topper["marks"]:
        topper = student

print("Topper Name:", topper["name"])
print("Highest Marks:", topper["marks"])