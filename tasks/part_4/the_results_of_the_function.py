def f(x):
    pass


n = input()
d = {}
for i in range(int(n)):
    inp = int(input())
    if inp not in d:
        d.update({inp: f(inp)})
    print(d[inp])
