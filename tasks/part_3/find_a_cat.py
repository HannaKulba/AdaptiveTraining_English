import re

try:
    while True:
        i = input()
        if re.search(r'(\bcat\b)|(\Bcat\B)', i):
            print(i)
except EOFError:
    pass
