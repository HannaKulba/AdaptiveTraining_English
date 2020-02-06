a, b, c, d = int(input()), int(input()), int(input()), int(input())


def min(a, b):
    if a < b:
        return a
    else:
        return b


def min4(a, b, c, d):
    res1 = min(a, b)
    res2 = min(c, d)
    if res1 > res2:
        return res2
    else:
        return res1


print(min4(a, b, c, d))
