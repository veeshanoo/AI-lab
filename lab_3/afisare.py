special_char = " "
column_dimension = 10


class NotValidList(Exception):
    pass


class NotValidTuples(Exception):
    pass


def print_on_two_columns(lst):
    try:
        if type(lst) is not list:
            raise NotValidList
    except Exception as error:
        print(error)
        return

    for el in lst:
        try:
            if type(el) is not tuple:
                raise Exception("list contains elements other than tuples")
            if len(el) != 2:
                raise Exception("not a valid list of tuples")
        except Exception as error:
            print(error)
            return

    element = special_char * column_dimension
    line = 2 * [element]
    mat = [list(line) for x in lst]
    sz = len(lst)

    for i in range(0, sz):
        el = lst[i]
        fi = el[0]
        se = el[1]

        try:
            if len(fi) > column_dimension or len(se) > column_dimension:
                raise Exception("invalid tuple element length")
        except Exception as error:
            print(error)
            return

        rem = column_dimension - len(fi)
        mat[i][0] = fi + rem * special_char
        rem = column_dimension - len(se)
        mat[i][1] = se + rem * special_char

    for line in mat:
        for el in line:
            print(el, end="")
        print()


def print_on_three_columns(lst):
    try:
        if type(lst) is not list:
            raise Exception("input is not list")
    except Exception as error:
        print(error)
        return

    for el in lst:
        try:
            if type(el) is not tuple:
                raise Exception("list contains elements other than tuples")
            if len(el) != 3:
                raise Exception("not a valid list of tuples")
        except Exception as error:
            print(error)
            return

    element = special_char * column_dimension
    line = 3 * [element]
    mat = [list(line) for x in lst]
    sz = len(lst)

    for i in range(0, sz):
        el = lst[i]
        fi = el[0]
        se = el[1]
        th = el[2]

        try:
            if len(fi) > column_dimension or len(se) > column_dimension or len(th) > column_dimension:
                raise Exception("invalid tuple element length")
        except Exception as error:
            print(error)
            return

        # mat[i] = [((column_dimension - len(el)) // 2) * special_char + x + (column_dimension - len(el) - (column_dimension - len(el)) // 2) * special_char for x in el]

        rem = column_dimension - len(fi)
        pe2 = rem // 2
        mat[i][0] = pe2 * special_char + fi + (rem - pe2) * special_char

        rem = column_dimension - len(se)
        pe2 = rem // 2
        mat[i][1] = pe2 * special_char + se + (rem - pe2) * special_char

        rem = column_dimension - len(th)
        pe2 = rem // 2
        mat[i][2] = pe2 * special_char + th + (rem - pe2) * special_char

    for line in mat:
        for el in line:
            print(el, end="|")
        print()
