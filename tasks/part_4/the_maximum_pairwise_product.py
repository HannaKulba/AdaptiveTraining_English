def print_max_pairwise_product(list):
    max_in_list = max(list)
    list.remove(max_in_list)
    next_max_in_list = max(list)
    print(max_in_list * next_max_in_list)


if __name__ == '__main__':
    n = int(input())
    list = [int(i) for i in input().split()]
    print_max_pairwise_product(list)
