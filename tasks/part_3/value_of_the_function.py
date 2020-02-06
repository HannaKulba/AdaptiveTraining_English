def f(x):
    res = 0
    if x <= -2:
        res = 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        res = -(x / 2)
    else:
        res = (x - 2) ** 2 + 1
    return res


if __name__ == '__main__':
    print(f(4.5))
