array = [int(i) for i in input().split()]
x_1 = array[0]
y_1 = array[1]
x_2 = array[2]
y_2 = array[3]

if x_1 == x_2 or y_1 == y_2:
    print('YES')
elif abs(x_2 - x_1) == abs(y_2 - y_1):
    print('YES')
else:
    print('NO')
