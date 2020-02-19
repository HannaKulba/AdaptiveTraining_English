M_N = [int(i) for i in input().split()]
N = M_N[1]
array = [int(i) for i in input().split()]

for n in range(1, N + 1):
    print(str(array.count(n)), end=' ')
