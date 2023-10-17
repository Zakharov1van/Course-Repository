n = input("Enter the number of students: ")
k = input("Enter the number of apples: ")
try:
    taken_apples = int(k) // int(n)
    remaining_apples = int(k) % int(n)
    print("Each student took", taken_apples, "apples")
    print(remaining_apples, "apples are left")
except ValueError:
    print("You need to enter valid numbers")