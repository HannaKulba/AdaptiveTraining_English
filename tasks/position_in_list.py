array = [int(i) for i in input().split()]
index = int(input())
index_arr = []

for i in range(len(array)):
    if array[i] == index:
        index_arr.append(i)

if len(index_arr) == 0:
    print("Missing")
else:
    for i in index_arr:
        print(i, end=" ")
