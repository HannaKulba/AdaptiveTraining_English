def print_max_pairwise_product(list):
    max = list[0]
    index = 0

    while index < len(list):
        for i in range(len(list)):
            if index != i:
                if list[index] * list[i] > max:
                    max = list[index] * list[i]
        index += 1
    print(max)


if __name__ == '__main__':
    n = int(input())
    list = [int(i) for i in input().split()]
    print_max_pairwise_product(list)
