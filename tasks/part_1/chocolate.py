n = int(input())
m = int(input())
k = int(input())

square = n * m

if square <= k:
    print('NO')
elif k < n or k < m:
    print('NO')
elif n % k == 0 or m % k == 0 or k % n == 0 or k % m == 0:
    print('YES')
else:
    print('NO')
