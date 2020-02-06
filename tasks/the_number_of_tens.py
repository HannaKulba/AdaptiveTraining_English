N = int(input())

array = []

while N > 0:
    array.append(N % 10)
    N = N // 10

try:
    print(array[1])
except IndexError:
    print(0)
