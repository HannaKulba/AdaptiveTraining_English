def is_triangle(a, b, c):
    if a + b > c and a + c > b and c + b > a:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    a, b, c = int(input()), int(input()), int(input())
    is_triangle(a, b, c)
