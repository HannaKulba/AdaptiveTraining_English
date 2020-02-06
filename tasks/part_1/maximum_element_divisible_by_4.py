n = int(input())
max_4 = 0

while n > 0:
    i = int(input())
    if i % 4 == 0 and max_4 < i:
        max_4 = i
    n -= 1

print(max_4)
