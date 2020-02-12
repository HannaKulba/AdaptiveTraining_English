import math


def IsPointInCircle(x, y, xc, yc, r):
    h = math.sqrt((x - xc) ** 2 + (y - yc) ** 2)
    if h <= r:
        return True
    return False


if __name__ == '__main__':
    x, y, xc, yc, r = float(input()), float(input()), float(input()), float(input()), float(input())
    if IsPointInCircle(x, y, xc, yc, r):
        print('YES')
    else:
        print('NO')
