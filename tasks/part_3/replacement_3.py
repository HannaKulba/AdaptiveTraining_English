import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    result = re.sub(r'\b(a|A+)+\b', 'argh', line, 1)
    print(result)
