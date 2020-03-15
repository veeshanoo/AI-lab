def fn1(lst):
    return {x for x in lst if str(x)[0] == str(x)[-1]}


def fn2(mat):
    return {mat[i][j] for i in range(0, len(mat)) for j in range(0, len(mat[i])) if i == j}


print(fn1([1,2, 3, 33, 13]))
print(fn2([[1, 0, 0], [0, 2, 0], [0, 0, 3]]))
