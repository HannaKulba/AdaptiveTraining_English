array = input().split()
sum = 0
for a in array:
    try:
        t = int(a)
        sum += t
    except ValueError:
       pass

print(sum)
