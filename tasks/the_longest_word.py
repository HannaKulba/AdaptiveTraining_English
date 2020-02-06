string_array = input().split()

length = 0
long_word = ""

for s in string_array:
    len_w = len(s)
    if len_w > length:
        length = len_w
        long_word = s

print(long_word)
