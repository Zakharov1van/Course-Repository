user_str = "hello 1 one two three 15 world"
user_lst = user_str.split()
is_consecutive = False
for item in range(1, len(user_lst)-1):
    if user_lst[item-1].isalpha() and user_lst[item].isalpha() and user_lst[item+1].isalpha():
        is_consecutive = True

# words = 0
# for item in user_lst:
#     if words == 3:
#         is_consecutive = True
#     if item.isalpha():
#         words += 1
#     else:
#         words = 0
print(f"Are there three consecutive words in the string?: {is_consecutive}")
