n = input().split(' ')
count = 0

for i in n:
    if i == 'A':
        count += 1

print(f"{count/len(n) :.2f}")
