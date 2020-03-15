import random

l = [0] * 4
m = [list(l) for x in range(4)]

for i in range(4):
    for j in range(4):
        m[i][j] = random.randint(0, 16)

print(m)

diag1 = [m[i][i] for i in range(4)]
diag2 = [m[i][4 - i - 1] for i in range(4)]
border = [m[0][i] for i in range(4)] + [m[3][i] for i in range(4)] + [m[i][0] for i in range(1, 4)] + [m[i][3] for i in range(1, 4)]
sum_of_matrix = 0
for i in range(4):
    sum_of_matrix += sum(m[i])

d = {}
d[1] = diag1
d[2] = diag2
d[3] = border
d[4] = sum_of_matrix
d[5] = "exit"

while True:
    s = int(input())
    print(d[s])
    if s == 5:
        break


