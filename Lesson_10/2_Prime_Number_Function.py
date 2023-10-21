def is_prime(number):
    if number < 2 or number > 1000:
        raise ValueError("Your number must be between 2 and 1000")
    else:
        flag = True
        for num in range(2, number):
            if number % num == 0:
                flag = False
                break
        return flag


user_number = int(input("Enter your number: "))
print(f"Is {user_number} a prime number?: {is_prime(user_number)}")
