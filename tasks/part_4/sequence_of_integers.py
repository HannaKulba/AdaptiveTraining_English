try:
    list = [int(i) for i in input().split()]
    result = []
    for index in range(len(list)):
        if index % 2 != 0:
            result.append(list[index])

    for number in reversed(result):
        print(number, end=' ')
except EOFError:
    pass
