try:
    user_number = int(input("Enter your number: "))
except ValueError:
    print("You need to enter a valid integer number")
    quit()

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if user_number == 0:
    print("You can't enter 0")
else:
    idx = 0
    for number in number_list:
        if number % user_number == 0:
            print(number)
            idx += 1

    if idx == 0:
        print("There are no such numbers")
