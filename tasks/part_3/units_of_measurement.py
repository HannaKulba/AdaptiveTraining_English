input = input().split(' ')
numb = float(input[0])
unit_from = input[1]
unit_to = input[3]

dict = {'mile': 1609, 'yard': 0.9144, 'foot': 0.3048, 'inch': 0.0254, 'km': 1000, 'm': 1, 'cm': 0.01, 'mm': 0.001}

res = (numb * dict[unit_from]) / dict[unit_to]
print('%10.2e' % res)
