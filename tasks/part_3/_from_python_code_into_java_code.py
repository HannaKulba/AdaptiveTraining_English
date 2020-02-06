arr = input().split("_")

if len(arr) == 1:
    print(arr[0].upper())
else:
    for a in arr:
        if a == '':
            continue
        else:
            print(a[0].upper() + a[1:len(a)].lower(), end='')
