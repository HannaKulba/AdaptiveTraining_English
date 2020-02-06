n = int(input())
sum = 0
for i in range(n):
    number = int(input())
    if number % 6 == 0:
        sum += number

print(sum)
