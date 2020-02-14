def create_star(n):
    for i in range(n):
        for j in range(n):
            if j == n // 2 or i == n // 2 or j == i or j == n - (i + 1):
                print('* ', end='')
            else:
                print('. ', end='')
        print()


if __name__ == '__main__':
    n = int(input())
    create_star(n)
