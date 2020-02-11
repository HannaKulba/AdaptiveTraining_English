arr = input().split("_")

if len(arr) == 1 and arr[0] == 1:
    print(arr[0].upper())
elif len(arr) == 1:
    print(arr[0][0].upper() + arr[0][1:len(arr[0])].lower(), end='')
else:
    for a in arr:
        if a == '':
            continue
        else:
            print(a[0].upper() + a[1:len(a)].lower(), end='')
