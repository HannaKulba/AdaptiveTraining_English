string = input()

i = 0
result = ''

while i < len(string):
    letter = string[i]
    if i + 1 < len(string):
        if letter == string[i + 1]:
            result += letter
        else:
            result += letter + ' '
    else:
        result += letter
    i += 1

arr = result.split()
for a in arr:
    if len(a) == 1:
        print(a[0], end='')
    else:
        print(str(len(a)) + a[0], end='')
