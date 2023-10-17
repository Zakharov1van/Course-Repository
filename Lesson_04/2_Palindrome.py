user_string = input("Enter your string: ")
# We can use (input("Enter your string: ")).lower or (input("Enter your string: ")).upper if
# we don't want to take into consideration the difference between lowercase and uppercase letters

print(f"Is your string a palindrome: {user_string == user_string[::-1]}")
