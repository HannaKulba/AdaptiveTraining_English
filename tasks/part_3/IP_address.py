import re


def is_ip(ip):
    result = re.search(
        r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$',
        ip)
    if result is not None:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    ip = input()
    is_ip(ip)
