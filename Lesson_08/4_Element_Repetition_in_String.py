result_link = "https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s"

result_dict = {}
for char in result_link:
    result_dict[char] = result_link.count(char)

print(f"Here is the resulting dictionary:\n{result_dict}")
