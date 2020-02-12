d = int(input())
words = []

for _ in range(d):
    i = input()
    words.append(i.lower())

result = set()
l = int(input())

for _ in range(l):
    i = input().split()
    set_list = set()
    for j in i:
        set_list.add(j.lower())

    for word in words:
        if word in set_list:
            set_list.remove(word)

    if len(set_list) > 0:
        for s in set_list:
            for j in i:
                if j.lower() == s:
                    result.add(j)

for r in result:
    print(r)
