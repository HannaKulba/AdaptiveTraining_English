array = [int(i) for i in input().split()]


def calc_expr(a, b, c):
    res = (a + b * c) / 5 - a ** 3 + (a + (c / 3)) / 4
    return res


print(calc_expr(array[0], array[1], array[2]))
