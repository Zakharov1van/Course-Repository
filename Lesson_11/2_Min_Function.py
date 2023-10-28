def user_min(items, *args):
    if len(args) > 0:
        new_lst = [items]
        for data in args:
            new_lst.append(data)
    else:
        new_lst = list(items)
    result_lst = sorted(new_lst)
    return result_lst[0]


# Data for testing
my_dict = {"eleven": 11, "twenty two": 22, "thirty three": 33, "forty four": 44}
my_tuple = (11, 2, 8, -4, 105, 66)
my_str = "homework11"
my_set = {11, 2, 8, -4, 105, 66}
my_lst = [11, 2, 8, -4, 105, 66]

# Testing with different data
print(user_min(my_dict))
print(user_min(my_tuple))
print(user_min(my_str))
print(user_min(my_set))
print(user_min(my_lst))
print(user_min(11, 2, 8, -4, 105, 66))
