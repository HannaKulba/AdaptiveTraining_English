def factorial(n):
    result = 1
    count = 1
    while count <= n:
        result *= count
        count += 1
    return result


def find_smaller_number(input_num):
    for i in range(1, input_num):
        fact = factorial(i)
        if fact > input_num:
            print(i)
            break


if __name__ == '__main__':
    M = int(input())
    find_smaller_number(M)
