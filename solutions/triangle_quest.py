# URL: https://www.hackerrank.com/challenges/python-quest-1/problem

for i in range (1, int(input())):
    """
    i = 1  1 * 1 = 1
    i = 2  2 * 11 = 22
    i = 3  3 * 111 = 333

    10 // 9 = 1
    100 // 9 = 11
    1000 // 9 = 111
    
    """ 
    print(i * ((10 ** i) // 9))