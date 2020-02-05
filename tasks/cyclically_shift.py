n = int(input())
arr = [int(i) for i in input().split()]

for i in range(n):
    t = arr[n - 1 - i]
    if n - 2 - i >= 0:
        arr[n - 1 - i] = arr[n - 2 - i]
        arr[n - 2 - i] = t

for a in arr:
    print(a, end=" ")
