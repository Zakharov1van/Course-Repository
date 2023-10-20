def is_prime(number):
    flag = True
    for num in range(2, number):
        if number % num == 0:
            flag = False
            break
    return flag


user_number = int(input("Enter your number: "))
if user_number < 2 or user_number > 1000:
    print("Your number must be between 2 and 1000")
else:
    print(f"Is {user_number} a prime number?: {is_prime(user_number)}")
