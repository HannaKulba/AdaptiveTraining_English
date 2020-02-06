n = input()
first_part = ''
second_part = ''
new_n = ''
if len(n) == 1:
    new_n = '000' + n
elif len(n) == 2:
    new_n = '00' + n
elif len(n) == 3:
    new_n = '0' + n
else:
    new_n = n

first_part = new_n[0:2]
second_part = second_part.join(reversed(new_n[2:4]))

if first_part == second_part:
    print(1)
else:
    print(37)
