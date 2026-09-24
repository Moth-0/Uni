'''
    DENSE SAMPLE

    Given a list of positive weights, the task is to find a subsequence (sample)
    of the weights such that 1) the subsequence has minimum sum, 2) among every
    three consecutive weights in the lists, at least one of them is in the 
    sample. It is guaranteed that there is a unique minimum weight solution.

    Input:  A single Python list L of integers (weights), where 
            3 <= len(L) <= 100 and all elements are between 1 and 1000.

    Output: A single line with a Python list of strictly increasing indexes 
            into L defining a sample, where the weights in the sample have
            minimum sum, and among every three consecutive indexes into L, 
            at least one is in the sample.

    Example:

      Input:  [7, 5, 7, 5, 7, 6, 7]

      Output: [1, 4]

      Explanation: In the input list L, L[1] + L[4] = 5 + 7 = 12 achieves the 
      minimum possible weight sum, if for all three consecutive indexes at least 
      one index is in the sample.
    
    Note: The below code already reads the input list L.
'''

L = eval(input())
# insert code
from functools import cache


def func(L):
    n = len(L)
    
    @cache
    def solve(i):
        # if there is less then 3 elements left, we dont need to add more
        if i >= n-3:
            return L[i], [i]
        
        # run recursion on the next three numbers from out current idx
        new_sum, new_idx = min(solve(i+1), solve(i+2), solve(i+3), 
                               key=lambda x: x[0]) # pick the one with min value 

        # update and return the new sum 
        sum = L[i] + new_sum
        idx = [i] + new_idx

        return sum, idx
    
    out0 = solve(0)
    out1 = solve(1)
    out2 = solve(2)

    value, index = min(out0, out1, out2, 
                       key=lambda x: x[0])
    
    return index

    
        
print(func(L))