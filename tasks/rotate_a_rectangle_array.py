n = [int(i) for i in input().split()]

array = []

for i in range(n[0]):
    strs = [int(i) for i in input().split()]
    array.append(strs)
rotated = list(zip(*array[::-1]))

for i in range(len(rotated)):
    for j in range(len(rotated[i])):
        print(rotated[i][j], end=" ")
    print()
