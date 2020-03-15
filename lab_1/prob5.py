l = list(map(str, input().split(" ")))

d = {}
for cuv in l:
    d[cuv] = 0

for cuv in l:
    d[cuv.lower()] += 1

for cuv in l:
    print(cuv + ": ", d[cuv.lower()])