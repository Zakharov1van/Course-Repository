from math import sqrt


def add(a, b):
    if isinstance(a, (int, float, complex)) and isinstance(b, (int, float, complex)):
        return a + b
    else:
        return "Arguments should be numeric."


def subtract(a, b):
    try:
        return a - b
    except TypeError:
        return "Arguments should be numeric."


def multiply(a, b):
    try:
        return a * b
    except TypeError:
        return "Arguments should be numeric."


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Can't divide by 0."
    except TypeError:
        return "Arguments should be numeric."


def square_root(a):
    try:
        return sqrt(a)
    except ValueError:
        return "Can't take square root of a negative number"
    except TypeError:
        return "Argument should be numeric."
