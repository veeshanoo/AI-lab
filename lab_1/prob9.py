lst = ["papagal", "pisica", "soarece", "bolovan", "soparla", "catel", "pasare"]

N = 26


def gen_matrice():
    ans = [0] * N
    ans = [list(ans) for i in range(0, N)]

    ans[0] = [chr(i + ord('a')) for i in range(0, N)]
    for i in range(0, N):
        ans[i][0] = chr(i + ord('a'))

    return ans


mat = gen_matrice()
for line in mat:
    print(line)


def count(word):
    ans = 0
    for cuv in lst:
        for i in range(0, len(cuv) - 1):
            if cuv[i] + cuv[i + 1] == word:
                ans += 1

    return ans


def completeaza_matrice(a, b):
    for i in range(1, N):
        for j in range(1, N):
            s = a[0][j - 1] + a[i - 1][0]
            print(s)
            cnt = count(s)
            # print(str(i) + " " + str(j) + " " + str(cnt))
            a[i][j] = cnt


completeaza_matrice(mat, lst)
for line in mat:
    print(line)


def remove_lines_and_columns(a):
    for line in a:
        if line[1:] == [0] * (N - 1):
            a.remove(line)

    col_id = 1
    while col_id < len(a[0]):
        line = [a[x][col_id] for x in range(1, len(a))]
        print(line)
        print(len(a))
        if line == [0] * (len(a) - 1):
            for row_id in range(0, len(a)):
                mat[row_id] = mat[row_id][:col_id] + mat[row_id][col_id + 1:]
            col_id -= 1
        col_id += 1


remove_lines_and_columns(mat)
print()
for line in mat:
    print(line)


print([mat[i][0] + mat[0][j] for i in range(1, len(mat)) for j in range(1, len(mat[0])) if True if mat[i][j] > 2])