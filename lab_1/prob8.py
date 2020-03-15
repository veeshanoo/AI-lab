import re


lst = ["margareta", "crizantema", "lalea", " zorea , violeta, orhidee", "trandafir", "gerbera , iasomie", "iris", "crin "]


def remove_and_append(cuv):
    if cuv in lst:
        lst.remove(cuv)
        lst.append(cuv)
    else:
        lst.append(cuv)


cpy = lst.copy()
for el in cpy:
    lst.remove(el)
    el = el.strip()
    g = re.split('\,', el)
    # print(g)
    for cuv in g:
        remove_and_append(cuv.strip())

print(lst)


def create_new_list(c):
    return [cuv for cuv in lst if c in cuv]


print(create_new_list("z"))
print(sorted(lst, key=lambda x: x, reverse=True))

