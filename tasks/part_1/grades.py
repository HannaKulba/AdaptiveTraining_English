n = int(input())
a = 0
b = 0
c = 0
d = 0

for i in range(n):
    mark = int(input())
    if mark == 2:
        d += 1
    elif mark == 3:
        c += 1
    elif mark == 4:
        b += 1
    elif mark == 5:
        a += 1

print(d, c, b, a)
