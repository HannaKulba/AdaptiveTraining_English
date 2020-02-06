string = input()
pos = 0
c = 0
while pos != -1:
    r = string.find(' ', pos + 1)
    c += 1
    pos = r

print(c)