'''
    LIMITED SUM

    Your task is to implement a function limited_sum(values, limit) that
    returns the maximum sum of a subset of values such that the sum is
    less than or equal to limit. The values and limit are assumed to be 
    non-negative integers. E.g., for values = [7, 5, 13, 11, 19] and limit = 28, 
    the largest sum less than or equal to the limit is 26 = 7 + 19.

    Input:  The first line contains a Python list values with at most 100 
            non-negative integers. The second line contains a non-negative
            integer limit <= 20_000.

    Output: The result of calling limited_sum(values, limit).

    Example:

      Input:  [7, 5, 13, 11, 19]
              28

      Output: 26

    Note: The below code already handles reading the input and printing
          the result of calling limited_sum(values, limit).
'''


def limited_sum(values, limit):
    # insert code
    sums = {0}
    for n in sorted(values): 
        sums.update({n+x for x in sums if n+x <= limit})
    
    return max(sums)





values = eval(input())
limit = int(input())
print(limited_sum(values, limit))