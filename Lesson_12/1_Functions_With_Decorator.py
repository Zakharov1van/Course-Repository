def name_of_func(func):
    def wrapper(items, *args):
        print(f"Name of the function is '{func.__name__}'.")
        result = func(items, *args)
        return result
    return wrapper


@name_of_func
def user_max(items, *args):
    if len(args) > 0:
        new_lst = [items]
        for data in args:
            new_lst.append(data)
    else:
        new_lst = list(items)
    result_lst = sorted(new_lst)
    return result_lst[-1]


@name_of_func
def user_min(items, *args):
    if len(args) > 0:
        new_lst = [items]
        for data in args:
            new_lst.append(data)
    else:
        new_lst = list(items)
    result_lst = sorted(new_lst)
    return result_lst[0]


my_lst = [11, 2, 8, -4, 105, 66]
print(user_max(my_lst))
print(user_min(my_lst))
