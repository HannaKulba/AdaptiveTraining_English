def is_ip(ip):
    arr = ip.split('.')
    res = 0
    try:
        for a in arr:
            if 0 <= int(a) <= 255:
                res += 1
        if res == 4:
            print('YES')
        else:
            print('NO')
    except ValueError:
        if res != 4:
            print('NO')


if __name__ == '__main__':
    ip = input()
    is_ip(ip)
