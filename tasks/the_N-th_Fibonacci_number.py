def fib(n):
    first = 0
    second = 1
    count = 1
    t = 0

    if n == 1:
        return second
    else:
        while count < n:
            t = first + second
            first = second
            second = t
            count += 1
    return t


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
