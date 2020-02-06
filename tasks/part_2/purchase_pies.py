a = int(input())
b = int(input())
count = int(input())

if b * count >= 100:
    print(a * count + (b * count) // 100, (b * count) % 100)
else:
    print(a * count, b * count)
