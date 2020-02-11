import re

text = input()
res = re.sub(r'(\s|\t)+([.,?!);:"\'\-\t+\s])', r'\2', text)
print(res)
