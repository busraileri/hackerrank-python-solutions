# URL: https://www.hackerrank.com/challenges/np-arrays/problem


import numpy as np

def arrays (arr):
    # complete this function
    # use numpy.array 

    arr = np.array(arr, float)
    arr = arr[::-1]
    return arr


arr = input().strip().split(' ')
result = arrays(arr)
print(result)