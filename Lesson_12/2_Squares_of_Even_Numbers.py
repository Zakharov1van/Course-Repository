def squares_of_evens():
    for number in range(0, 1000000001):
        if number % 2 == 0:
            yield number ** 2


result = squares_of_evens()
print(next(result))
