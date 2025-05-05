# URL: https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby

data = input()

for k, g in groupby(data):
    print(f"({len(list(g))}, {k})", end=' ')
