n = int(input())
c = 0
doughterParent = {}
while c < n:
    exc, *e = input().split()
    if ':' in e:
        e.remove(':')
    doughterParent.update({exc: e})
    c += 1

m = int(input())
cc = 0
list = []
while cc < m:
    a = input()
    list.append(a)
    cc += 1


def f(a, d):
    for b in doughterParent:
        if a in doughterParent[b]:
            d.append(b)
            f(b, d)
    return d


deleted = {}
for l in list:
    ddd = []
    sss = f(l, ddd)
    deleted.update({l: ddd})

mmm = {}


def func(spis, potomki):
    for s in spis:
        for key in potomki:
            a = spis.index(s)
            b = spis.index(key)
            if (s in potomki[key]) and (a > b):
                mmm.update({s: ''})


func(list, deleted)

for i in mmm:
    print(i)
