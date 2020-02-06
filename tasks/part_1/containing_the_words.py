string_array = input().split()

dict = {}

for w in string_array:
    length = len(w)

    if dict.__contains__(length):
        temp = dict.get(length)
        dict[length] = temp + 1
    else:
        dict.setdefault(length, 1)

for k in sorted(dict.keys()):
    print(str(k) + ": " + str(dict[k]))
