def print_difference(set_1, set_2):
    res = []

    for s in set_1:
        if s not in set_2:
            res.append(s)

    for s in set_2:
        if s not in set_1:
            res.append(s)

    for r in sorted(res):
        print(r, end=' ')


if __name__ == '__main__':
    set_1 = [int(i) for i in input().split()]
    set_2 = [int(i) for i in input().split()]
    print_difference(set_1, set_2)
