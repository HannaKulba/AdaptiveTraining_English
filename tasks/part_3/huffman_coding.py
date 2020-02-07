########################################################################################
# method 'encode(frequency)' was taken from here: https://gist.github.com/nboubakr/0eec4ea650eeb6dc21f9
########################################################################################
import heapq
from collections import defaultdict


def encode(frequency):
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


def get_Huffman_encode_symbols(data):
    dict = {}
    frequency = defaultdict(int)
    for symbol in data:
        frequency[symbol] += 1
    huff = encode(frequency)
    for p in huff:
        if p[1] == '':
            p[1] = 0
        dict.update({p[0]: p[1]})
    return dict


def get_encoded_results(data, dict):
    res = ''
    for l in data:
        res += str(dict[l])

    print(len(dict), len(res))
    for d in dict.keys():
        print(d + ': ' + str(dict[d]))
    print(res)


if __name__ == '__main__':
    data = input()
    dict = get_Huffman_encode_symbols(data)
    get_encoded_results(data, dict)
