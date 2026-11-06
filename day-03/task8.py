tasks = []

# Add 5 tasks
tasks.append("Study Python")
tasks.append("Practice HTML")
tasks.append("Learn CSS")
tasks.append("Complete Assignment")
tasks.append("Exercise")

print("Current Tasks:")
print(tasks)

# Remove 2 tasks
tasks.remove("Practice HTML")
tasks.remove("Exercise")

print("\nUpdated To-Do List:")

for task in tasks:
    print("-", task)