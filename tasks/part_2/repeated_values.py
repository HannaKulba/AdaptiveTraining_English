arr = [int(i) for i in input().split()]
set_n = set()

for a in arr:
    if arr.count(a) > 1:
        set_n.add(a)

for s in set_n:
    print(s, end=' ')
