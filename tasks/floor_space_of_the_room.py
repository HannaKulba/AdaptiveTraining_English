import math

figure = input()

if figure == "triangle":
    a = int(input())
    b = int(input())
    c = int(input())
    p = float((a + b + c) / 2)
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(float(S))
elif figure == "rectangle":
    a = int(input())
    b = int(input())
    S = a * b
    print(float(S))
elif figure == "circle":
    a = int(input())
    S = 3.14 * (a ** 2)
    print(float(S))
