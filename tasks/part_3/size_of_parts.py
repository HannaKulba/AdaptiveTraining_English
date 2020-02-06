def detect_parts(number):
    large = 0
    small = 0
    perfect = 0

    for i in range(number):
        n = int(input())
        if n == 1:
            large += 1
        elif n == -1:
            small += 1
        elif n == 0:
            perfect += 1

    print(str(perfect), str(large), str(small))


if __name__ == '__main__':
    n = int(input())
    detect_parts(n)
