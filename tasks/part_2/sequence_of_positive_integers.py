array = [int(i) for i in input().split()]
array.reverse()
for a in array:
    if a > 0:
        print(a, end=" ")
