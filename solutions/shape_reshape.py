# URL: https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy as np

def reshape_and_print(input_list):
    numpy_array = np.array(input_list)
    reshaped_array = np.reshape(numpy_array, (3,3))
    print(reshaped_array)


user_input = input()
input_list = list(map(int, user_input.strip().split()))
reshape_and_print(input_list)