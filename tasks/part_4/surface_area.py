def coordinates_list():
    coordinates = []
    for _ in range(4):
        input_coord = input().split()
        coordinates.append((float(input_coord[0]), float(input_coord[1])))
    return coordinates


def print_square():
    coordinates = coordinates_list()

    sum_1 = 0
    for i in range(4):
        if i + 1 == 4:
            sum_1 += coordinates[i][0] * coordinates[0][1]
        else:
            sum_1 += coordinates[i][0] * coordinates[i + 1][1]

    sum_2 = 0
    for i in range(4):
        if i + 1 == 4:
            sum_2 += coordinates[0][0] * coordinates[i][1]
        else:
            sum_2 += coordinates[i + 1][0] * coordinates[i][1]

    S = (sum_1 - sum_2) / 2
    print('{:.3f}'.format(S))


if __name__ == '__main__':
    print_square()
