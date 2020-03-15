lst = list()
with open("tst.in", "r") as fin:
    for line in fin.readlines():
        (idx, name) = tuple(line[:-1].split(":"))
        idx = int(idx)
        if idx > len(lst):
            lst = lst + (["none"] * (idx - len(lst) - 1))
            lst.append(name)
        else:
            lst[idx] = name


print(lst)