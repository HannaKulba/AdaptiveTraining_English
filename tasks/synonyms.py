n = int(input())
dict = {}

for i in range(n):
    s = input().split()
    dict.update({s[0]: s[1]})

word = input()

for k in dict.keys():
    if dict[k] == word:
        print(k)
        break
    elif k == word:
        print(dict[k])
        break
