n = int(input())


def get_sum_n(number):
    sum_n = 0
    while number > 0:
        x = number % 10
        sum_n = sum_n + x
        number = int(number / 10)
    return sum_n


summa_n = get_sum_n(n)

i = 1
count = 0
while 0 < i < n:
    sum_i = get_sum_n(i)
    if summa_n == sum_i:
        count += 1
    i += 1

print(count)