def print_fraction_numbers(drob):
    a = int(drob.split('/')[0])
    b = int(drob.split('/')[1])
    c = 0

    while a != 0 and b != 0:
        if a > b:
            c = a // b
            print(c, end=' ')
            a = a % b
        elif a == b:
            c = a
            print(c, end=' ')
            break
        elif a < b:
            if c == 0:
                print(0, end=' ')
            c = b // a
            b = b % a
            print(c, end=' ')


if __name__ == '__main__':
    drob = input()
    print_fraction_numbers(drob)