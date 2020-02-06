def get_encoding_phrase(string):
    i = 0
    result = ''

    while i < len(string):
        letter = string[i]
        if i + 1 < len(string):
            if letter == string[i + 1]:
                result += letter
            else:
                result += letter + ' '
        else:
            result += letter
        i += 1

    def print_results():
        nonlocal result
        arr = result.split()
        for a in arr:
            print(a[0] + str(len(a)), end='')

    return print_results()


if __name__ == '__main__':
    string = input()
    get_encoding_phrase(string)
