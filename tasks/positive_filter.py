array = [int(i) for i in input().split()]


def filter_positive(arr):
    new_arr = []
    for i in arr:
        if i > 0:
            new_arr.append(i)
    return new_arr