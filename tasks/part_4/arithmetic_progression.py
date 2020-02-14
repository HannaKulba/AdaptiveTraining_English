def is_arithmetic_progression(list):
    list = sorted(list)

    if len(list) == 1:
        print('Yes')
    elif len(list) > 1:
        difference = list[1] - list[0]
        result = 1
        for i in range(len(list)):
            if i + 1 < len(list) and list[i] + difference == list[i + 1]:
                result += 1
        if result == len(list):
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    list = [int(i) for i in input().split()]
    is_arithmetic_progression(list)
