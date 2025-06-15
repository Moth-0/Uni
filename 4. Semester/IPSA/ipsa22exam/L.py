'''
    SIGNED SUBSET

    Your task is to write a function subset(values, n), that given
    a sorted list of distinct positive integers and an integer n,
    determines if there exists a subset of the values that has sum n,
    possibly by negating some of the values. E.g. subset([1, 5, 11, 17], 7)
    should return True, since 7 = 1 + -5 + 11 = 1 + -11 + 17.

    Input:  A single line with a Python expression calling subset,
            with len(values) <= 40, each value <= 1000, n <= 40000.

    Output: The result of evaluating the expression.

    Example:

      Input:  subset([1, 5, 11, 17], 7)

      Output: True

    Note: The below code already handles the input and output.
'''

from functools import cache


def subset(values, n):
    # insert code
    @cache
    def solve(i, n):
        if n == 0:
            return True
        if i == 0:
            return False
        return solve(i - 1, n) or solve(i - 1, n - values[i - 1]) or solve(i - 1, n + values[i - 1])

    return solve(len(values), n)



print(eval(input()))
