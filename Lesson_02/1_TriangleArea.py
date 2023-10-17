k1 = input("Enter the length of the first сathetus: ")
k2 = input("Enter the length of the second сathetus: ")
try:
    area = 0.5*float(k1)*float(k2)
    print("Area of the right-angled triangle is", area)
except ValueError:
    print("You need to enter valid numbers")
