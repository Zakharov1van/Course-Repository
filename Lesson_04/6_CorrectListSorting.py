user_lst1 = ['aBc', 'Hello', 'neW', 'TEST', 'Tst']
user_lst2 = ['Tst', 'aBc', 'TEST', 'Hello', 'neW']

sort_lst1 = sorted(user_lst1, key=str.lower)
sort_lst2 = sorted(user_lst2, key=str.lower)


print(f"Is the first string sorted?: {user_lst1 == sort_lst1}\nIs the second string sorted?: {user_lst2 == sort_lst2}")
