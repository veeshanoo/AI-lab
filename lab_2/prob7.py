def fn1(lst):
    return all([1 if int(x) == x and x > 0 else 0 for x in lst])


def fn2(lst):
    return any([s[0] == s[len(s) - 1] for s in lst])


def fn3(mat):
    return all([x == 0 for line in mat for x in line])


def fn4(sir, lst):
    return any([cuv in sir for cuv in lst])