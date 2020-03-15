import sys


def add(*args):
    l = []
    for el in args:
        try:
            l.append(int(el))
        except:
            e = sys.exc_info()[0]
            print(e)
            return

    ret = 0
    for el in l:
        ret += el

    return ret


lst = sys.argv[1:]
print(add(*lst))

