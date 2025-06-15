'''
    SUBSET

    Your task is to write a function subset(values, k, n), that given
    a sorted list of distinct positive integer values and two positive
    integers k and n, determines if there exists a subset of values of
    size k and with sum n. If a solution exist, the lexicopgraphically
    smallest list with a solution should be returned.
    If no solution exist, False should be returned.

    Input:  A single line with a Python expression calling subset,
            with len(values) <= 40 and each value <= 1000.

    Ouput:  The result of evaluating the expression.

    Example:

      Input:  subset([2, 3, 5, 7, 9, 14, 17], 3, 19)

      Output: [2, 3, 14]

      Five subsets achieve sum 19:
      
          [2, 17] [5, 14] [2, 3, 14] [3, 7, 9] [2, 3, 5, 9] 

      Among the two solutions with three elements, [2, 3, 14] is
      lexicographically smaller than [3, 7, 9].

    Note: The below code already handles the input and output.
'''
from functools import cache

def subset(values, k, n):
    @cache
    def solve(i, k, n): 
        if k == 0: 
            return [] if n==0 else False
        if k > len(values) - i:
            return False
        if values[i] <= n:
            solution = solve(i + 1, k - 1, n - values[i])
            if solution != False:
                return [values[i]] + solution
        return solve(i + 1, k, n)
    
    return solve(0, k, n)  
        


print(eval(input()))
