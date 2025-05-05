# URL: https://www.hackerrank.com/challenges/itertools-permutations/problem


from itertools import permutations

string, k = input().split()
k = int(k)
if not string.isupper():
    print("Input string must contain only uppercase characters!")
else:
    perms = permutations(sorted(string), k)

    for perm in perms:
        print("".join(perm))