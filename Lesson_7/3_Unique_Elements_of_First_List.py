first_lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

first_set = set(first_lst)
second_set = set(second_lst)
result_lst = []
for i in first_set.difference(second_set):
    result_lst.append(str(i))
print(f"Elements that exist only in 1st list: {', '.join(result_lst)}")
