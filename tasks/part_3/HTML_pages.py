import requests
import re

list2 = []
s1, s2 = input(), input()

result = requests.get(s1)
findUrl = re.findall(r'(href=[\'"]?([^\'" >]+)")', result.text)

for l in findUrl:
    res = requests.get(l[1])
    findUrl_1 = re.findall(r'(href=[\'"]?([^\'" >]+)")', res.text)
    for f in findUrl_1:
        list2.append(f[1])

if s2 in list2:
    print('Yes')
else:
    print('No')