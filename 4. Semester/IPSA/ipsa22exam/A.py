'''
    INTERVAL SUM

    Your task is to write a function interval_sum(i, j), that returns
    the sum i + (i + 1) + ... + j. Eg. for i = 10 and j = 13 the sum
    returned should be 10 + 11 + 12 + 13 = 46.

    Input:  Two lines, containing integers i and j, respectively.
            It is guaranteed that 1 <= i <= j <= 100.

    Output: The sum i + (i + 1) + ... + j.

    Example:

      Input:  10
              13

      Output: 46

    Note: The below code already handles the input and ouput.
'''


def interval_sum(i, j):
    # insert code
    sum = 0 
    while i <= j: 
        sum += i 
        i += 1
    return sum

i = int(input())
j = int(input())
print(interval_sum(i, j))
