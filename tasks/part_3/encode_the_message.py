map_list = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}

input_string = input()

for char in input_string:
    print(map_list[char], end='')
