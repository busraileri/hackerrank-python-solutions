# URL: https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

string, k = input().split()
k = int(k)



if not string.isupper():
     print("Input string must contain only uppercase characters!")
else:
    for i in range(1, k+1):
        combs = combinations(sorted(string), i)
    
        for combination in combs:
            print("".join(combination))