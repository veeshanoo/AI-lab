print([x for x in range(0, 10) if x % 2 == 1])
print([chr(x) for x in range(ord('a'), ord('z') + 1)])

# 3
def fn(n):
    return [x * (-1) ** (x + 1) for x in range(1, n + 1)]


print(fn(5))


# 4
def fnx(s):
    return [x for x in s if x % 2 == 1]


print(fnx([1, 2, 3, 4]))


# 5
def fn2(s):
    return s[::2]


print(fn2([2, 3, 4, 1, 7, 4]))



def fn3(s):
    return [s[x] for x in range(0, len(s)) if x % 2 == s[x] % 2]


print(fn3([2, 4, 3, 1, 1, 5]))


def fn4(s):
    return [(s[x], s[x + 1]) for x in range(0, len(s) - 1)]


print(fn4([2, 3, 1, 4, 5, 6]))


def fn5(n):
    return [["{}*{}={}".format(x, y, x * y) for y in range(1, n + 1)] for x in range(1, n + 1)]


print(fn5(3))


def fn6(s):
    return [s[x:] + s[0:x] for x in range(0, len(s))]


print(fn6("abcde"))


def fn7(n):
    return [[i for x in range(0, i)] for i in range(0, n)]


print(fn7(4))
