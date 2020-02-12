import sys

for line in sys.stdin:
    line = line.rstrip()
    line = line.replace("human", "computer")
    print(line)