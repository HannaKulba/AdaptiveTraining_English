string = input()

length = len(string)

countC = string.lower().count('c')
countG = string.lower().count('g')

print(float((countC + countG) / length * 100))
