d = int(input())
words = []

for _ in range(d):
    i = input()
    words.append(i.lower())

result = set()
l = int(input())

for _ in range(l):
    i = input().split()
    array = []
    for j in i:
        array.append(j.lower())

    for word in words:
        if word in array:
            array.remove(word)

    if len(array) > 0:
        for a in array:
            for j in i:
                if j.lower() == a:
                    result.add(j)

for r in result:
    print(r)
