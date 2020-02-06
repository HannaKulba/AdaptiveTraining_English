n = int(input())
sum = n
arr = [n]

while sum != 0:
    n = int(input())
    arr.append(n)
    sum += n

sum_sq = 0
for a in arr:
    sum_sq += a ** 2

print(sum_sq)
