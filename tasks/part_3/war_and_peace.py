def print_results(arr):
    set_words = list(set(arr))
    for word in set_words:
        print(word + ' ' + str(arr.count(word)))


if __name__ == '__main__':
    words = input().lower().split()
    print_results(words)
