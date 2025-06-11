'''
    DOUBLE

    Your task is to write a function double(values) that takes a list of
    at most 100 integers and returns a list where each value is doubled.

    Input:  A Python list of at most 100 integers.

    Output: A Python list of integers, where each input value is doubled.

    Example:

      Input:  [1, 2, 3, 4, 5]

      Output: [2, 4, 6, 8, 10] 

    Note: The below code already handles input and output.
'''


def double(values):
    # insert code
    return [2*x for x in values]


print(double(eval(input())))
