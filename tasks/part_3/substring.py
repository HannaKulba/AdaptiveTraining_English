def count_substring(string, sub):
    count = 0
    for i in range(len(string)):
        new_string = string[i:]
        if new_string.startswith(sub):
            count += 1
    return count


if __name__ == '__main__':
    s, t = input(), input()
    print(count_substring(s,t))