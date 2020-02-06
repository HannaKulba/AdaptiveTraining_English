# from math import ceil
#
# h = int(input())
# a = int(input())
# b = int(input())
#
# d = a - b
# print(ceil((h - a) / d + 1))

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_reversed = []

for i in range(len(list)):
    list_reversed.append(list[len(list) - 1 - i])

print(list)
print(list_reversed)
