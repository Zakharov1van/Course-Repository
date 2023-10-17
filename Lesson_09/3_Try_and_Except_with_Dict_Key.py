course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}
try:
    user_answer = input("Enter the key: ").lower()
    print(f"Your value: {course[user_answer]}")
except KeyError:
    print("You entered invalid key.")
