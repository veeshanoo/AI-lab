def check_all_equal(s):
    return any({x - s[0] for x in s}) is False


def check_all_alphabet(s):
    return len({x.lower() for x in s}) == 26


def check_anagram(a, b):
    return sorted(a) == sorted(b)


def cartesian_product(a, b):
    return [[x, y] for x in a for y in b]


def power_set(s):
    ans = []
    for x in range(0, 1 << len(s)):
        binstr = str(bin(x))
        ans.append([s[i - 2] for i in range(2, len(binstr)) if binstr[i] == '1'])

    return ans


print(check_all_equal([1, 1, 1]))
print(check_all_alphabet("aabcdefghijklmnopqrstuvwxyz"))
print(check_anagram("asd", "dsa"))
print(cartesian_product([2, 3, 4], [1, 2]))
print(power_set([1, 2]))
