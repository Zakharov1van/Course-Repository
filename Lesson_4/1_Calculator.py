try:
    first_number = float(input("Enter your first number: "))
    second_number = float(input("Enter your second number: "))
except ValueError:
    print("You need to enter valid numbers")
    quit()

operation = input("Type '+' for adding, '-' for subtracting, '*' for multiplying or '/' for dividing: ")

if operation != "+" and operation != "-" and operation != "*" and operation != "/":
    print("You chose wrong operation")
else:
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    else:
        result = first_number / second_number
    print(f"Result of calculation is {result}")
