import numpy


def deposit(p, x, y):
    cents = y / 100
    start_money = x + cents
    procent = (start_money * p) / 100
    end_year_money = start_money + procent + cents
    print(str(end_year_money).split('.')[0])
    print(numpy.around(int(str(end_year_money).split('.')[1]), decimals=2))


if __name__ == '__main__':
    P = int(input())
    X = int(input())
    Y = int(input())
    deposit(P, X, Y)
