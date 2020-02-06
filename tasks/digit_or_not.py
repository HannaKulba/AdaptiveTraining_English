n = input()

try:
    int(n)
    print('yes')
except ValueError:
    print('no')
