count = 0


def f(string, aa, bb):
    global count
    if string.__contains__(bb) and bb.__contains__(aa):
        return 'Impossible'
    elif string.count(aa) > 0:
        string = string.replace(aa, bb)
        count += 1
        return f(string, aa, bb)


def get_result(s, a, b):
    r = f(s, a, b)
    if r == 'Impossible':
        print('Impossible')
    else:
        print(count)


if __name__ == '__main__':
    s, a, b = input(), input(), input()
    get_result(s, a, b)
