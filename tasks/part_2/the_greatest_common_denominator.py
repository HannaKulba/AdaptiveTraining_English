array = [int(i) for i in input().split()]
a = array[0]
b = array[1]

while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a

gcd = a + b
print(gcd)
