import re


def is_number(n):
    if len(n) == 11:
        result = re.match(r'(19\d+)|(19\s\d+\s\d+)', n)
        if result is not None:
            return 'Yes'
        else:
            return 'No'
    else:
        return 'No'


if __name__ == '__main__':
    number = input().strip()
    print(is_number(number))
