import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    words = re.split(r'[.,"\':;?!#%&\s*]', line)

    for word in words:
        mid = len(word) // 2
        if len(word) > 1 and word[0: mid] == word[mid:len(word)]:
            print(line)
            break
        elif '-' in word and len(word) > 1:
            parts = word.split('-')
            if len(parts) > 1 and parts[0] == parts[1]:
                print(line)
                break
