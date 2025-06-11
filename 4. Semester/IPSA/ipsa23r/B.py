'''
    CLOSE PRODUCT

    Your task is to write a function close_product(values, target), that takes
    a list of non-negative integer values and a non-negative integer target,
    and returns the largest value less than or equal to target that is the
    product of two values in the list, possibly the square of one value. 
    If no such value exists, the function should return zero. E.g.,

       close_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 23) 

    should return 21 = 3 * 7.

    Input:  A python expression using the function close_product(values, target).
            It is guaranteed that the list values contains at most 100
            non-negative integers.

    Output: The result of evaluating the expression. 

    Example: 

      Input:  close_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 26) 

      Output: 25

    Note: The below code already reads and evaluates the input.
'''


def close_product(values, target):
    # insert code
    return max([x*y for x in values for y in values if x*y <= target])


print(eval(input()))
