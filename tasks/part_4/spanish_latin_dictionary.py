from collections import OrderedDict

d = {}
l = int(input())
for i in range(l):
    w = input()
    v1 = w.split(' - ')[0]
    k1 = w.split(' - ')[1].split(', ')

    for i in range(len(k1)):
        if k1[i] in d:
            d[k1[i]].append(v1)
        else:
            d[k1[i]] = [v1]

dd = OrderedDict(sorted(d.items(), key=lambda t: t[0]))

print(len(dd))
for key, val in dd.items():
    s = val[0]
    for i in range(1, len(val)):
        s = s + ', ' + val[i]
    print(key + ' - ' + s)
