from collections import namedtuple

person = namedtuple("person", ["name", "age", "avg_score", "is_failing"])
john = person("John", 20, 2.4, True)
ed = person("Ed", 22, 5, False)
lily = person("Lily", 20, 3.3, False)
mary = person("Mary", 21, 4.6, False)

class_lst = [john, ed, lily, mary]
expected_types = ["<class 'str'>", "<class 'int'>", "<class 'float'>", "<class 'bool'>"]
value_lst = []

for names in class_lst:
    for idx in range(len(names)):
        if str(type(names[idx])) != expected_types[idx]:
            data = f"Warning! Invalid data type. Expected {expected_types[idx]}, Actual {type(names[idx])}"
        else:
            data = names[idx]
        value_lst.append(data)

print(f"Here is a list of values in tuples: {value_lst}")
