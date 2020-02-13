import re


def decode(string):
    result = re.findall(r'(\d+\w|\w)', string)
    for r in result:
        number = re.findall(r'\d+', r)
        letter = re.findall(r'[a-zA-Z]', r)
        if len(number) == 0:
            print(letter[0], end='')
        else:
            print(letter[0] * int(number[0]), end='')


if __name__ == '__main__':
    n = input()
    decode(n)
