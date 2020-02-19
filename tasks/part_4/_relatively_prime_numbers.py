# def gcd(x, y):
#     while y != 0:
#         t = x
#         x = y
#         y = t % y
#     return x
#
#
# def get_prime_numbers(n):
#     count = 0
#     for i in range(1, n):
#         if gcd(i, n) == 1:
#             count += 1
#     return count

def run(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:

            while n % p == 0:
                n = n // p
                result = result * (1.0 - 1.0 / float(p))
                p = p + 1

        if n > 1:
            result = result * (1.0 - 1.0 / float(n))
    return int(result)


def get_prime_numbers(n):
    count = 0
    for i in range(1, n):
        if run(n) is int:
            count += 1
    return count


if __name__ == '__main__':
    n = int(input())
    print(get_prime_numbers(n))
