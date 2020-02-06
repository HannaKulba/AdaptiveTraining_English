n = int(input())


def f(x):
    res = 1
    if x % 2 == 0:
        for i in range(1, x + 1):
            if i % 2 == 0:
                res *= i
    else:
        for i in range(x + 1):
            if i % 2 == 1:
                res *= i
    return res


print(f(n))
