array = [int(i) for i in input().split()]

min = array[0]
max = array[0]

for i in array:
    if i > max:
        max = i
    if i < min:
        min = i

print(max, min)
