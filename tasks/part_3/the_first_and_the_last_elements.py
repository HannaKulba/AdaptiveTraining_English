def f(ls):
    array = []
    array.append(ls[0])
    array.append(ls[len(ls) - 1])
    return array


if __name__ == '__main__':
    array = input().split()
    print(f(array))
