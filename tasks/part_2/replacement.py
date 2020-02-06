arr = input().split()
string = ""
for i in range(len(arr)):
    if i == len(arr) - 1:
        string += arr[i]
    else:
        string += arr[i] + "_"

print(string)
