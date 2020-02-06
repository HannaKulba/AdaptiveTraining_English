arr = [int(i) for i in input().split()]

x1, y1, x2, y2 = arr[0], arr[1], arr[2], arr[3]

if (x1 + 2 == x2 and y1 + 1 == y2) \
        or (x1 + 2 == x2 and y1 - 1 == y2) \
        or (x1 - 2 == x2 and y1 - 1 == y2) \
        or (x1 - 2 == x2 and y1 + 1 == y2) \
        or (x1 + 1 == x2 and y1 + 2 == y2) \
        or (x1 + 1 == x2 and y1 - 2 == y2) \
        or (x1 - 1 == x2 and y1 - 2 == y2) \
        or (x1 - 1 == x2 and y1 + 2 == y2):
    print('YES')
else:
    print('NO')

