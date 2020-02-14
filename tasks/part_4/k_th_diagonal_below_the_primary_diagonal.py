import numpy as np


def create_matrix(n):
    matrix = []
    for _ in range(n):
        list = [int(i) for i in input().split()]
        matrix.append(list)
    return matrix


def print_diagonal(k, matrix):
    matrix = np.array(matrix)
    diagonal = matrix.diagonal(-k)
    for _ in diagonal:
        print(_, end=' ')


if __name__ == '__main__':
    n = int(input())
    matrix = create_matrix(n)
    k = int(input())
    print_diagonal(k, matrix)
