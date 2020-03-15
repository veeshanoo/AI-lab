inp = ["co-pa-cel", "pa-pu-cel", "a-bac", "021-220-20-10", "1-pi-tic", "go-go-nea", "tip-til", "123-456", "a-co-lo", "lo-go-ped", "pa-pa-gal", "co-co-starc"]

d = {}
d["vocale"] = "aeiou"
d["consoane"] = "bcdfghjklmnpqrstvxyz"
d["cifre"] = "0123456789"

for i in d.items():
    print(i)

d2 = {}
for i in d["vocale"] + d["consoane"] + d["cifre"]:
    lst = [x for x in inp if i in x]
    d2[i] = lst

for i in d2:
    print(i, d2[i])


for i in d["cifre"]:
    if i in d2:
        print(i, " : ", d2[i])
        del d2[i]

print(len(d2))

for cuv in inp:
    lst = cuv.split("-")
    for v in lst:
        if len(v) != 3:
            continue

        if v[0] in d["consoane"] and v[1] in d["vocale"] and v[2] in d["consoane"]:
            print(v)
