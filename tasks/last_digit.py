def fib_digit(n):
    first = 0
    second = 1
    count = 1
    t = 0

    if n == 1:
        return first
    else:
        while count < n:
            a = first % 10
            b = second % 10
            t = (a + b) % 10
            first = b
            second = t
            count += 1
    return t


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
