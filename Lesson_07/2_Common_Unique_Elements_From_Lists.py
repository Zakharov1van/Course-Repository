a_lst = [1, 1, 2, 3, 5, 8, 10, 13, 21, 34, 55, 89]
b_lst = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13]

result_lst = list(set(a_lst).intersection(set(b_lst)))
print(f"Resulting list: {result_lst}")
