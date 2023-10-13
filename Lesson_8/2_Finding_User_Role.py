roles = {'admin': ["John", "Peter"],
         'maintainer': ["Mary", "Katie"],
         'manager': ["Steve", "Jenny"],
         'developer': ["Bruce", "Lily"]
         }

user_name = input("Enter the name: ").title()
user_role = "Guest"
for item in roles:
    if user_name in roles[item]:
        user_role = item

print(f"Hello, {user_role}")
