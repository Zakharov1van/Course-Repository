params = {'v': 'some_id', 'list': 'some_list', 'index': '6', 't': '0s'}
initial_str = 'https://www.youtube.com/watch?'
params_lst = []

for item in params:
    params_lst.append(f"{item}={params[item]}")

result_link = initial_str + "&".join(params_lst)
print(f"result_link = '{result_link}'")
