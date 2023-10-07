user_str = "hello 1 one two three 15 world"
user_lst = user_str.split(" ")
is_consecutive = False
for item in range(1, len(user_lst)-1):
    if user_lst[item-1].isalpha() and user_lst[item].isalpha() and user_lst[item+1].isalpha():
        is_consecutive = True

print(f"Are there three consecutive words in the string?: {is_consecutive}")
