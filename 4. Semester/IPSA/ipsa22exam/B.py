'''
    MAXSUM

    Write a function maxsum(L), that given a list of integers,
    returns the maximum sum that can be obtained from a subset of the
    elements in L, e.g. for L = [3, -2, 1, 0, 4], the maximum sum is
    3 + 1 + 4 = 8. Note the empty subset has sum 0.

    Input:  A list L of integers, where 0 <= len(L) <= 100 and each
            integer x in L is -1000 <= x <= 1000.

    Output: A line with a single integer, the maximum sum of a subset
            of the elements in L.
    
    Example:

      Input:  [3, -2, 1, 0, 4]

      Output: 8

    Note: The below code already handles reading the input.
'''


def maxsum(L):
    # insert code 
    return sum([n for n in L if n > 0])


L = eval(input())
print(maxsum(L))
