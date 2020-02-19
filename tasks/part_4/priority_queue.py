import heapq


def get_result(n):
    pq = []
    reversed_nums = [-num for num in pq]
    heapq.heapify(reversed_nums)
    for i in range(n):
        data = input().split()
        if data[0] == 'Insert':
            heapq.heappush(reversed_nums, -int(data[1]))
        elif data[0] == 'ExtractMax':
            res = -heapq.heappop(reversed_nums)
            print(res)


if __name__ == '__main__':
    n = int(input())
    get_result(n)
