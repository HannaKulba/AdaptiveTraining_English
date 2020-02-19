import sys

dict = {}
for line in sys.stdin:
    data = line.split()
    site = data[0]
    sec = int(data[1])
    if site in dict:
        sum = dict[site][0] + sec
        count = dict[site][1] + 1
        result = [sum, count]
        dict.update({site: result})
    else:
        dict.update({site: [sec, 1]})

for site in dict.keys():
    print(site + '\t' + str(int(dict[site][0] / dict[site][1])))
