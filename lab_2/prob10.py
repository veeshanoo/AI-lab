def fn1(k):
    return {i: [x for x in range(1, i + 1)] for i in range(1, k, 2)}


def fn2(target):
    return {c: [word for word in target if c in word] for c in set("".join(target))}


def fn3(target):
    return {key: [x for x in range(key[0], key[1], int((-1) ** (key[0] > key[1])))] for key in target}


print(fn1(10))
target = ["asd", "ds", "2d", "d", "lit"]
print(fn2(target))
target = [(2, 6), (5, 10), (3, 1)]
print(fn3(target))
