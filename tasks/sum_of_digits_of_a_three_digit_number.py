n = int(input())
sum = 0
for i in range(3):
    sum += n % 10
    n = n // 10

print(sum)
