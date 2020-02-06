N = int(input())
M = int(input())
X = int(input())
Y = int(input())

x1, x2, y1, y2 = 0, 0, 0, 0


def get_coordinates(side, param):
    if side - param > param:
        res_1 = abs(side - param)
        res_2 = param
    else:
        res_1 = param
        res_2 = abs(side - param)
    return res_1, res_2


if N > M:
    x1 = get_coordinates(M, X)[0]
    x2 = get_coordinates(M, X)[1]
    y1 = get_coordinates(N, Y)[0]
    y2 = get_coordinates(N, Y)[1]
else:
    x1 = get_coordinates(N, X)[0]
    x2 = get_coordinates(N, X)[1]
    y1 = get_coordinates(M, Y)[0]
    y2 = get_coordinates(M, Y)[1]

r = min(x1, x2, y1, y2)
print(r)
