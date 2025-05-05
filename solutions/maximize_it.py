# URL: https://www.hackerrank.com/challenges/maximize-it/problem

from itertools import product

K, M = map(int, input().split())

lists = []

for _ in range(K):
    lists.append(list(map(int, input().split()))[1:])
   

max_value = 0

for combination in product(*lists):
    total = sum(x**2 for x in combination)
    max_value = max(max_value, total % M)


print(max_value)