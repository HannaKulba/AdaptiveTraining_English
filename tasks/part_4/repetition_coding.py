import re

string = input()
result = re.findall(r'\w\d+', string)
for s in result:
    number = re.findall(r'\d+', s)
    letter = re.findall(r'\w', s)
    print(letter[0] * int(number[0]), end='')
