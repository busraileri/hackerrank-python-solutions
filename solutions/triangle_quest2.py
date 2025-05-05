# URL: https://www.hackerrank.com/challenges/triangle-quest-2/problem


""" 10 // 9 = 1
    100 // 9 = 11
    1000 // 9 = 111
        
        and
        
    1 * 1 = 1
    11 * 11 = 121
    111 * 111 = 12321
"""

for i in range(1, int(input())+1):
    print(((10 ** i) // 9) ** 2 )

