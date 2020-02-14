a = float(input())
n = int(input())

if a % 2 == 0:
    a = (a ** 2) ** (n / 2)
else:
    a = a * a ** (n - 1)
print(a)