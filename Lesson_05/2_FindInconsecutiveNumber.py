user_lst = [1, 2, 3, 3, 5, 6, 7]
number = 1
while number < len(user_lst):
    if user_lst[number] != user_lst[number - 1] + 1:
        print(f"First nonconsecutive number is {user_lst[number]}")
        break
    number += 1
else:
    print("All numbers in the list are consecutive")
