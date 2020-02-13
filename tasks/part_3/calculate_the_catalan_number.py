def factorial(number):
    res = 1
    while number >= 1:
        res *= number
        number -= 1
    return res


if __name__ == '__main__':
    n = int(input())
    m = 1000000007
    C_n = (factorial(n * 2) // (factorial(n + 1) * factorial(n))) % m
    print(C_n)
