usernames = ["Ali", "samad", "Ahmed", "John", "kureshi"]

result = list(filter(lambda name: len(name) >= 6, usernames))

print("Valid Usernames:", result)