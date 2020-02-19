import heapq


def get_result(n):
    pq = []
    for i in range(n):
        data = input().split()
        if data[0] == 'Insert':
            heapq.heappush(pq, int(data[1]))
        elif data[0] == 'ExtractMax':
            print(heapq.heappop(pq))


if __name__ == '__main__':
    n = int(input())
    get_result(n)
