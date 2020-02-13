n = int(input())
c = 0
dict = {}
list = []
while c < n:
    d, *p = input().split()
    dict.update({d: p})
    if ':' in dict[d]:
        dict[d].remove(':')
    c += 1

q = int(input())
cc = 0
while cc < q:
    cl1, cl2 = input().split()
    list.append([cl1, cl2])
    cc += 1


def find(first, second):
    if first == second:
        return 'Yes'
    elif first in dict[second]:
        return 'Yes'
    else:
        for i in dict[second]:
            if find(first, i) == 'Yes':
                return 'Yes'


for arr in list:
    if (arr[0] in dict) and (arr[1] in dict):
        if find(arr[0], arr[1]) == 'Yes':
            print('Yes')
        else:
            print('No')
    else:
        print('No')