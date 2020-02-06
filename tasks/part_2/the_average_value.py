bool = True

sum = 0
count = 0

while bool:
    i = int(input())
    sum += i
    count += 1
    if i == 0:
        bool = False
        count -= 1

print(sum/count)
