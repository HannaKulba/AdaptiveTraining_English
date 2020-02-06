X = input()

if len(X.split(".")) == 1:
    print(0)
else:
    print(X.split(".")[1][0])
