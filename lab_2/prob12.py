lines = []

with open("tst.in", "r+") as fin:
    for line in fin.readlines():
        ans = eval(line[:-1])
        lines.append(line[:-1] + "=" + str(ans))


with open("tst.in", "r+") as fin:
    for line in lines:
        fin.write(line + "\n")




