def modify_list(l):
    for i in range(len(l)):
        if l[i] % 2 == 1:
            l[i] = 0
        else:
            l[i] = l[i] // 2

    for i in range(len(l) - 1, -1, -1):
        if (l[i] == 0):
            l.pop(i)


lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)  # [1, 2, 3]
modify_list(lst)
print(lst)
