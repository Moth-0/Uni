'''
    DOMINANCE

    Write a function dominance(L) that determines if a list of integers L,
    contains most positive, negative or zero values.

    Input:  A line containing a Python list of at most 100 integers.

    Output: A single line containing one of the words 'positive',
            'negative', 'zero', 'draw'. If there are more positive
            integers than negative integers and more positive integers
            than zero values, then 'positive' should be returned.
            Similarly 'negative' or 'zero' should be returned, if
            negative or zero values are most frequent. If there is
            not a unique most frequent answer, then 'draw' should be
            returned.

    Example:

      Input:  [-1, -2, 42, 42, 0, -3]

      Output: negative

    Note: The below code already handles input and output.
'''


def dominance(L):
    # insert code
    positive = sum(e > 0 for e in L)
    negative = sum(e < 0 for e in L)
    zero = sum(e == 0 for e in L)
        
    if positive > max(zero, negative):
        return 'positive'
    if negative > max(zero, positive):
        return 'negative'
    if zero > max(positive, negative):
        return 'zero'
    return 'draw'



L = eval(input())
print(dominance(L))
