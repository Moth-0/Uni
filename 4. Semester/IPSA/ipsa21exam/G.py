'''
    VALID RANGE

    Your task is to write a function valid_range(f), that determines
    the range of integers [low, high], both inclusive, for which f is
    defined. It is guaranteed that f(0) is defined, and f(x) throws
    an exception outside the range [low, high].
 
    Input:  A Python expression evaluating to a function.
            It is guaranteed that -1000 <= low <= 0 <= high <= 1000.

    Output: A tuple with (low, high).

    Example:

      Input:  lambda x : 1 / max(0, (1000 - (x - 15) ** 2))

      Output: (-16, 46)

    Note: The below code already handles input and output.
'''


def valid_range(f):
    # insert code

    pass


f = eval(input())
print(valid_range(f))
