import math


def encode(n, string):
    latin_alphabet = ' abcdefghijklmnopqrstuvwxyz'
    dict = {}
    c = 0

    for i in latin_alphabet:
        dict.setdefault(c, i)
        c += 1

    print('Result: "', end='')
    for s in string:
        for f in dict:
            c = math.fabs((f + n) // len(dict))

            if dict[f] == s and f + n < 0:
                print(dict[c * len(dict) + f + n], end='')
            elif dict[f] == s and f + n == 0:
                print(dict[f + n], end='')
            elif dict[f] == s and f + n > 0:
                if f + n < len(dict):
                    print(dict[f + n], end='')
                elif f + n >= len(dict):
                    print(dict[f + n - c * len(dict)], end='')
    print('"')


if __name__ == '__main__':
    n = int(input())
    string = input().strip()
    encode(n, string)
