employees = {
    "Aman": 25000,
    "Riya": 45000,
    "Sara": 35000,
    "Arjun": 60000,
    "Rahul": 55000
}

sorted_employees = sorted(
    employees.items(),
    key=lambda x: x[1],
    reverse=True
)

print("Top 3 Highest Paid Employees:")

for name, salary in sorted_employees[:3]:

    print(name, ":", salary)