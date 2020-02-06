P, X, Y, K = int(input()), int(input()), int(input()), int(input())

deposit = X * 100 + Y
percent = 1.0 + P / 100

for i in range(K):
    deposit = int(deposit * percent)

print(deposit // 100, deposit % 100)
