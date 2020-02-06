n = int(input())
arr_nums = [int(i) for i in input().split()]
arr_nums.sort()

for a in arr_nums:
    print(a, end=" ")
