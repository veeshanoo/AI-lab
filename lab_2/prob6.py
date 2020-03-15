try:
    with open("tst.in") as fin:
        matrix = list(map(lambda x: x[:-1].split(" "), fin.readlines()))
        print(matrix)
        check = set([len(x) for x in matrix])
        if len(check) > 1:
            raise ValueError
        anotherCheck = [1 if x.isnumeric() else 0 for y in matrix for x in y]
        print(sum([sum(map(int, line)) for line in matrix]))
except FileNotFoundError:
    print("file not found")
except ValueError:
    print("line lengths are not equal")
except Exception as exc:
    print(exc)
