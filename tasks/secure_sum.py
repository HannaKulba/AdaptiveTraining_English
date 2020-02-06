def sum(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return Exception("TypeError")
    else:
        if a <= 0 or b <= 0:
            return Exception("ValueError")
        else:
            return int(a) + int(b)


print(sum(1, 8))
print(sum(-1,8))
print(sum(1, '0'))
