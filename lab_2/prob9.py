def fn1(n):
    return [[x] * n for x in range(0, n)]


def fn2(mat):
    return [[x for idx, x in enumerate(line) if (idx + 1) % 2 == 1] for line in mat]


def fn3(mat, mat2):
    return [[mat[i][j] if mat2[i][j] else 0 for j in range(0, len(mat[i]))] for i in range(0, len(mat))]


def fn4(n, element):
    return [[element if i == n - j - 1 else 0 for j in range(0, n)] for i in range(0, n)]


def fn5(lst1, lst2):
    return [[el1 if el1 > el2 else el2 for el1 in lst1] for el2 in lst2 ]


if __name__ == '__main__':
    print(fn1(5))
    print(fn2([[1, 0, 1], [1, 0, 1], [1, 0, 1]]))
    print(fn3([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 0, 1], [0, 1, 0], [1, 0, 1]]))
    print(fn4(4, 2))
    print(fn5([1, 2, 3], [1, 2]))