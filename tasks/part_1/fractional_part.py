n = input()

if len(n.split(".")) == 1:
    print(0)
else:
    print("0." + n.split(".")[1])
