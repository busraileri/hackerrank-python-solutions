# URL: https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from itertools import combinations

n = int(input())  #total nums of letters
letters = input().split() 
k = int(input()) 

all_combinations = list(combinations(letters, k))

count=0
for comb in all_combinations:
    if 'a' in comb:
        count += 1 

probability = count / len(all_combinations)

print(f"{probability:.3f}")


