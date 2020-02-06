bool = True

while bool:
    i = int(input())
    if i < 10:
        continue
    elif i > 100:
        bool = False
    else:
        print(i, end="\n")
