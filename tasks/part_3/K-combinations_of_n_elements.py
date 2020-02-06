import itertools


def get_combinations(k, n):
    res = itertools.combinations(range(n), k)
    for i in res:
        for j in i:
            print(j, end=" ")
        print()


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    get_combinations(arr[0], arr[1])
