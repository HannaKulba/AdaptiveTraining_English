n = input()
sum = 0
for i in range(int(n)):
    num = input()
    if num.endswith('4'):
        sum += int(num)

print(sum)
