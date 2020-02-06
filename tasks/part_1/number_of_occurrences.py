s, t = input(), input()
c = 0


def func(stroka):
    global c
    for i in range(len(stroka)):
        if stroka[i:].startswith(t):
            c += 1
        else:
            continue


func(s)
print(c)