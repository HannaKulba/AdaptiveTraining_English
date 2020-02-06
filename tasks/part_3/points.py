import math


def sort_points_by_distance(list):
    dict = {}
    for l in list:
        distance = find_distance(l[0], l[1])
        dict.update({str(l[0]) + ' ' + str(l[1]): distance})

    sorted_points = sorted(dict.items(), key=lambda kv: kv[1])
    for i in sorted_points:
        print(i[0])


def find_distance(a, b):
    return math.sqrt(a ** 2 + b ** 2)


if __name__ == '__main__':
    n = int(input())
    coordinates = []
    for i in range(n):
        coord = [int(i) for i in input().split()]
        coordinates.append(coord)
    sort_points_by_distance(coordinates)
