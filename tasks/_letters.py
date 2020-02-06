s = input()
a = input()
b = input()

if s.__contains__(b) and b.__contains__(a):
    print('Impossible')
else:
    count = 0


    def f(string, aa, bb):
        global count
        if string.count(aa) > 0:
            string = string.replace(aa, bb)
            count += 1
            return f(string, aa, bb)


    try:
        f(s, a, b)
    except RecursionError:
        pass
    print(count)
