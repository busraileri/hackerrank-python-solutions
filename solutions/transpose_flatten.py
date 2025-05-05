# URL: https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

import numpy as np

def main():
    rows, cols = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(rows)]

    arr = np.array(data)
    print(arr.T)
    print(arr.flatten())

main()