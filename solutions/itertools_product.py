# URL: https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product

A = map(int, input().split())
B = map(int, input().split())

cartesian = product(A, B)

print(*cartesian)