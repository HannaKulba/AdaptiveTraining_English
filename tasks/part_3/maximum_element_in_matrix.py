nm = [int(i) for i in input().split()]
matrix = []

for _ in range(nm[0]):
    list = [int(i) for i in input().split()]
    matrix.append(list)

max = matrix[0][0]
for n in range(len(matrix)):
    for elem in matrix[n]:
        if elem > max:
            max = elem

for n in range(len(matrix)):
    try:
        index = matrix[n].index(max)
        print(n, index)
        break
    except ValueError:
        pass
