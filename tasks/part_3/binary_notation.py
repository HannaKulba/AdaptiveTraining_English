import re

try:
    while True:
        i = input()
        number = re.findall(r'[\d]+', i)
        if len(number) == 1:
            if int(number[0], 2) % 3 == 0:
                print(number[0])
except EOFError:
    pass
