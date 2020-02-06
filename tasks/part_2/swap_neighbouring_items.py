length = int(input())
array = [int(i) for i in input().split()]

arr = []

for a in range(length):
    if a % 2 == 0:
        if a + 1 < length:
            arr.append(array[a + 1])
            arr.append(array[a])
        else:
            arr.append(array[a])

for a in arr:
    print(a, end=" ")
