a = [1, 2, 32, 23, 111]
a.sort(key=lambda x: str(x))
print(a)

a.sort(key=lambda x: str(x)[::-1])
print(a)

a.sort(key=lambda x: len(str(x)))
print(a)

a.sort(key=lambda x: len({x for x in str(x)}))
print(a)

p = ["1+2+3", "2-5", "3+4", "5*10"]
p.sort(key=lambda x: eval(x))
print(p)

