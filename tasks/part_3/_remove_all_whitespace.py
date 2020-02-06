import re

text = input()
res = re.sub(r'\s+([.,?!);:"\'\-\t+\s])', r'\1', text)
print(res)
