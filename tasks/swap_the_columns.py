arr = [int(i) for i in input().split()]

matrix = []

for i in range(arr[0]):
    n = [int(i) for i in input().split()]
    matrix.append(n)

indexes = [int(i) for i in input().split()]

for array in matrix:
    temp = array[indexes[0]]
    temp_2 = array[indexes[1]]
    array[indexes[1]] = temp
    array[indexes[0]] = temp_2
    for a in array:
        print(a, end=' ')
    print()

