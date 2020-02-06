def get_rome_date(some_date):
    dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5,
            'IV': 4, 'I': 1}

    rome = ''
    for d in dict:
        s = divmod(some_date, dict[d])
        rome += d * s[0]
        some_date = s[1]
    return rome


if __name__ == '__main__':
    date = int(input())
    print(get_rome_date(date))
