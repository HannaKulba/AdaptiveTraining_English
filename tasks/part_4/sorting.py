def sort_indexes(list):
    indexes = {}
    for i in range(len(list)):
        indexes.update({i+1: list[i]})

    list = sorted(list)
    for elem in list:
        for k in indexes.keys():
            if elem == indexes[k]:
                print(k, end= ' ')


if __name__ == '__main__':
    n = int(input())
    list = [int(i) for i in input().split()]
    sort_indexes(list)
