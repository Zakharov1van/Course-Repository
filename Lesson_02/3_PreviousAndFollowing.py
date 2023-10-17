number = input("Enter your number: ")
try:
    print("Previous number is", int(float(number)) - 1)
    print("Following number is", int(float(number)) + 1)
except ValueError:
    print("You need to enter valid number")