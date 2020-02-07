import math


def print_roots(a, b, c):
    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(x1, x2) if x1 < x2 else print(x2, x1)
    elif D == 0:
        x1 = (-b) / (2 * a)
        print(x1)
    else:
        print()


if __name__ == '__main__':
    a, b, c = float(input()), float(input()), float(input())
    print_roots(a, b, c)
