V = int(input())
T = int(input())

if V > 0:
    distance = (V * T) % 109
    print(distance)
elif V == 0:
    print(0)
else:
    abs_distance = abs(V * T)
    abs_distance = abs_distance % 109
    distance = 109 - abs_distance
    if abs_distance == 0:
        distance = 0
    print(distance)
