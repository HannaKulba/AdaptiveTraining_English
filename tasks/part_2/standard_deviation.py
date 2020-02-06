import math

n = int(input())
arr = []
arr.append(n)

while n != 0:
    n = int(input())
    if n != 0:
        arr.append(n)

sum = 0
for a in arr:
    sum += a

average = sum / len(arr)

sum_2 = 0

for a in arr:
    t = (a - average) ** 2
    sum_2 += t

deviation = math.sqrt((sum_2 / (len(arr) - 1)))
print(deviation)
