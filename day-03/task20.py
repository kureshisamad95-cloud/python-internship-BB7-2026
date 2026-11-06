default_settings = {
    "theme": "Light",
    "language": "English",
    "notifications": True,
    "font_size": 12
}

user_settings = {
    "theme": "Dark",
    "font_size": 16
}

final_settings = {**default_settings, **user_settings}

print("Default Settings:", default_settings)

print("User Settings:", user_settings)

print("Final Settings:", final_settings)