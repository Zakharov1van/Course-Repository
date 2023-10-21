def arithmetic(num_1, num_2, operation):
    if operation == "+":
        return num_1 + num_2
    elif operation == "-":
        return num_1 - num_2
    elif operation == "*":
        return num_1 * num_2
    elif operation == "/":
        if num_2 == 0:
            return "Division by 0 can't be done."
        else:
            return num_1 / num_2
    else:
        return f"Not known operation: {operation}"


user_num_1 = float(input("Enter 1st number: "))
user_num_2 = float(input("Enter 2nd number: "))
user_operation = input("Enter the arithmetic operation: ")

print(arithmetic(user_num_1, user_num_2, user_operation))
