'''
    CENTER SUM

    Write a function center_sum(L) that takes a list of integers L as input and
    returns the sum of all integers in L except the smallest and largest integers.

    E.g., if L = [6, 2, 10, 7, 1, 3], the function center_sum(L) should return 18,
    which is the sum of 6, 2, 7, and 3.
    
    Input:  A python list L containing between 3 and 1000 distinct integers, 
            where all integers are in the range -1000 to 1000.

    Output: The sum of all integers in L except the smallest and largest values.

    Example:

      Input:  [6, 2, 10, 7, 1, 3]

      Output: 18
    
    Note: The below code already reads the list L and calls center_sum.
'''


def center_sum(L):
    # insert code
    return sum(L) - max(L) - min(L)


L = eval(input())
print(center_sum(L))
