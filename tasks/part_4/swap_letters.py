import sys
import re

for line in sys.stdin:
    words = re.findall(r'\w+|\W', line)
    for index in range(len(words)):
        res = re.match(r'\w+', words[index])
        if res is not None and words[index] == res.group(0):
            if len(words[index]) > 1:
                words[index] = words[index][1] + words[index][0] + words[index][2: len(words[index])]

    for word in words:
        print(word,end='')
