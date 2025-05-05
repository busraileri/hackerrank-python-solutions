# URL: https://www.hackerrank.com/challenges/incorrect-regex/problem

import re 

def is_valid_regex(s):
    try:
        re.compile(s)
        return True
    except re.error:
        return False
    

t = int(input())
for _ in range(t):
    print(is_valid_regex(input()))