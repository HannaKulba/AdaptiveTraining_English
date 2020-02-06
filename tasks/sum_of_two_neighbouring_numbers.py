array = [int(i) for i in input().split()]
new_array = []

if len(array) == 1:
    new_array.append(array[0])
else:
    for i in range(len(array)):
        prev = i - 1
        next = i + 1
        if prev < 0:
            prev = len(array) - 1
        if next >= len(array):
            next = 0
        new_array.append(array[prev] + array[next])

for i in new_array:
    print(i, end=" ")
