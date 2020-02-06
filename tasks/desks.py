class_A = int(input())
class_B = int(input())
class_C = int(input())

array = [class_A, class_B, class_C]
total = 0

for i in array:
    if i % 2 == 1:
        total += i // 2 + 1
    else:
        total += i // 2

print(total)
