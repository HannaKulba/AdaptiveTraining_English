N = int(input())
array = [int(i) for i in input().split()]

set_list = set()

for a in array:
    if set_list.__contains__(a):
        continue
    else:
        set_list.add(a)

print(len(set_list))
