arr = [int(i) for i in input().split()]

sum = 0
for a in range(len(arr)):
    if a % 2 == 1:
        print(arr[a])
    if arr[a] % 2 == 0:
        sum += arr[a]

print(sum)
