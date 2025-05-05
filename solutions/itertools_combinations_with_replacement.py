# URL: https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement


string, n= input().split()
n = int(n)

if not string.isupper():
    print("Input string must contain only uppercase characters!")
else: 
    for comb in combinations_with_replacement(sorted(string), n):
        print("".join(comb))
    


   
