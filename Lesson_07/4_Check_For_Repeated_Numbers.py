numbers_str = input("Enter the list of numbers (separated by space): ")
numbers_lst = numbers_str.split()
if len(numbers_lst) == len(set(numbers_lst)):
    print("All numbers are unique")
else:
    print("There are recurring numbers")
