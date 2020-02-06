bool = True

max = 0

while bool:
    i = int(input())
    if max < i:
        max = i
    if i == 0:
        bool = False

print(max)