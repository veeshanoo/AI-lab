s = input()

print(s)
for i in range(len(s) - 1):
    print(s[i + 1:] + s[0:i + 1])

print("\n")
print(s)
for i in range(len(s) - 1, 0, -1):
    print(s[i:] + s[:i])

print("\n")
for i in range(len(s) // 2):
    print(s[:i + 1] + "|" + s[len(s) - i - 1:])