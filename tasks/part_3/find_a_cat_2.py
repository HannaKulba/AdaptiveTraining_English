import sys

for line in sys.stdin:
    line = line.rstrip()
    count = 0
    for i in range(len(line)):
        if line[i:].startswith('cat'):
            count += 1
    if count >= 2:
        print(line)
