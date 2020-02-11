def dead_or_alive(n, m, a):
    res = {}
    for i in range(n):
        for j in range(m):
            temp = 0
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj

                    if ai >= n:
                        ai -= n
                    if aj >= m:
                        aj -= m

                    if (-1 <= ai < n) and (-1 <= aj < m) and (a[ai][aj] == 'X'):
                        temp += 1

            if a[i][j] == 'X':
                temp -= 1
            res.update({str(i) + '_' + str(j): temp})

    for i in range(n):
        for j in range(m):
            if (a[i][j] == 'X' and res[str(i) + '_' + str(j)] == 2) or (
                    a[i][j] == 'X' and res[str(i) + '_' + str(j)] == 3):
                a[i][j] = 'X'
            elif a[i][j] == '.' and res[str(i) + '_' + str(j)] == 3:
                a[i][j] = 'X'
            else:
                a[i][j] = '.'

    return a


if __name__ == '__main__':
    h, w = (int(i) for i in input().split())
    field = []

    for i in range(h):
        f = [str(i) for i in input()]
        field.append(f)

    rrr = dead_or_alive(h, w, field)

    for i in rrr:
        for j in i:
            print(j, end='')
        print()
