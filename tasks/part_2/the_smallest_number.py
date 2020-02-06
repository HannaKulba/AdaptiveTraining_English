a = int(input())


def closest_mod_5(x):
    if x % 5 == 0:
        return x
    else:
        for i in range(x):
            if (x + i) % 5 == 0:
                return x + i


print(closest_mod_5(a))
