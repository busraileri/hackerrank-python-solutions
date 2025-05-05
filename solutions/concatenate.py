# URL: https://www.hackerrank.com/challenges/np-concatenate/problem

import numpy as np

def main():
    row_a, row_b, cols = map(int, input().split())
    matrix_a = [list(map(int, input().split())) for _ in range(row_a)]
    matrix_b = [list(map(int, input().split())) for _ in range(row_b)]

    arr_a = np.array(matrix_a)
    arr_b = np.array(matrix_b)
    result = np.concatenate((arr_a, arr_b))
    print(result)

main()