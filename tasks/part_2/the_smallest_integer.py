arr = [int(i) for i in input().split()]


def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


print(lcm(arr[0], arr[1]))
