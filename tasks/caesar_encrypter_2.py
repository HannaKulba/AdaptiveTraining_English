import math

n = int(input())
string = input().strip()

alphabet = ''.join([chr(i) for i in range(int(0x1f600), int(0x1f64f)+1)])
d = {}
c = 0

for i in alphabet:
    d.setdefault(c, i)
    c += 1

print('Result: "', end='')
for s in string:
    for f in d:
        c = math.fabs((f + n) // len(d))

        if d[f] == s and f + n < 0:
            print(d[c * len(d) + f + n], end='')
        elif d[f] == s and f + n == 0:
            print(d[f + n], end='')
        elif d[f] == s and f + n > 0:
            if f + n < len(d):
                print(d[f + n], end='')
            elif f + n >= len(d):
                print(d[f + n - c * len(d)], end='')
print('"')