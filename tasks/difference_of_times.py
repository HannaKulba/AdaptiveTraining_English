h = int(input())
m = int(input())
s = int(input())

h_1 = int(input())
m_1 = int(input())
s_1 = int(input())

seconds = h * 3600 + m * 60 + s
seconds_1 = h_1 * 3600 + m_1 * 60 + s_1

print(seconds_1 - seconds)
