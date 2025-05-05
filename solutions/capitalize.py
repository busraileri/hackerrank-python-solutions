# URL: https://www.hackerrank.com/challenges/capitalize/problem

import math
import os
import random
import re
import sys

def solve(s):
    words = s.split(" ")

    new_words = []
    for word in words:
        new_words.append(word.capitalize())
    
    result = " ".join(new_words)
    return result
  

if __name__ == '__main__':
    s= input()
    result = solve(s)
    print(result)
   
