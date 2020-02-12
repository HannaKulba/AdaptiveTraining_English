import re

text = input()
res = re.sub(r'(\s)+([.,?!);:"\'-])', r'\2', text)
print(res)
