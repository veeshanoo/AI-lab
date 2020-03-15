def calc(a, b, c):
    x = b | c
    y = a - c
    return [x, y]


def calc2(a, b, c):
    x = b | a
    y = c | a
    return [x, y]


print(calc({1, 2, 3, 4}, {2, 3}, {1, 4}))
print(calc2({2, 3}, {1}, {4}))
