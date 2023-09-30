user_lst = [1, 2, 3, 4, 5, 6, 8]
number = 1
while number < len(user_lst):
    if user_lst[number] != user_lst[number - 1] + 1:
        print(f"First nonconsecutive number is {user_lst[number]}")
        break
    number += 1

if number == len(user_lst):
    print("All numbers in the list are consecutive")
